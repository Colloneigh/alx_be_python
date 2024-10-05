#Importing the necessary components from the datetime module
from datetime import datetime, timedelta

#Part 1 Diplay the current date and time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

#Part 2 Calculate a future date based on user input
def calculate_future_date():
    current_date = datetime.now()
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days = days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

#Main function to run both parts
def main():

    #display current date and time
    display_current_datetime()

    #calculate and display the future date
    calculate_future_date()

if __name__ == "__main__":
    main()