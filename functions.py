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

# Import Classes
import sys
import os
import datetime

# Constant
DAYSOFTHEWEEK = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def read(name):
    try:
        with open(resource_path(name), "r") as schedulefile:
            return list(map(lambda line: line.strip(), schedulefile.readlines()))
    except FileNotFoundError:
        sys.exit()

def string_to_time(timeString):
    try:
        return datetime.time(int(timeString[0:2]), int(timeString[3:]))
    except ValueError:
        return int(timeString)

def datetime_to_time(dtime):
    return datetime.time(dtime.time().hour, dtime().time().minute)

def time_to_datetime(ctime, time):
    return datetime.datetime.combine(ctime, time)

def get_schedule_for_today(day, schedule):
    if DAYSOFTHEWEEK[day % 7] == "Saturday":
        sched = schedule[schedule.index(DAYSOFTHEWEEK[day % 7]) + 1:]
    else:
        sched = schedule[schedule.index(DAYSOFTHEWEEK[day % 7]) + 1:schedule.index(DAYSOFTHEWEEK[(day + 1) % 7])]
    for periodIndex in range(len(sched)):
        sched[periodIndex] = list(map(lambda item: string_to_time(item), sched[periodIndex].split()))
    return sched
