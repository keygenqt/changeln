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
import os
from enum import Enum
from pathlib import Path

import click.exceptions
from yaml import Loader
from yaml import load

from changeln.src.support.data.config import CHANGELOG_CONF
from changeln.src.support.data.template import CHANGELOG_TEMPLATE
from changeln.src.support.helper import get_path_file
from changeln.src.support.output import echo_stdout, echo_stderr
from changeln.src.support.texts import AppTexts

# Data versions
APP_NAME = 'changeln'
APP_VERSION = '2.0.0'

# Default path config
PATH_CONF = './.changeln/changeln.yaml'
PATH_MAKO = './.changeln/changeln.mako'


# Verbose output types
class OutType(Enum):
    markdown = 'markdown'
    html = 'html'
    pdf = 'pdf'

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)


# Loader configuration yaml
class Conf:

    @staticmethod
    def get_app_name() -> str:
        return APP_NAME

    @staticmethod
    def get_app_version() -> str:
        return APP_VERSION

    @staticmethod
    def _get_path_conf(path, default):
        path = get_path_file(path)

        default = get_path_file(default, none=False)

        if path and str(path).lower().endswith('.yaml'):
            return path
        else:
            if not default.is_file():
                Conf._create_default_config(default)
            return Path(default)

    @staticmethod
    def _create_default_config(path):
        if not click.confirm(AppTexts.confirm_init()):
            exit(0)

        path_dir = os.path.dirname(path)

        # Create dir if not exist
        if not os.path.isdir(path_dir):
            Path(path_dir).mkdir()

        # Write default configuration file
        with open(path, 'w') as file:
            print(CHANGELOG_CONF, file=file)

        # Check and write default template file
        path_mako = get_path_file(PATH_MAKO, none=False)
        if not Path(path_mako).is_file():
            with open(path_mako, 'w') as file:
                print(CHANGELOG_TEMPLATE, file=file)

        echo_stdout(AppTexts.success_init(), 2)

    def __init__(self, path):
        # Get path config
        self.conf_path = Conf._get_path_conf(path, default=PATH_CONF)

        # Load config
        with open(self.conf_path, 'rb') as file:
            self.conf = load(file.read(), Loader=Loader)

    # Get config path
    def get_path_out(self) -> Path:
        path = Path(os.path.dirname(self.conf_path))
        if path.name == '.changeln':
            return Path(os.path.dirname(path))
        else:
            return path

    # Get template
    def get_template(self) -> str:
        if 'template' not in self.conf.keys():
            echo_stderr(AppTexts.error_load_key('template'))
            exit(1)
        else:
            if not isinstance(self.conf['template'], str):
                echo_stderr(AppTexts.error_load_key('template'))
                exit(1)
            path = get_path_file(self.conf['template'], none=False, starting=os.path.dirname(self.conf_path))
            if not path.is_file():
                echo_stderr(AppTexts.not_found_template())
                exit(1)
            return open(path, 'r').read()

    # Get parse key
    def get_parse(self) -> str:
        if 'parse' not in self.conf.keys():
            echo_stderr(AppTexts.error_load_key('parse'))
            exit(1)
        else:
            if not isinstance(self.conf['parse'], str):
                echo_stderr(AppTexts.error_load_key('parse'))
                exit(1)
            return self.conf['parse']

    # Get parse key
    def get_filter(self) -> str:
        if 'filter' not in self.conf.keys():
            echo_stderr(AppTexts.error_load_key('filter'))
            exit(1)
        else:
            if not isinstance(self.conf['filter'], str):
                echo_stderr(AppTexts.error_load_key('filter'))
                exit(1)
            return self.conf['filter']

    # Get parse key
    def get_commits(self) -> str:
        if 'commits' not in self.conf.keys():
            echo_stderr(AppTexts.error_load_key('commits'))
            exit(1)
        else:
            if not isinstance(self.conf['commits'], dict):
                echo_stderr(AppTexts.error_load_key('commits'))
                exit(1)
            return self.conf['commits']
