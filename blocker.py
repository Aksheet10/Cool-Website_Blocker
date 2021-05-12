import time
frome datetime import datetime as dt
hosts_path - r"/etc/hosts" #the r is used for our raw string btw
hosts_temp = "hosts"
redirect = "127.0.0.1"
web_sites_lists = ["pornhub.com", "xvideos.com"]
# i made this to help people, but you can edit this and put any site's you would like

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt.now().year, dt.now().month, dt.now().day,22):
        print("No dude you can't do this")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in web_sites_lists:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")<<<<<<< patch-1                    if:=======                    else:>>>>>>> main
                        print("Time to do something good :D")
                        with open(hosts_path, "r+") as file:
                            content - file.readlines()
                            file.seek(0) 
                            for line in content:
                                #it took me a while to learn this part 
                                if not any(website in line for website in web_sites_list):
                                    file.write(line)
                                    file.truncate() #this is delete lines (mainly dns)
                                    time.sleep(5)
                                    
                                    
                                   #and that's the end!
