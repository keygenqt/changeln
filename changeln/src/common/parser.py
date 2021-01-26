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

    def ln_last(self):
        tags = sorted(self.repo.tags, key=lambda t: t.commit.committed_datetime)
        if tags:
            return tags[-1]
        else:
            'None'

    def ln_released(self):
        return len(self.repo.tags)

    def ln_list_tags(self):
        tags = []
        for tag in reversed(natsorted(self.repo.git.tag(merged='master').split('\n'), key=lambda y: y.lower())):
            for item in self.repo.tags:
                if tag == item.name:
                    tags.append(item)
        return tags

    def ln_list_tags_commits(self):
        tags = []

        list_tags = self.ln_list_tags()
        if list_tags:
            to = 'HEAD'
            tag = None
            for tag in list_tags:
                data = list(self.repo.iter_commits('{}...{}'.format(tag, to), no_merges=True))
                tags.append(dict(
                    to=('TAG', 'HEAD')[to == 'HEAD'],
                    tag=(to, None)[to == 'HEAD'],
                    data=data
                ))
                to = tag

            if tag is not None:
                tags.append(dict(
                    to='TAG',
                    tag=tag,
                    data=list(self.repo.iter_commits(tag, no_merges=True))
                ))

        return tags

    def ln_list_groups(self, groups):
        tags = self.ln_list_tags_commits()
        result = []
        for index in groups:
            for tag in tags:
                commits = []
                for item in tag['data']:
                    for message in item.message.split('\n'):
                        optional = re.findall(groups[index], message)
                        if optional:
                            commits.append(dict(
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

                tag[index] = commits
                result.append(tag)
        return result
