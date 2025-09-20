task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")

time_bound = input("Is it time-bound? (yes/no): ")

reminder = ""

match priority.lower():
    case 'high':
        reminder = f"Reminder: '{task}' is a high priority task"
    case 'medium':
        reminder = f"Note: '{task}' is a medium priority task"
    case 'low':
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unknown priority"

if time_bound.lower() == 'yes':
    reminder += " that requires immediate attention today!"
elif time_bound.lower() == 'no':
    reminder += ". Consider completing it when you have free time."
else:
    reminder += "."
    
print(reminder)

