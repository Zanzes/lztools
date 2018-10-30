import inspect
from types import FunctionType

import click
from click import Context

DEFAULT_CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'], max_content_width=click.get_terminal_size()[0])
# groups = dict()

# def proper_command():
#     lvars = inspect.currentframe().f_back.f_locals
#     name = lvars["__name__"]
#     return lvars[groups[name]].command(context_settings=DEFAULT_CONTEXT_SETTINGS)
#
# def proper_group():
#     f = inspect.currentframe().f_back
#     name = f.f_locals["__name__"]
#     filename = inspect.getfile(f)
#     code_line = open(filename).readlines()[f.f_lineno]
#     groupname = code_line.strip()[4:-3]
#     groups[name] = groupname
#     return click.group(name=groupname, context_settings=DEFAULT_CONTEXT_SETTINGS)

class MatchNameGroup(click.Group):

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

def group(name=None, cls=click.Group):
    return click.group(name=name, context_settings=DEFAULT_CONTEXT_SETTINGS, cls=cls)

def alias_group(name=None):
    return click.group(name=name, context_settings=DEFAULT_CONTEXT_SETTINGS, cls=MatchNameGroup)

def command(name=None):
    return click.command(name=name, context_settings=DEFAULT_CONTEXT_SETTINGS)

def create_alias(alias, targer:FunctionType, group=None):
    cmd = click
    if group:
        cmd = group
    getattr()
    return exec(f"""@cmd.command(context_settings=DEFAULT_CONTEXT_SETTINGS)
    @click.pass_context
    def {alias}(ctx:Context, *args, **kwargs):
        ctx.forward(get_at)""")
