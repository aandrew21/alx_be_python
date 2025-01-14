from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in a readable format."""
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """Calculate and display the future date based on user input."""
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: ").strip())
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()