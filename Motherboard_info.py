import os
import platform
import subprocess

def get_motherboard_info():
    try:
        system_platform = platform.system()

        if system_platform == "Windows":
            # For Windows, we can use wmic
            result = subprocess.check_output(['wmic', 'baseboard', 'get', 'product,manufacturer,version,serialnumber']).decode('utf-8').strip().split("\n")
            return "\n".join(result[1:])

        elif system_platform == "Linux":
            # For Linux, dmidecode is quite helpful (might need sudo privileges)
            result = subprocess.check_output(['dmidecode', '-t', '2']).decode('utf-8').strip().split("\n")
            return "\n".join([line.strip() for line in result if "Base Board" in line or "Manufacturer" in line or "Product" in line or "Version" in line])

        elif system_platform == "Darwin":
            # macOS doesn't provide a straightforward tool, but system_profiler can provide some related info
            result = subprocess.check_output(['system_profiler', 'SPHardwareDataType']).decode('utf-8').strip().split("\n")
            return "\n".join([line for line in result if "Model Name" in line or "Model Identifier" in line])

        else:
            return "Unsupported platform"

    except Exception as e:
        return str(e)