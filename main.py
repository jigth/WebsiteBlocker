import time
from datetime import datetime as dt

# host files
# Windows c:\\windows\system32\drivers\etc
# Mac & Linux /etc/hosts
host_path_windows = r"C:\Windows\System32\drivers\etc\hosts"
host_path_unix = "/etc/hosts"

hosts_dir = host_path_unix

redirect = "127.0.0.1"

webs_blacklist = [
    "www.facebook.com",
    "facebook.com",
    "fb.com",
    "mail.google.com",
    "animeflv.net"
]

from_hour = 7
to_hour = 16

while True:

    start_hour = dt(dt.now().year, dt.now().month, dt.now().day, from_hour)
    end_hour = dt(dt.now().year, dt.now().month, dt.now().day, to_hour)
    if( start_hour < dt.now() < end_hour):
        print("working")
        with  open(hosts_dir, 'r+') as file:
            content = file.read()
            for website in webs_blacklist:
                if website not in content:
                    file.write(redirect + ' ' + website + '\n')
    else:
        print("fun...")
        with open(hosts_dir, 'r+') as file:
            content = file.readlines()
            file.seek(0) # Beginning of the host file
            for line in content:
                # Write line if it doesn't contain a "blacklist" item
                if not any(website in line for website in webs_blacklist):
                #for website in webs_blacklist:
                #    if not any(website in line):
                    file.write(line)
                file.truncate()
    time.sleep(1)
