import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes":["tkinter"], 'include_files': ['config.py']}

base = None
if sys.platform == 'win32':
    base = 'win32GUI'

executables = [
    Executable('gui.py', 
               base=base, 
               target_name = 'Fracionamento',
               icon="icon.ico")
]

setup(
    name = 'Fracionamento',
    version = '1.0',
    description = 'Gera Etiqueta de Fracionamento',
    options = {'build_exe': build_exe_options},
    executables = executables
)