"""
Copyright 2021-2024 Vitaliy Zarubin

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
from enum import Enum


# Application texts
class AppTexts(Enum):
    @staticmethod
    def error_dependency_git():
        return '<red>Application</red> "git" <red>not found, install it.</red>'

    @staticmethod
    def error_template_parse(error: Exception):
        return '<red>Template parsing error.</red>\n{}: {}.'.format(type(error).__name__, error)

    @staticmethod
    def error_empty_repo():
        return '<red>Could not find comments, the repository may be empty.</red>'

    @staticmethod
    def confirm_init():
        return 'Add changeln configuration files to the project?'

    @staticmethod
    def success_init():
        return '<green>Configuration files added successfully.</green>'

    @staticmethod
    def success_save_changelog(path: str):
        return '<green>Changelog saved successfully:</green> {}'.format(path)

    @staticmethod
    def not_found_git_folder():
        return '<red>Changelog generation is not possible.</red> ".git" <red>directory not found.</red>'

    @staticmethod
    def not_found_template():
        return '<red>Template not found. Update the configuration file path template.</red>'

    @staticmethod
    def error_load_key(key: str):
        return '<red>Error reading configuration file. Check the</red> "{}" <red>parameter.</red>'.format(key)
