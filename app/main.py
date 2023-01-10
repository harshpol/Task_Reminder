import pandas as pd
from datetime import datetime, timedelta
from plyer import notification
import openpyxl

# Read the Excel file
df = pd.read_excel("task_list.xlsx")

# Initialize a variable to keep track of completed tasks
completed_tasks = 0

while True:
    # Loop through the rows in the dataframe
    for index, row in df.iterrows():
        task = row["Task"]
        scheduled_time = row["Time"]

        # Calculate the time remaining until the task is scheduled
        now = datetime.now()
        time_remaining = scheduled_time - now
        minutes_remaining = time_remaining.total_seconds() // 60

        # Check if the scheduled time is within 10 minutes of now
        if minutes_remaining <= 10 and minutes_remaining >= 9:
            # Display a notification for the task
            notification.notify(
                title="Task Reminder",
                message=task,
                app_icon=r"E:\personal_folder\Task_Reminder\app\clock_128.ico",
                timeout=10
            )
            completed_tasks += 1
    # Check if all the tasks are completed
    if completed_tasks == len(df):
        break

print("All tasks are completed!")
