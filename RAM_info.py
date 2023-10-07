import psutil

# Get RAM information using psutil
virtual_memory = psutil.virtual_memory()

# Print the RAM information
print(f"Total RAM: {virtual_memory.total / (1024**3):.2f} GB")
print(f"Available RAM: {virtual_memory.available / (1024**3):.2f} GB")
print(f"Used RAM: {virtual_memory.used / (1024**3):.2f} GB")
print(f"RAM Percentage Used: {virtual_memory.percent}%")
#print(f"Buffered RAM: {virtual_memory.buffers / (1024**3):.2f} GB")
#print(f"Cached RAM: {virtual_memory.cached / (1024**3):.2f} GB")
#print(f"Shared RAM: {virtual_memory.shared / (1024**3):.2f} GB")

# If you want to check swap memory details (if present):
swap_memory = psutil.swap_memory()
print("\nSwap Memory:")
print(f"Total Swap: {swap_memory.total / (1024**3):.2f} GB")
print(f"Used Swap: {swap_memory.used / (1024**3):.2f} GB")
print(f"Free Swap: {swap_memory.free / (1024**3):.2f} GB")
print(f"Swap Percentage Used: {swap_memory.percent}%")
