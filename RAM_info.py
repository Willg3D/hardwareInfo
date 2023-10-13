import psutil

# Get RAM information using psutil
virtual_memory = psutil.virtual_memory()
swap_memory = psutil.swap_memory()
def get_ram_info():
    raminfo = (
# Print the RAM information
        f"Total RAM: {virtual_memory.total / (1024**3):.2f} GB\n"
        f"Available RAM: {virtual_memory.available / (1024**3):.2f} GB\n"
        f"Used RAM: {virtual_memory.used / (1024**3):.2f} GB\n"
        f"RAM Percentage Used: {virtual_memory.percent}%\n\n"

# If you want to check swap memory details (if present):

        f"Swap Memory:\n"
        f"Total Swap: {swap_memory.total / (1024**3):.2f} GB\n"
        f"Used Swap: {swap_memory.used / (1024**3):.2f} GB\n"
        f"Free Swap: {swap_memory.free / (1024**3):.2f} GB\n"
        f"Swap Percentage Used: {swap_memory.percent}%\n"

            )
    return raminfo
    