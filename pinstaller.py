import os
import subprocess
from pathlib import Path

import nicegui

# Creates an executable in the /dist/ folder

cmd = [
    'python',
    '-m', 'PyInstaller',
    'randomizer.py',
    '--name', 'randomizer',
    '--onefile',
    '--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui'
]
subprocess.call(cmd)
