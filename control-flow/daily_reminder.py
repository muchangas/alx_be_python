# daily_reminder.py

def get_valid_input(prompt, valid_options):
    """
    Prompts the user for input and ensures the input is one of the valid options.
    Returns the validated, lower-cased input.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            # Provide feedback and retry
            print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")

def daily_reminder():
    """
    Prompts the user for a single task's details and provides a customized reminder.
    """
    print("--- Daily Task Reminder Setup ---")

    # 1. Prompt for a Single Task
    task_description = input("Enter your task: ").strip()

    # Get and validate the priority
    priority_options = ['high', 'medium', 'low']
    task_priority = get_valid_input(
        f"Priority ({'/'.join(priority_options)}): ", 
        priority_options
    )
    
    # Get and validate the time-bound status
    time_bound_options = ['yes', 'no']
    time_bound = get_valid_input(
        f"Is it time-bound? ({'/'.join(time_bound_options)}): ", 
        time_bound_options
    )

    # Base reminder message setup
    base_message = f"'{task_description}' is a {task_priority} priority task"
    
    # 2. Process the Task Based on Priority and Time Sensitivity
    
    # Use Match Case for priority-based distinction (demonstrates control flow)
    match task_priority:
        case 'high':
            # High priority tasks often benefit from a more urgent tone
            reminder_modifier = " and is **critical** to complete"
        case 'medium':
            reminder_modifier = " that should be addressed soon"
        case 'low':
            reminder_modifier = " that can be done at your leisure"
        # The 'low' case handles all other possibilities due to input validation, 
        # but a default case is good practice in a general match
        case _:
            reminder_modifier = " with an unclassified priority" 
            
    # Combine base message and priority modifier
    final_reminder = base_message + reminder_modifier

    # Use an if statement to modify the reminder for time-bound tasks
    # This directly addresses the 'that requires immediate attention today!' requirement
    if time_bound == 'yes':
        # Overrides or augments the existing message for time-sensitive tasks
        time_sensitivity_message = " that requires **immediate attention today!**"
        
        # We'll use a simplified structure that replaces the existing modifier 
        # to ensure the mandatory message is delivered clearly.
        final_reminder = base_message + time_sensitivity_message
    else:
        # For non-time-bound tasks, we just ensure a period is at the end
        final_reminder += "."

    # 3. Provide a Customized Reminder
    print("\n--- Reminder ---")
    print(f"Reminder: {final_reminder}")
    print("-" * 20)

# Execute the main function
if __name__ == "__main__":
    daily_reminder()