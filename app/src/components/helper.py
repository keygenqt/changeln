from pathlib import Path

from app.src.common.default_conf import gen_default_conf
from app.src.common.default_template import gen_default_template


def get_path_home():
    return Path.home()


def get_app_name():
    return 'changeln'


def get_app_version():
    return '0.0.1'


def get_path_conf(conf=None):
    if conf is not None:
        return conf
    else:
        return '{}/.{}.yaml'.format(get_path_home(), get_app_name())


def get_path_template(template=None):
    if template is not None:
        return template
    else:
        return '{}/.{}.template'.format(get_path_home(), get_app_name())


def get_default_conf():
    return gen_default_conf()


def get_default_template():
    return gen_default_template()
