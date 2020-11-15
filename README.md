# Meeting Scheduler
This is the official repository for a school meeting scheduler. It automatically opens meeting links for classes so that you don't have to worry about forgetting a class or entering the wrong class. This scheduler can follow the bell schedule of any school that you attend.

This repository is licensed under the GNU General Purpose License. A copy of the license is provided in this project under the name COPYING.txt. Please visit https://www.gnu.org/licenses/ for license details.

## DISCLAIMER:
By running, copying, distributing, and/or modifying any part of this repository, you agree that you are fully responsible for all of the consequences arising from your use or inability to use this program. You are in full control of which websites this meeting scheduler will visit.

## How to Use This Code
### Download/Setup
**The first step is to download the official source code.**
 1. Go to the [Meeting Scheduler GitHub release page](https://github.com/anshgandhi4/MeetingScheduler/releases/tag/v2.1).
 2. Click on "SourceCode.zip".
 3. Unzip the folder.
 
**The second step is to set up a "links.txt" file.**

 1. Open "links.txt".
 2. In the first line, write the meeting link for your zero period class.
 3. In the second line, write the meeting link for your first period class.
 4. Repeat this for all of your classes.
 5. If you don't have a class during a certain period, or don't want this scheduler to open a meeting for a specific class period, just leave the corresponding line in the file blank.
 6. For the last line of the file, put in the number of minutes early you want to attend your classes. For example, if you want to open all of your class 2 minutes before they actually start, put 2 as the seventh line. Make sure that the number you enter is a whole number.
 7. An example file (example.txt) is provided. In this file, there is no zero period class, but there are links for periods 1-6.

**The third step is to set up a "schoolschedule.txt" file.**

 1. Open "schoolschedule.txt".
 2. In the first line, write the name of your school.
 3. Write all of the days of the week in separate lines.
 4. Underneath each day of the week, write the period numbers of all of the classes you will have that day in separate lines.
 5. To the right of each period number, put a space, followed by the start time, followed by another space, followed by the end time. Note that the time needs to be in the 24-hour format and not the 12-hour format. For example, 8:15 am should be written as 08:15 and 2:30 pm should be written as 14:30.
 6. Example files for different schools have been provided in the "schoolschedules" folder. If the data for your school is in that folder, feel free to copy-paste that data into the "schoolschedule.txt" file.

### Using the Code
Once you update links.txt, there are two ways to use this code.

If you would like to use this code as is, simply run meetingscheduler.exe. It will open a window with the time and a progress bar. The time will tick every minute (so you know its still working) and the progress bar will slowly grow longer as your class progresses. If you would like to stop the program, just close the window.

**Note: You can only run the .exe file on Windows because the file type isn't supported on MacOS or Linux based operating systems.**

If you would like to use this code to modify it to your own needs, follow the steps below.
 1. You will need to some version of Python 3 installed on your computer.
 2. The source code will be ready for you to modify and run. The main file is meetingscheduler.py. No package installs are necessary.
 3. Make sure to follow GNU GPL license rules regarding the legal restrictions of copying, distribution, modification, etc. of this code.

## Troubleshooting
### Failed to execute script meetingscheduler
Your "links.txt" file and/or "schoolschedule.txt" file isn't formatted correctly. Please look at "example.txt" and the text files in the "schoolschedules" folder to get an idea of what you need to do.

### A window briefly opens and then closes.
You don't have anything scheduled for the day, so the program just terminates.

## Changelog
### Current Features
Meeting Scheduler Features include:
 - Automatically opens meeting links for different classes
 - Opens meetings links in your default browser
 - Works with any school/bell schedule
 - Automatically terminates after school is over for the day
 - Small GUI window with help menu
 - Progress bar lets you know how much of the period is over
 - Custom icon
### Version 2.1 (08/31/20)
 - Bug fixes
 - Typo fixes
### Version 2.0 (08/31/20)
 - Created GUI
 - Added multiple school/bell schedule support
 - Bug fixes
### Version 1.0 (08/27/20)
 - Initial release
