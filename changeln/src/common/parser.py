"""
Copyright 2021 Vitaliy Zarubin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import re

import git
from natsort import natsorted


class Parser:
    def __init__(self, path):
        self.path = path
        self.repo = git.Repo(path)

    def get_branch(self):
        return self.repo.active_branch.name

    def ln_last(self, find_tags):
        pattern = re.compile(find_tags)
        for tag in reversed(natsorted(self.repo.git.tag().split('\n'), key=lambda y: y.lower())):
            for item in self.repo.tags:
                if tag == item.name and pattern.match(tag):
                    return tag
        return 'None'

    def ln_released(self, find_tags):
        return len(self.ln_list_tags(find_tags))

    def ln_list_tags(self, find_tags):
        result_tags = []
        pattern = re.compile(find_tags)
        for tag in reversed(natsorted(self.repo.git.tag().split('\n'), key=lambda y: y.lower())):
            for item in self.repo.tags:
                if tag == item.name and pattern.match(tag):
                    result_tags.append(item)
        return result_tags

    def ln_list_tags_commits(self, find_tags):
        result_tags = []

        list_tags = self.ln_list_tags(find_tags)
        if list_tags:
            to = 'HEAD'
            tag = None
            for tag in list_tags:
                data = list(self.repo.iter_commits('{}...{}'.format(tag, to), no_merges=True))

                result_tags.append(dict(
                    to=('TAG', 'HEAD')[to == 'HEAD'],
                    tag=(to, None)[to == 'HEAD'],
                    data=data
                ))
                to = tag

            if tag is not None:
                result_tags.append(dict(
                    to='TAG',
                    tag=tag,
                    data=list(self.repo.iter_commits(tag, no_merges=True))
                ))

        return result_tags

    def ln_list_groups(self, groups, find_tags):
        result_tags = self.ln_list_tags_commits(find_tags)
        result = []
        for tag in result_tags:
            commits = dict()
            for item in tag['data']:
                for message in item.message.split('\n'):
                    for index in groups:
                        if index not in commits:
                            commits[index] = []
                        optional = re.findall(groups[index], message)
                        if optional:
                            commits[index].append(dict(
                                optional=optional[0],
                                commit=git.Commit(
                                    item.repo,
                                    item.binsha,
                                    tree=item.tree,
                                    author=item.author,
                                    authored_date=item.authored_date,
                                    author_tz_offset=item.author_tz_offset,
                                    committer=item.committer,
                                    committed_date=item.committed_date,
                                    committer_tz_offset=item.committer_tz_offset,
                                    message=message.strip(),
                                    parents=item.parents,
                                    encoding=item.encoding,
                                    gpgsig=item.gpgsig
                                )
                            ))
            for index in groups:
                if index in commits:
                    tag[index] = commits[index]
                else:
                    tag[index] = []
            result.append(tag)
        return result
