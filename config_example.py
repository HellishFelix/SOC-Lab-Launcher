# ==========================
# Virtual Machines
# ==========================

# Windows VM name in VirtualBox
WINDOWS_VM_NAME = "Windows 10"

# Kali Linux VM name in VirtualBox
KALI_VM_NAME = "kali"

VM_LIST = [
    WINDOWS_VM_NAME,
    KALI_VM_NAME
]


# ==========================
# Applications
# ==========================

# Path to Obsidian executable
OBSIDIAN_PATH = r"PATH_TO_OBSIDIAN"

# Path to Google Chrome executable
CHROME_PATH = r"PATH_TO_CHROME"

PROGRAM_LIST = [
    OBSIDIAN_PATH,
    CHROME_PATH
]


# ==========================
# Splunk
# ==========================

# Splunk Web URL
SPLUNK_URL = "http://localhost:8000"


# ==========================
# VirtualBox
# ==========================

# Path to VBoxManage.exe
VBOXMANAGE_PATH = r"PATH_TO_VBOXMANAGE"


# ==========================
# Voice Activation
# ==========================

# Wake phrase words
# All words must be recognized to trigger the launcher
WAKE_WORDS = [
    "просыпайся",
    "папочка",
    "вернулся"
]

# Microphone ID
# Run list_microphones.py to find available devices
# Set to None to use the system default microphone
MICROPHONE_ID = None