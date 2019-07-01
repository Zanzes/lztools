from __future__ import annotations

from pathlib import Path

import click
from lztools import io

DEFAULT_CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'], max_content_width=click.get_terminal_size()[0])

class ExtraSettings(object):
    _global:ExtraSettings = None

    verbose:bool = False
    working_dir:Path = io.get_current_path()

    @classmethod
    def create(cls):
        return ExtraSettings()

    @classmethod
    def set_global(cls, settings:ExtraSettings):
        cls._global = settings

    @classmethod
    def set_specific_global(cls, **kwargs):
        if not cls._global:
            cls._global = ExtraSettings()
        for k in kwargs:
            cls.__dict__[k] = kwargs[k]

    @classmethod
    def get_global(cls):
        return cls._global

class CommandMatchingGroup(click.Group):

    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx)
                   if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail('Too many matches: %s' % ', '.join(sorted(matches)))

def command_matching_group(name=None):
    return click.group(name=name, context_settings=DEFAULT_CONTEXT_SETTINGS, cls=CommandMatchingGroup)

def parse_args(kwargs):
    tmp_set = DEFAULT_CONTEXT_SETTINGS.copy()
    if "context_settings" in kwargs:
        for key in kwargs["context_settings"]:
            tmp_set[key] = kwargs["context_settings"][key]
        del kwargs["context_settings"]
    return tmp_set, kwargs

def group(**kwargs):
    ctxt, kwargs = parse_args(kwargs)
    return click.group(context_settings=ctxt, **kwargs)

def command(**kwargs):
    ctxt, kwargs = parse_args(kwargs)
    return click.command(context_settings=ctxt, **kwargs)