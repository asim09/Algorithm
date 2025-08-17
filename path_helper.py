# path_helper.py
import sys
import os
import pathlib

def add_project_root_to_path():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(project_root)
    sys.path.append(str(pathlib.Path(__file__).parent.parent))
