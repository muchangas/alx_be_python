from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in a specified format.
    """
    # Use datetime.now() directly because it was imported from the datetime module
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """
    Calculates and displays a future date based on user input.
    """
    try:
        num_days_str = input("Enter the number of days to add to the current date: ")
        num_days = int(num_days_str)

        # Get current date
        current_date = datetime.now()

        # Calculate future date using timedelta (imported directly)
        future_date = current_date + timedelta(days=num_days)

        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()