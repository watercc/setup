#!/usr/bin/env python3
"""Apply the improved .bashrc by copying .bashrc.new -> .bashrc.
Run this script from the repo root: python3 write_bashrc.py
"""
import os
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(script_dir, '.bashrc.new')
dst = os.path.join(script_dir, '.bashrc')
shutil.copy2(src, dst)
print(f"Updated {dst}")
