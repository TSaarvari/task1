import os
import platform
import time

def get_uptime():
    if platform.system() == "Windows":
        # On Windows, use uptime from 'net stats srv'
        try:
            import subprocess
            output = subprocess.check_output("net stats srv", shell=True, encoding='utf-8')
            for line in output.split('\n'):
                if "Statistics since" in line:
                    from datetime import datetime
                    boot_time_str = line.strip().split("since", 1)[1].strip()
                    boot_time = datetime.strptime(boot_time_str, "%m/%d/%Y %I:%M:%S %p")
                    uptime_seconds = (datetime.now() - boot_time).total_seconds()
                    return uptime_seconds
        except Exception:
            pass
        return None
    else:
        # On Unix-like systems
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
                return uptime_seconds
        except FileNotFoundError:
            # Fallback for macOS and others
            try:
                import subprocess
                output = subprocess.check_output(['sysctl', '-n', 'kern.boottime'], encoding='utf-8')
                import re
                match = re.search(r'sec = (\d+),', output)
                if match:
                    boot_time = int(match.group(1))
                    uptime_seconds = time.time() - boot_time
                    return uptime_seconds
            except Exception:
                pass
        return None

def print_system_uptime():
    uptime_seconds = get_uptime()
    if uptime_seconds is not None:
        uptime_hours = uptime_seconds // 3600
        uptime_minutes = (uptime_seconds % 3600) // 60
        uptime_seconds = int(uptime_seconds % 60)
        print(f"System uptime: {int(uptime_hours)} hours, {int(uptime_minutes)} minutes, {uptime_seconds} seconds")
    else:
        print("Unable to determine system uptime.")

if __name__ == "__main__":
    print_system_uptime()
