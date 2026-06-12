import subprocess
import time

def check_warp():
    try:
        result = subprocess.run(
            ["warp-cli", "status"],
            capture_output=True,
            text=True
        )

        output = result.stdout.lower()

        if "status update: connected" in output:
            print("\n[WARNING] Cloudflare WARP is enabled!")
            print("[WARNING] Splunk may not work correctly.")
            print("[WARNING] Disable WARP and launch SOC Lab again.\n")

            print("Closing in 5 seconds...")
            time.sleep(5)

            exit()
    except FileNotFoundError:
        pass