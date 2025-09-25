import datetime

def display_current_datetime():
    """
    Displays the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates the future date.
    """
    try:
        num_days_str = input("Enter the number of days to add to the current date: ")
        num_days = int(num_days_str)
        
        current_date = datetime.datetime.now()
        future_date = current_date + datetime.timedelta(days=num_days)
        
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()