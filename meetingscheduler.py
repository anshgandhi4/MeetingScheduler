#  Copyright © 2020 Ansh Gandhi
#
#  This file is part of Meeting Scheduler.
#
#  Meeting Scheduler is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Meeting Scheduler is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Meeting Scheduler.  If not, see <https://www.gnu.org/licenses/>.
#  Original Author: Ansh Gandhi
#  Original Source Code: <https://github.com/anshgandhi4/MeetingScheduler/>
#
#  EVERYTHING ABOVE THIS LINE MUST BE KEPT AS IS UNDER GNU GPL LICENSE RULES.

# Import Classes
import webbrowser
import datetime
import time as sleeptime
import sys
import os

# Open File
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

linksfile = open(resource_path("links.txt"), "r")
links = list(map(lambda line:line.strip(), linksfile.readlines()))
linksfile.close()

# Generate Link Variables
PERIOD1 = links[0]
PERIOD2 = links[1]
PERIOD3 = links[2]
PERIOD4 = links[3]
PERIOD5 = links[4]
PERIOD6 = links[5]
BUFFERTIME = int(links[6])
VERSION = 1.0

print("Meeting Scheduler Version " + str(VERSION))
while True:
    # Get Time Information
    ctime = datetime.datetime.now()
    day = ctime.isoweekday()
    currenttime = datetime.datetime.now()
    if currenttime.time() > datetime.time(14, 30):
        print("No More School Today!")
        break
    buffertime = str(currenttime + datetime.timedelta(minutes = BUFFERTIME))[11:16]
    print(str(currenttime)[11:16])

    # Get Link
    link = ""
    if day == 1:
        if buffertime == "08:00":
            print("Opening Period 1 Meeting Link")
            link = PERIOD1
        elif buffertime == "08:50":
            print("Opening Period 2 Meeting Link")
            link = PERIOD2
        elif buffertime == "10:45":
            print("Opening Period 3 Meeting Link")
            link = PERIOD3
        elif buffertime == "11:35":
            print("Opening Period 4 Meeting Link")
            link = PERIOD4
        elif buffertime == "12:55":
            print("Opening Period 5 Meeting Link")
            link = PERIOD5
        elif buffertime == "13:45":
            print("Opening Period 6 Meeting Link")
            link = PERIOD6
    elif day == 2 or day == 4:
        if buffertime == "08:00":
            print("Opening Period 1 Meeting Link")
            link = PERIOD1
        elif buffertime == "10:45":
            print("Opening Period 3 Meeting Link")
            link = PERIOD3
        elif buffertime == "12:55":
            print("Opening Period 5 Meeting Link")
            link = PERIOD5
    elif day == 3 or day == 5:
        if buffertime == "08:00":
            print("Opening Period 2 Meeting Link")
            link = PERIOD2
        elif buffertime == "10:45":
            print("Opening Period 4 Meeting Link")
            link = PERIOD4
        elif buffertime == "12:55":
            print("Opening Period 6 Meeting Link")
            link = PERIOD6

    # Open Link
    if link != "":
        webbrowser.open_new_tab(link)

    # Loop Every Minute
    sleeptime.sleep(60)