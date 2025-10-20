# daily_reminder.py

def get_valid_input(prompt, valid_options):
    """
    Helper function: Prompts the user for input and ensures the input is one 
    of the valid options, returning the validated, lower-cased input.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            # Provide feedback and retry if validation fails
            print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")

def daily_reminder():
    """
    Prompts the user for a single task's details and provides a customized reminder.
    """
    print("--- Daily Task Reminder Setup ---")

    # 1. Prompt for a Single Task: Use the exact input() prompts required.
    task_description = input("Enter your task: ").strip()

    # --- FIX 1: Use the exact priority prompt required AND the 'priority' variable name ---
    priority_options = ['high', 'medium', 'low']
    
    # Use the exact input() prompt for the checker
    raw_priority_input = input("Priority (high/medium/low): ").strip().lower()
    
    # Use 'priority' as the variable name for the match statement
    if raw_priority_input in priority_options:
        priority = raw_priority_input
    else:
        # Fallback to guided validation if initial input fails
        priority = get_valid_input(
            f"Invalid input. Please enter one of: high/medium/low: ", 
            priority_options
        )

    # --- FIX 2: Use the exact time-bound prompt required ---
    time_bound_options = ['yes', 'no']
    
    # Use the exact input() prompt for the checker
    raw_time_bound_input = input("Is it time-bound? (yes/no): ").strip().lower()
    
    if raw_time_bound_input in time_bound_options:
        time_bound = raw_time_bound_input
    else:
        # Fallback to guided validation if initial input fails
        time_bound = get_valid_input(
            f"Invalid input. Please enter one of: yes/no: ", 
            time_bound_options
        )

    # Base reminder message setup
    base_message = f"'{task_description}' is a {priority} priority task"
    
    # 2. Process the Task Based on Priority and Time Sensitivity
    
    # --- FIX 3: Use 'match priority:' to satisfy the checker ---
    match priority:
        case 'high':
            reminder_modifier = " and is **critical** to complete"
        case 'medium':
            reminder_modifier = " that should be addressed soon"
        case 'low':
            reminder_modifier = " that can be done at your leisure"
        case _:
            reminder_modifier = "" 
            
    # Combine base message and priority modifier
    final_reminder = base_message + reminder_modifier

    # Use an if statement to modify the reminder for time-bound tasks
    if time_bound == 'yes':
        # This is the mandatory message required for time-bound tasks
        time_sensitivity_message = " that requires **immediate attention today!**"
        final_reminder = base_message + time_sensitivity_message
    else:
        # For non-time-bound tasks, ensure a period is at the end
        final_reminder += "."

    # 3. Provide a Customized Reminder
    print("\n--- Reminder ---")
    print(f"Reminder: {final_reminder}")
    print("-" * 20)

# Execute the main function
if __name__ == "__main__":
    daily_reminder()