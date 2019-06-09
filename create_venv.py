"""
# create_venv.py
Creates a new virtual environment for SMARSLab
"""
import subprocess

print("Creating Python 3 Virtual Environment")
subprocess.call(["virtualenv", "-python3", "venv"])
