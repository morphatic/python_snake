"""
Utility functions that support the game
"""

from os import path
import sys

# SOURCE: https://stackoverflow.com/a/13790741/296725
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        base_path = path(sys._MEIPASS)
    else:
        base_path = path.abspath(".")
    return path.join(base_path, relative_path)
