import click
from prompt_toolkit import Application
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.key_binding import KeyBindings

commands = ["lztools", "¤"]
completer = WordCompleter(commands, ignore_case=True)
kb = KeyBindings()

@kb.add('c-q')
def exit_(event):
    """
    Pressing Ctrl-Q will exit the user interface.

    Setting a return value means: quit the event loop that drives the user
    interface and return this value from the `Application.run()` call.
    """
    event.app.exit()

@click.command()
def run():
    app = Application(full_screen=True, mouse_support=True, key_bindings=kb)
    app.run()

    # while True:
    #     prompt(u"$USER\n> ",
    #            mouse_support=True,
    #            history=FileHistory("history.txt"),
    #            auto_suggest=AutoSuggestFromHistory(),
    #            completer=completer)
