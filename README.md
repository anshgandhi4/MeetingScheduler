# Meeting Scheduler
This is the official code for a school meeting scheduler. It automatically opens meeting links for classes so that you don't have to worry about forgetting a class or entering the wrong class. This scheduler follows the [Mission San Jose High School Bell Schedule](http://mission-fusd-ca.schoolloop.com/file/1500711509070/1500711507309/9033068015616581745.pdf).

This code is licensed under the GNU General Purpose License. A copy of the license is provided in this project under the name COPYING.txt. Please visit https://www.gnu.org/licenses/ for license details.

## DISCLAIMER:
By running, copying, distributing, and/or modifying this code, you agree that you are fully responsible for all of the consequences arising from your use or inability to use this program. You are in full control of which websites this meeting scheduler will visit.

## How to Use This Code
### Download/Setup
 1. Go to the [official Meeting Scheduler GitHub page](https://github.com/anshgandhi4/MeetingScheduler).
 2. Click on the green "Code" button and click on "Download ZIP".
 3. Unzip the folder.
 4. Create a new file in the directory called "links.txt".
 5. Change the text in the first line to the meeting link for your first period class.
 6. Change the text in the second line to the meeting link for your second period class.
 7. Repeat this for the first six lines of the file.
 8. If for whatever reason you do not want this scheduler to open a meeting for a specific class period, just leave that line blank.
 9. For the seventh line of the file, put in the number of minutes early you want to attend your classes. For example, if you want to open all of your class 2 minutes before they actually start, put 2 as the seventh line. Make sure that the number you enter is a whole number.
 10. An example file (example.txt) is provided.

### Using the Code
Once you update links.txt, there are two ways to use this code.

If you would like to use this code as is, simply run meetingscheduler.exe. It will open a terminal and will print the time every minute (so you know that it is still running). If you would like to stop the program, just close the terminal.

**Note:** You can only run this on Windows, as the .exe file type is not supported natively on MacOS or Linux based operating systems.

If you would like to use this code to modify it to your own needs, follow the steps below.
 1. You will need to some version of Python 3 installed on your computer.
 2. The source code (meetingscheduler.py) will be ready for you to modify and run. No package installs are necessary.
 3. Make sure to follow GNU GPL license rules regarding the legal restrictions of copying, distribution, modification, etc. of this code.

## Changelog
### Version 1.0 (08/27/20)
Meeting Scheduler Features include:
 - Automatically opening meeting links for different classes
 - Opens the links in your default browser
 - Based off of [Mission San Jose High School Bell Schedule](http://mission-fusd-ca.schoolloop.com/file/1500711509070/1500711507309/9033068015616581745.pdf)
 - Automatically terminates at 2:30 pm (once school is over)
