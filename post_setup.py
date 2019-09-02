import os

final_messages = []

def setup_openexchangerates():
    id = input("APP ID: ")
    os.system(f'export OERID={id}')
    os.system(f'echo "export OERID={id}" >> ~/.bashrc')
    final_messages.append("Please restart your bash session to load changes or run:")
    final_messages.append("\tsource ~/.bashrc")

def run():
    if input("Setup openexchangerates.org?").lower() in ['y', 'yes']:
        setup_openexchangerates()