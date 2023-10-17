import GPUtil

# Get list of available GPU devices.
gpus = GPUtil.getGPUs()

def get_gpu_info():

    for gpu in gpus:
        info = (
            f"GPU ID: {gpu.id}\n"
            f"GPU Name: {gpu.name}\n"
            f"Driver Version: {gpu.driver}\n"
            f"GPU Load: {gpu.load * 100:.1f}%\n"
            f"GPU Memory Free: {gpu.memoryFree}MB\n"
            f"GPU Memory Used: {gpu.memoryUsed}MB\n"
            f"GPU Memory Total: {gpu.memoryTotal}MB\n"
            f"GPU Memory Utilization: {gpu.memoryUtil * 100:.1f}%\n"
    #print(f"GPU Core Clock: {gpu.gpuClock}MHz")
    #print(f"GPU Memory Clock: {gpu.memoryClock}MHz")
        )
        return info