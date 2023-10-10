import psutil
import subprocess
import platform
hardware = platform.system()


# Number of logical and physical cores
print(f"Logical cores: {psutil.cpu_count(logical=True)}")
print(f"Physical cores: {psutil.cpu_count(logical=False)}")


# CPU frequencies (Windows / Linux)
def win_cpu_freq(): 
    cpu_freq = psutil.cpu_freq()
    cpu_times = psutil.cpu_times()
    info = (
        f"Current frequency: {cpu_freq.current}Mhz\n"
        f"Max Frequency: {cpu_freq.max}Mhz\n"
        f"Min Frequency: {cpu_freq.min}Mhz\n"
        # CPU percent usage
        f"CPU usage (per core): {psutil.cpu_percent(interval=1, percpu=True)}%\n"
        f"Total CPU usage: {psutil.cpu_percent(interval=1)}%\n"

        # CPU times
        
        f"User time: {cpu_times.user}s\n"
        f"System time: {cpu_times.system}s\n"
        f"Idle time: {cpu_times.idle}s\n"
    )
    return info

# CPU frequencies (Mac)
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