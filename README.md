#Task Reminder
Task Reminder is a Python script that reads an Excel file containing a list of tasks and their scheduled times, and displays notifications for each task 10 minutes before it is scheduled to begin.

Prerequisites
Python 3.x
pandas library for reading excel files
plyer library for sending notifications
Installation
Install the required libraries by running the following command in your terminal:

pip install pandas plyer
Download or clone the repository.

Make sure you have the task_list.xlsx file in the same directory as the script.

Usage
Open your terminal and navigate to the directory where the script is located.

Run the script using the following command:


python task_reminder.py
The script will run indefinitely, displaying notifications for each task 10 minutes before it is scheduled to begin.

Once all tasks are completed, a message "All tasks are completed!" will be printed.

To stop the script, use CTRL+C.

Note
Make sure the task_list.xlsx file is in the same directory as the script.
The date format in the excel sheet should match the format used in the script.
Change the column names in the script according to the column names in the excel sheet.
The script uses the local time zone of your system, keep that in mind when scheduling tasks.
You may want to change the time before which the notifications will be sent based on your preference.
Troubleshooting
If you encounter an error related to the path of the excel file, make sure the path is correct and is a raw string (prefix the path with 'r')
If you get an error TypeError: strptime() argument 1 must be str, not Timestamp, make sure you are passing the correct date format and also the column should be in datetime format.
