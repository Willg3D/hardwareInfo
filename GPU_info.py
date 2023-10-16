import GPUtil

# Get list of available GPU devices.
gpus = GPUtil.getGPUs()

for gpu in gpus:
    print(f"GPU ID: {gpu.id}")
    print(f"GPU Name: {gpu.name}")
    print(f"Driver Version: {gpu.driver}")
    print(f"GPU Load: {gpu.load * 100:.1f}%")
    print(f"GPU Memory Free: {gpu.memoryFree}MB")
    print(f"GPU Memory Used: {gpu.memoryUsed}MB")
    print(f"GPU Memory Total: {gpu.memoryTotal}MB")
    print(f"GPU Memory Utilization: {gpu.memoryUtil * 100:.1f}%")
    #print(f"GPU Core Clock: {gpu.gpuClock}MHz")
    #print(f"GPU Memory Clock: {gpu.memoryClock}MHz")
    print("----------------------------------------------------")