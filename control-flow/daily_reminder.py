# daily_reminder.py

# Prompt the user for a task description
task = input("Enter your task: ")

# Prompt for task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the priority message based on the input
match priority:
    case "high":
        priority_message = "high priority"
    case "medium":
        priority_message = "medium priority"
    case "low":
        priority_message = "low priority"
    case _:
        priority_message = "unknown priority"

# Generate the reminder message
if time_bound == "yes":
    reminder_message = f"Reminder: '{task}' is a {priority_message} task that requires immediate attention today!"
else:
    reminder_message = f"Reminder: '{task}' is a {priority_message} task that does not require immediate attention today."

# Print the final reminder message in the required format
print(reminder_message)
