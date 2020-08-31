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
#
#  Original Author: Ansh Gandhi
#  Original Source Code: <https://github.com/anshgandhi4/MeetingScheduler/>
#
#  EVERYTHING ABOVE THIS LINE MUST BE KEPT AS IS UNDER GNU GPL LICENSE RULES.

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
import datetime
import time as sleeptime
import webbrowser
from functions import *
from menubar import MenuBar

class Scheduler(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg = "white")
        self.grid()

        # Declaring Attributes
        self.VERSION = 2.0
        self.ctime = None
        self.day = None
        self.links = None
        self.schedule = None
        self.buffer = None
        self.buffertime = None
        self.sched = None

        # GUI Elements
        self.time = Label(self, bg = "white", font = ("Arial", 24), text = "00:00")
        self.time.grid(row = 0, column = 0)

        self.progress = Progressbar(self, orient = HORIZONTAL, length = 250, mode = "determinate")
        self.progress.grid(row = 1, column = 0, padx = (20, 20))

        self.message = Label(self, bg = "white", font = ("Arial", 14), text = "")
        self.message.grid(row = 2, column = 0)

        # Run Functions
        self.init()
        self.timer()

    def init(self):
        # Take Link and Schedule Data
        self.links = read("links.txt")
        self.schedule = read("schoolschedule.txt")

        # Get Buffer Time
        try:
            self.buffer = int(self.links[-1])
        except:
            sys.exit()

        # Get Time Information
        self.ctime = datetime.datetime.now()
        self.day = self.ctime.isoweekday()
        self.sched = get_schedule_for_today(self.day, self.schedule)

    def timer(self):
        # Update Time Information, Recalculate Schedule if Needed
        self.ctime = datetime.datetime.now()
        if self.ctime.isoweekday() != self.day:
            self.day = self.ctime.isoweekday()
            self.sched = get_schedule_for_today(self.day, self.schedule)
        self.buffertime = self.ctime + datetime.timedelta(minutes = self.buffer)

        # Exit if School is Over
        try:
            if len(self.sched) == 0 or datetime.timedelta(seconds = 0) <= self.ctime - time_to_datetime(self.ctime, self.sched[-1][2]) <= datetime.timedelta(seconds = 60):
                sys.exit()
        except:
            sys.exit()

        # Get Starting Period Number
        link = None
        currentperiodindex = None
        currentperiod = None
        for period in self.sched:
            if self.buffertime.time() > period[1]:
                timewindow = self.buffertime - time_to_datetime(self.ctime, period[1])
            else:
                timewindow = datetime.timedelta(seconds = 0)
            if datetime.timedelta(seconds = 0) < timewindow:
                currentperiodindex = self.sched.index(period)
                currentperiod = self.sched[currentperiodindex][0]
                if timewindow <= datetime.timedelta(seconds = 60):
                    try:
                        link = self.links[currentperiod]
                    except:
                        sys.exit()
                    break

        # Open Meeting Link and Update Progress Bar
        if link is not None:
            self.message["text"] = "Opening Link for Period " + str(currentperiod)
            webbrowser.open_new_tab(link)
        elif currentperiodindex is not None:
            curdiff = self.ctime - time_to_datetime(self.ctime, self.sched[currentperiodindex][1])
            fulldiff = time_to_datetime(self.ctime,self.sched[currentperiodindex][2]) - time_to_datetime(self.ctime, self.sched[currentperiodindex][1])
            self.progress["value"] = curdiff / fulldiff * 100
        else:
            self.progress["value"] = 0

        # Update Output and Sleep
        self.time["text"] = str(self.ctime)[11:16]
        root.after(60000, self.timer)

# Run Simulator
root = Tk()
root.title("Meeting Scheduler")
try:
    root.iconbitmap(resource_path("meetingschedulericon.ico"))
except:
    pass
scheduler = Scheduler(root)
menu = Menu(root)
menubar = MenuBar(root, menu, scheduler)
root.configure(menu = menu, background = "white")
scheduler.mainloop()
