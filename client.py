#client

import server
import os

#clearing screen
os.system("clear")

search = input("[search lyrics] --> ")

#ur search result
print(server.search_algo(search))

#clearing screen
print("")
clear_screen = input("|press 'Enter' to quit & clear screen|\n|\n|--$ ")
if clear_screen == "":
    os.system("clear")
else:
    os.system("clear")