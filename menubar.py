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

class MenuBar:
    def __init__(self, master, menubar, scheduler):
        self.master = master
        self.menubar = menubar
        self.scheduler = scheduler

        helpmenu = Menu(self.menubar, tearoff = 0)
        helpmenu.add_command(label = "About", command = self.about)
        self.menubar.add_cascade(label = "Help", menu = helpmenu)

    def about(self):
        messagebox.showinfo("Meeting Scheduler Version " + str(self.scheduler.VERSION), "This simulator was made by Ansh Gandhi.\nFor more information, visit bit.ly/MeetingSchedulerAG.", parent = self.master)