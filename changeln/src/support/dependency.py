import os
import subprocess
from pathlib import Path

from changeln.src.support.output import echo_stderr
from changeln.src.support.texts import AppTexts


# Check dependency for init
def check_dependency_init():
    # Check git application
    try:
        subprocess.run(['git', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except (Exception,):
        echo_stderr(AppTexts.error_dependency_git())
        exit(1)

    # Check folder has .git
    git_folder = Path(os.getcwd()) / '.git'
    if not git_folder.is_dir():
        echo_stderr(AppTexts.not_found_git_folder())
        exit(1)
