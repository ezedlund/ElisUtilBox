"""
-
-
-
-
-
-
- This is a file for testing various things
- Not for downloading or using
-
-
-
-
-
-
-
-
-
-
"""


import os
import subprocess
from time import sleep
import requests
import json
import random

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

# toggles
kill_spotify = False
kill_discord = True
kill_steam = False


def validate_options(options):
    """
    validate options
    """
    pass


def options_menu():
    """
    menu for changing some toggles
    """
    # menu loop
    while True:
        # menu setup
        menu_input = inquirer.checkbox(
            message=f"@EUB~# ",
            choices=[
                Choice("spotify", name="Kill Spotify", enabled=kill_spotify),
                Choice("discord", name="Kill Discord", enabled=kill_discord),
            ],
        ).execute()
        print(menu_input)


if __name__ == "__main__":
    options_menu()
