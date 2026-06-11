import subprocess
import os

from file_checker import file_exists


def launch_program(path):

    if file_exists(path):

        subprocess.Popen(path)

        program_name = os.path.basename(path)
        print(f"Started: {program_name}")

    else:
        print("Program not found")

def open_url(url):
    import webbrowser
    webbrowser.open(url)
    print(f"Opened: {url}")