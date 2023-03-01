# -*- coding: utf-8 -*-

name = u'TBM_hook'

version = '1.0.0'

description = u''

authors = [u'Christophe PETIT']

tools = []

requires = []

build_requires = ['python-2']

timestamp = 1677664384

format_version = 2

build_command = "python {root}/build.py {install}"

_data = {
    "icon": "{root}\\resources\\TBM_icon.png",
    "files": {
        "VSCode": {
            "code": ["{root}\\workspaces\\TBM_hook.code-workspace"]
        }
    }
}

_environ = {
    "MAYA_PLUG_IN_PATH": [
        "{root}\\"+name+"\\plug-ins"
    ],
    "XBMLANGPATH": [
        "{root}\\"+name+"\\icons"
    ]
}

build_command = 'python {root}\\build.py {install}'

def commands():
    global env
    global this
    global expandvars
    global _environ

    _environ = this._environ
    for key, value in _environ.items():
        if isinstance(value, (tuple, list)):
            [env[key].append(expandvars(v)) for v in value]
        else:
            env[key] = expandvars(value)
