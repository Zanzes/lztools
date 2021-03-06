from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings

from main_layout import main_layout

kb = KeyBindings()

@kb.add('c-q')
def exit_(event):
    """
    Pressing Ctrl-Q will exit the user interface.
    Setting a return value means: quit the event loop that drives the user
    interface and return this value from the `Application.run()` call.
    """
    event.app.exit()

def run():
    app = Application(full_screen=True, mouse_support=True, key_bindings=kb, layout=main_layout)
    app.run()
