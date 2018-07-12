import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """A collection of python tools and bash commands by laz aka nea"""

@main.command(context_settings=CONTEXT_SETTINGS)
@click.option("-c", "--count")
def picture(count):
    """Get or generate images"""
    if data_type == 'picture':
        print("pic {}".format(data_type))
    elif data_type == 'text':
        print("text {}".format(data_type))
    else:
        print("Invalid argument (--data-type = {})".format(data_type))

@main.command(context_settings=CONTEXT_SETTINGS)
def text():
    """Get or generate text"""





# @main.command(context_settings=CONTEXT_SETTINGS)
# @click.option('--data-type', type=click.Choice(['picture', 'text']), default='picture', help="The data type to work with")
# def data(data_type):
#     """Get or generate data"""
#     if data_type == 'picture':
#         print("pic {}".format(data_type))
#     elif data_type == 'text':
#         print("text {}".format(data_type))
#     else:
#         print("Invalid argument (--data-type = {})".format(data_type))