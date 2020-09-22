
#Note for running python script in backgournd and during device startup:
# 1) The extension of this python file is not .py but is pyw so that this file when double clicked will run in the background
# 2) Serach for task scheduler in windows search and schedule the .pyw file

# web site blocker: goal is to type the website in windows host file and redirect it to different ip for the duration(8 Am to 5 PM)
 # that we want it to be redirected (i.e. blocked)

import time
from datetime import datetime as dt

# since inside quotation we have \, python might interprete different meaning like \n = line break, hence we use r before starting quote
# which stands for raw i.e. we are passing a raw string or instead of that we could use \\ inside of \ for each occurences
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

while True:
    # example =  if dt(2020,9,14,8)<dt.now()<dt(2020,9,14,17) , this is true if the current time falls between 8AM and (17) i.e. 5PM for the current day
    # where dt.now() returns todays datetime
    # and also we can do datetime comparisions like this:  dt(2020,9,14,8)<dt(2020,9,14,17) returns true since 17>8 (time, 5PM>8AM)
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("Websites Blocked!")
        # now we know that the time is between 8AM and 5PM, we need to first check if the websitename is already in the host file,
        # if it is then we do nothing but if it is not there, we write the redirect ip and the name in the host file
        # r+ to both read and write in file
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                # if website(say facebook.com) is in content(all the lines in the file)
                if website in content:
                    # do nothing (similar to break in other lanugage)
                    pass
                else:
                    # we write 127.0.0.1 facebook.com in the host file if the websites were already not written in it
                    file.write("\n" + redirect + " " + website)
    # else means the time isn;t between 8AM and 5PM
    # first we need to check if the website blocking line exists, if it does we need to remove it
    # if the blocking line doesn't exist, then pass
    else:
        print("Websites Not Blocked!")
        with open(hosts_path,'r+') as file:
            # read() returns all the lines in a single string whereas readlines() returns each line as a string so 25 lines is stored in 25 strings
            content=file.readlines()
            # inside the for loop after this line of code, the file.write(line) actually rewrites all the existing lines of code
            # after the end of the existing contents
            # for example: if orginal hosts file contains 3 lines (say)
            # This is first line.(L1)
            # This is second line.(L2)
            # 127.0.0.1 www.facebook.com(L3)
            # then the file.write(line) rewrites it after the end of the last line (4th and 5th line) i.e. Case 1
            # This is first line.(L1)
            # This is second line.(L2)
            # 127.0.0.1 www.facebook.com(L3)
            # This is first line.(L4)
            # This is second line.(L5)
            # but we need to truncate the first 3 lines, to do that we use file(0) which shifts the pointer in the first line so that
            # file.write(line) execution makes the content like below: Case 2
            # This is first line.(L4)
            # This is second line.(L5)
            # This is first line.(L1)
            # This is second line.(L2)
            # 127.0.0.1 www.facebook.com(L3)
            # hence we can use truncate method to truncate the old contents (i.e. L1,L2 and L3) - truncate couln't have been used
            # to truncate L1,L2 and L3 if it were before L4 and L5 like in Case 1.
            file.seek(0)
            # for looping line by line
            for line in content:
                # like nested loop, loop1.1: if not any www.facebook.com in line1 for www.facebook.com in website_list
                #                   loop1.2: if not any facebook.com in line1 for facebook.com in website_list
                #                   loop2.1: if not any www.facebook.com in line2 for www.facebook.com in website_list
                #                   loop2.2: if not any facebook.com in line2 for facebook.com in website_list and so on
                if not any(website in line for website in website_list):
                    # if the line does not contain (say) www.facebook.com, then file.write(line) will rewrite the line,
                    # which means all the lines in the hosts file are written again (except for the lines containing the listed websites)
                    file.write(line)
            # removes everything after the pointer (i.e. truncates the original lines of code i.e. L1, L2 and L3 in Case 2 as mentioned above)
            file.truncate()

    # before again going back to the loop, keeping a delay of 5 sec i.e. the program executes every 5 sec (to check if the time is between 8AM & 5PM or not)
    time.sleep(5)
