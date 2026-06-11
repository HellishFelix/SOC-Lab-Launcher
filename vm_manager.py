import subprocess

def list_vms(vboxmanage_path):

    result = subprocess.run(
        [vboxmanage_path, "list", "vms"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

def start_vm(vboxmanage_path, vm_name):

    result = subprocess.run(
        [
            vboxmanage_path,
            "startvm",
            vm_name
        ],
        capture_output=True,
        text=True
    )
    print(result.stdout)

    if result.stderr:
        print(result.stderr)

def check_vm(vboxmanage_path, vm_name):

    result = subprocess.run(
        [
            vboxmanage_path,
            "showvminfo",
            vm_name
        ],
        capture_output=True,
        text=True
    )
    
    for line in result.stdout.splitlines():

        if line.startswith("State:"):

            state = line.split(":")[1].strip()

            return state
        
    return "unknown"


def check_and_start_vm(vboxmanage_path, vm_name):

    status = check_vm(
        vboxmanage_path,
        vm_name
    )
    if "powered off" in status:
        print(f"{vm_name} is powered off")
        print(f"Starting {vm_name}...")

        start_vm(
            vboxmanage_path,
            vm_name
        )
    else:
        print(f"{vm_name} is already running")
    return status