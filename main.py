import time
from config import (
    VM_LIST,
    VBOXMANAGE_PATH,
    SPLUNK_URL,
    PROGRAM_LIST
)

from vm_manager import check_and_start_vm

from app_launcher import (
    launch_program,
    open_url
)

from logger import write_log

from ui import(
    print_banner,
    print_ready
)

from network_checker import check_warp

check_warp()

print_banner()

start_time = time.time()

for vm in VM_LIST:
    status = check_and_start_vm(
        VBOXMANAGE_PATH,
        vm
    )
    write_log(f"{vm}: {status}")

for program in PROGRAM_LIST:
    launch_program(program)
    write_log(f"Started: {program}")


open_url(SPLUNK_URL)
write_log(f"Opened: {SPLUNK_URL}")

elapsed = time.time() - start_time

print_ready(elapsed)