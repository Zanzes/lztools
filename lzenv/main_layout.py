from prompt_toolkit.layout import FormattedTextControl
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.widgets import TextArea, SystemToolbar

def accept(buffer):
    out = input_field.text
    testx.text += f"\n{out}"
    # output_field.buffer.text += f"\n{out}"

# buffer1 = Buffer()
input_field = TextArea(height=1, prompt=f'> ', style='class:input-field', multiline=False, wrap_lines=False, accept_handler=accept)
output_field = TextArea(style='class:output-field', dont_extend_height=True,)
toolbar = SystemToolbar()

testx = FormattedTextControl('Press "q" to quit.')
root_container = HSplit([
    # One window that holds the BufferControl with the default buffer on
    # the left.

    # Window(content=BufferControl(buffer=buffer1)),
    # A vertical line in the middle. We explicitly specify the width, to
    # make sure that the layout engine will not try to divide the whole
    # width by three for all these windows. The window will simply fill its
    # content by repeating this character.
    Window(testx, allow_scroll_beyond_bottom=True,),
    Window(height=1, char='-', style='class:line'),
    toolbar,
    input_field,
])

# Window(width=1, char='|', style='class:line'),

main_layout = Layout(root_container, focused_element=input_field)