import click

DEFAULT_CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

def proper_command():
    return click.command(context_settings=DEFAULT_CONTEXT_SETTINGS)

def proper_group():
    return click.group(context_settings=DEFAULT_CONTEXT_SETTINGS)