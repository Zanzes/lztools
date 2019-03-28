from bash import command

import zlick

from text_tools.lztext import regex

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@zlick.group(context_settings=CONTEXT_SETTINGS)
def main():
    """lztools for git"""

@main.command(context_settings=CONTEXT_SETTINGS)
@zlick.option("-b", "--bash-format", is_flag=True, default=False)
def branch(bash_format):
    """Gets the active branch"""
    if not bash_format:
        for x in regex(r"\* (.*)", command("git", "branch", return_result=True)):
            print(x)
    else:
        git_branch = regex(r"\* (.*)", command("git", "branch", return_result=True), only_first=True, suppress=True)
        if git_branch is not None:
            print(f"({git_branch}) ")

