import click
from yaml import Loader
from yaml import load

from app.src.components.helper import *

CONF_PROJECTS = 'projects'
CONF_GROUPS = 'groups'


class Config:

    @staticmethod
    def init_conf(conf=None):
        path = Path(get_path_conf(conf))
        if not path.is_file():
            type_conf = ('default', 'custom')[conf is not None]
            click.echo(click.style("\nAdded {} config. {}\nPlease configure the application.\n".format(type_conf, path), fg="yellow"))
            with open(path, 'w') as file:
                print(get_default_conf(), file=file)
        return path

    @staticmethod
    def init_template(template=None):
        path = Path(get_path_template(template))
        if not path.is_file():
            type_template = ('default', 'custom')[template is not None]
            click.echo(click.style("\nAdded {} template. {}".format(type_template, path), fg="yellow"))
            with open(path, 'w') as file:
                print(get_default_template(), file=file)
        return path

    def __init__(self, test, conf, template):
        self.test = test
        self.path_template = Config.init_template(template)
        self.path_conf = Config.init_conf(conf)
        with open(self.path_template, 'r') as file:
            self.template = file.read()
        with open(self.path_conf, 'rb') as file:
            self.conf = load(file.read(), Loader=Loader)

    def get(self, name):
        if name == CONF_PROJECTS:
            if name in self.conf:
                return self.conf[name]
            else:
                return []

        if name == CONF_GROUPS:
            if name in self.conf:
                return self.conf[name]
            else:
                return {}
