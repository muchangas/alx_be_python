# daily_reminder.py

def daily_reminder():
    """
    Prompts the user for a single task, its priority, and time-sensitivity,
    then provides a customized reminder using match-case and if statements.
    """

    print("--- Personal Daily Reminder Script ---")

    # --- 1. Prompt for a Single Task ---
    
    # Task Description
    task = input("Enter your task: ").strip()

    # Task Priority (with simple input validation loop)
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ('high', 'medium', 'low'):
            break
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
    
    # Time Sensitivity (with simple input validation loop)
    while True:
        time_bound_input = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound_input in ('yes', 'no'):
            break
        print("Invalid response. Please enter 'yes' or 'no'.")

    # Convert time-bound input to a boolean for easier conditional checks later
    is_time_bound = (time_bound_input == 'yes')
    
    # --- 2. Process the Task and Construct the Base Reminder ---
    
    # Initialize the base reminder message
    base_message = f"'{task}' is a {priority} priority task"

    # Use Match Case to react differently based on priority
    match priority:
        case 'high':
            # High priority tasks often have the most demanding tone.
            pass  # The default base message is already strong.
        case 'medium':
            # Medium priority tasks might get a slightly milder emphasis.
            base_message += ", and should be worked on soon"
        case 'low':
            # Low priority tasks can be framed as flexible.
            base_message += ", which can be handled when time permits"
        case _:
            # Fallback, though the loop prevents this case from being reached
            base_message += ", with an unknown priority level"
            
    # --- 3. Modify the Reminder based on Time Sensitivity ---
    
    # Initialize the time-sensitive message part
    time_sensitivity_message = ""
    
    # Use an if statement to modify the reminder if the task is time-bound
    if is_time_bound:
        # Append the required message for time-bound tasks
        time_sensitivity_message = " that requires immediate attention today!"
    else:
        # Append a concluding statement for non-time-bound tasks
        time_sensitivity_message = "."

    # --- 4. Provide a Customized Reminder ---
    
    final_reminder = base_message + time_sensitivity_message
    
    print("\nReminder:", final_reminder)

if __name__ == "__main__":
    # The while True loop here keeps the script running for multiple reminders 
    # until the user decides to stop, making it slightly more robust/interactive,
    # though it's optional per the initial prompt.
    while True:
        daily_reminder()
        
        # Simple loop continuation check
        another = input("\nDo you want to enter another reminder? (y/n): ").strip().lower()
        if another != 'y':
            print("Reminder session ended. Have a productive day! 👋")
            break
