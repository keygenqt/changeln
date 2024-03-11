import os
import re
from datetime import datetime

import git
from git import TagReference
from natsort import natsorted

from changeln.src.support.output import echo_stderr
from changeln.src.support.texts import AppTexts


class ParseGit:
    def __init__(self, commits: {}, parse_commit: str, filter_tags: str):
        self.commits = commits
        self.parse = parse_commit
        self.filter = filter_tags
        self.repo = git.Repo(os.getcwd())

    # Get list tags
    def get_tags(self) -> [TagReference]:
        tags: [TagReference] = []
        pattern = re.compile(self.filter)
        for tag in reversed(natsorted(self.repo.git.tag().split('\n'), key=lambda y: y.lower())):
            for item in self.repo.tags:
                if tag == item.name and (not self.filter or not pattern.match(tag)):
                    tags.append(item)
        return tags

    # Get latest tag
    def get_last_tag(self) -> str | None:
        tags = self.get_tags()
        if not tags:
            return None
        return str(tags[0])

    # Get count tags
    def get_count_tags(self) -> int:
        tags = self.get_tags()
        return len(tags)

    # Get commits by group
    def get_group_commits(self):
        # Add formats commit message
        def format_commit(commit_tag, commit) -> {}:
            search = None
            if self.parse:
                search = re.search(self.parse, commit.message)
            return dict(
                commit=commit,
                regex=search.groups() if search else [],
                clean=commit.message.split(commit_tag)[1].strip()
            )

        result = []
        for tag_commits in self._get_tag_commits():
            group_commits = []
            for key, value in self.commits.items():
                group_commits.append(dict(
                    name=key,
                    commits=[format_commit(value, commit) for commit in tag_commits['commits'] if
                             value in commit.message]
                ))
            result.append(dict(
                name=tag_commits['name'],
                date=tag_commits['date'],
                commits=tag_commits['commits'],
                group=group_commits,
            ))
        return result

    # Filter commits by tags from config commits
    def _filter_commit_name(self, commits: []):
        def check_tags(message: str) -> bool:
            for value in self.commits.values():
                if value in message:
                    return True
            return False

        return [commit for commit in commits if check_tags(commit.message)]

    # Split multiple tags in one commit
    def _split_multi_commits(self, commits: []):
        result = []
        pattern = '({})'.format(('|'.join(self.commits.values())
                                 .replace('[', r'\[')  # replace tag symbols
                                 .replace(']', r'\]')))
        for commit in commits:
            split = re.split(pattern, commit.message.strip())[1:]
            # One commit
            if len(split) == 2:
                result.append(commit)
            else:
                # Multiple commits
                index = 0
                while index < len(split) - 1:
                    message = '{} {}'.format(split[index].strip(), split[index + 1].strip())
                    result.append(git.Commit(
                        commit.repo,
                        commit.binsha,
                        tree=commit.tree,
                        author=commit.author,
                        authored_date=commit.authored_date,
                        author_tz_offset=commit.author_tz_offset,
                        committer=commit.committer,
                        committed_date=commit.committed_date,
                        committer_tz_offset=commit.committer_tz_offset,
                        message=message,
                        parents=commit.parents,
                        encoding=commit.encoding,
                        gpgsig=commit.gpgsig
                    ))
                    index += 2

        return result

    # Find commits in tags
    def _get_tag_commits(self):
        result = []
        tags = self.get_tags()
        if not tags:
            # Get list HEAD...BOTTOM
            try:
                result.append(dict(
                    name='HEAD',
                    date=datetime.now(),
                    commits=self._split_multi_commits(
                        commits=self._filter_commit_name(
                            commits=self.repo.iter_commits(no_merges=True)
                        )
                    )
                ))
            except ValueError:
                echo_stderr(AppTexts.error_empty_repo())
                exit(1)
        else:
            to = 'HEAD'
            # Get list HEAD...tag...tag
            for tag in tags:
                result.append(dict(
                    name=str(to),
                    date=datetime.now() if isinstance(to, str) else to.commit.committed_date,
                    commits=self._split_multi_commits(
                        commits=self._filter_commit_name(
                            commits=self.repo.iter_commits('{}...{}'.format(tag.name, to), no_merges=True)
                        )
                    )
                ))
                to = tag
            # Get list tag...BOTTOM
            result.append(dict(
                name=str(to),
                date=to.commit.committed_date,
                commits=self._split_multi_commits(
                    commits=self._filter_commit_name(
                        commits=self.repo.iter_commits(to, no_merges=True)
                    )
                )
            ))

        return result
