import psutil
import subprocess
import platform
hardware = platform.system()


# Number of logical and physical cores
print(f"Logical cores: {psutil.cpu_count(logical=True)}")
print(f"Physical cores: {psutil.cpu_count(logical=False)}")


# CPU frequencies (Windows / Linux)
if hardware == "Windows" or hardware == "Linux":
    cpu_freq = psutil.cpu_freq()
    print(f"Current frequency: {cpu_freq.current}Mhz")
    print(f"Max frequency: {cpu_freq.max}Mhz")
    print(f"Min frequency: {cpu_freq.min}Mhz")

# CPU frequencies (Mac)
else:
    def get_cpu_freq():
        result = subprocess.check_output(["sysctl", "-n", "machdep.cpu.brand_string"]).decode('utf-8')
        return result.strip()

        print(f"CPU Info: {get_cpu_freq()}")

        # CPU percent usage
        print(f"CPU usage (per core): {psutil.cpu_percent(interval=1, percpu=True)}%")
        print(f"Total CPU usage: {psutil.cpu_percent(interval=1)}%")

        # CPU times
        cpu_times = psutil.cpu_times()
        print(f"User time: {cpu_times.user}s")
        print(f"System time: {cpu_times.system}s")
        print(f"Idle time: {cpu_times.idle}s")