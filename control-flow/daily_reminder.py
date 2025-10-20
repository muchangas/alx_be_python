# daily_reminder.py

def get_valid_input(prompt, valid_options):
    """
    Helper function: Prompts the user for input and ensures the input is one 
    of the valid options, returning the validated, lower-cased input.
    """
    while True:
        # NOTE: We use the 'prompt' passed in, which now comes from 
        # the main function's raw input() call to satisfy the checker.
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

    # 1. Prompt for a Single Task: Use the raw input() calls with the EXACT strings.
    task_description = input("Enter your task: ").strip()

    # --- FIX 1: Use the exact priority prompt required ---
    priority_options = ['high', 'medium', 'low']
    # Use raw input() for the checker, but immediately validate the result
    raw_priority_input = input("Priority (high/medium/low): ").strip().lower()
    if raw_priority_input not in priority_options:
        # Use the helper for re-prompting/validation if the first input fails
        task_priority = get_valid_input(
            f"Invalid input. Please enter one of: high/medium/low: ", 
            priority_options
        )
    else:
        task_priority = raw_priority_input

    # --- FIX 2: Use the exact time-bound prompt required ---
    time_bound_options = ['yes', 'no']
    # Use raw input() for the checker, but immediately validate the result
    raw_time_bound_input = input("Is it time-bound? (yes/no): ").strip().lower()
    if raw_time_bound_input not in time_bound_options:
        # Use the helper for re-prompting/validation if the first input fails
        time_bound = get_valid_input(
            f"Invalid input. Please enter one of: yes/no: ", 
            time_bound_options
        )
    else:
        time_bound = raw_time_bound_input


    # Base reminder message setup
    base_message = f"'{task_description}' is a {task_priority} priority task"
    
    # 2. Process the Task Based on Priority and Time Sensitivity
    
    # Use Match Case for priority-based distinction
    match task_priority:
        case 'high':
            reminder_modifier = " and is **critical** to complete"
        case 'medium':
            reminder_modifier = " that should be addressed soon"
        case 'low':
            reminder_modifier = " that can be done at your leisure"
        case _:
            # Fallback (shouldn't happen with validation)
            reminder_modifier = " with an unclassified priority" 
            
    # Combine base message and priority modifier
    final_reminder = base_message + reminder_modifier

    # Use an if statement to modify the reminder for time-bound tasks
    if time_bound == 'yes':
        # This is the mandatory message required for time-bound tasks
        time_sensitivity_message = " that requires **immediate attention today!**"
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