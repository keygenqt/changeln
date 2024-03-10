import os
import re

import git
from git import TagReference
from natsort import natsorted


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
                    tags.append(tag)
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
