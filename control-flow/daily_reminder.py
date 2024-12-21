# daily_reminder.py

# Prompt the user for a task description
task = input("Enter your task: ")

# Prompt for task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority
match priority:
    case "high":
        priority_message = "high priority"
    case "medium":
        priority_message = "medium priority"
    case "low":
        priority_message = "low priority"
    case _:
        priority_message = "unknown priority"

# Build the reminder message
if time_bound == "yes":
    reminder_message = f"Reminder: '{task}' is a {priority_message} task that requires immediate attention today!"
else:
    reminder_message = f"Note: '{task}' is a {priority_message} task. Consider completing it when you have free time."

# Print the final reminder message
print('Finish project report' is a high priority task that requires immediate attention today!)
