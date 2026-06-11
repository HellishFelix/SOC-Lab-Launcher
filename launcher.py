from config import NOTEPAD_PATH
from logger import write_log
from app_launcher import launch_program

def start_lab():

    print("Starting SOC Lab")
    write_log("Starting SOC Lab")

    launch_program(NOTEPAD_PATH)

    print("SOC Lab Ready")
    write_log("SOC Lab Ready")