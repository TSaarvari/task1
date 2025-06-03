import platform
import subprocess
import time
from datetime import datetime

def get_windows_uptime():
    try:
        result = subprocess.run(
            ["net", "stats", "srv"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8',
            check=True
        )
        for line in result.stdout.split('\n'):
            if "Statistics since" in line:
                boot_time_str = line.strip().split("since", 1)[1].strip()
                boot_time = datetime.strptime(boot_time_str, "%m/%d/%Y %I:%M:%S %p")
                uptime_seconds = (datetime.now() - boot_time).total_seconds()
                return uptime_seconds
    except Exception as e:
        print(f"Error retrieving uptime on Windows: {e}")
    return None

def get_unix_uptime():
    try:
        # Try reading /proc/uptime (Linux)
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
                return uptime_seconds
        except FileNotFoundError:
            # Fallback for macOS using sysctl
            result = subprocess.run(
                ['sysctl', '-n', 'kern.boottime'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding='utf-8',
                check=True
            )
            import re
            match = re.search(r'sec = (\d+),', result.stdout)
            if match:
                boot_time = int(match.group(1))
                uptime_seconds = time.time() - boot_time
                return uptime_seconds
    except Exception as e:
        print(f"Error retrieving uptime on Unix: {e}")
    return None

def print_system_uptime():
    uptime_seconds = None
    if platform.system() == "Windows":
        uptime_seconds = get_windows_uptime()
    else:
        uptime_seconds = get_unix_uptime()

    if uptime_seconds is not None:
        uptime_hours = int(uptime_seconds // 3600)
        uptime_minutes = int((uptime_seconds % 3600) // 60)
        uptime_secs = int(uptime_seconds % 60)
        print(f"System uptime: {uptime_hours} hours, {uptime_minutes} minutes, {uptime_secs} seconds")
    else:
        print("Unable to determine system uptime.")

if __name__ == "__main__":
    print_system_uptime()
