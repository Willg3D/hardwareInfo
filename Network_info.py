import subprocess 
import psutil
from pprint import pprint


# using the check_output() for having the network term retrieval 
devices = subprocess.check_output(['netsh','wlan','show','network']) 
  
# decode it to strings 
devices = devices.decode('ascii') 
devices= devices.replace("\r","") 

nets = psutil.net_if_stats()
ipInfo = pprint(nets)

# displaying the information 

def get_net_info():
    netInfo = (
        f"{devices}\n"
        f"{ipInfo}\n"
    )
    return netInfo

