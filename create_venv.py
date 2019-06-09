"""
# create_venv.py
Creates a new virtual environment for SMARSLab
"""
import subprocess

print("Creating Python 3 Virtual Environment")
subprocess.call(["virtualenv", "-p", "python3", "venv"])
print("Environment created - To use the virtual environment, type:")
print("  source venv/bin/activate")
print("to activate the environment, and")
print("  deactivate")
print("to deactivate the environment.")
