import streamlit as st
import datetime

# Get current date and time
current_datetime = datetime.datetime.now()

# Extract year, month, and day from the current datetime
current_year = current_datetime.year
current_month = current_datetime.month
current_day = current_datetime.day

# Display current date components
st.write("Current Year:", current_year)
st.write("Current Month:", current_month)
st.write("Current Day:", current_day)

# Set up the Streamlit app title
st.title("Date range")

# Define the minimum and maximum allowable dates for selection
# Start date is set to 7 days ago from the current date
min_date = datetime.datetime(current_year, current_month, current_day - 7)
# End date is set to the current date
max_date = datetime.date(current_year, current_month, current_day)

# Create a date input widget allowing the selection of a date range
a_date = st.date_input("SELECT THE DATE RANGE", (min_date, max_date))

# Check if a date range is selected
if a_date:
    # Format the start date
    start_date_formatted = a_date[0].strftime("%Y-%m-%d")
    
    # Check if end date exists in the tuple
    if len(a_date) > 1:
        # Format the end date
        end_date_formatted = a_date[1].strftime("%Y-%m-%d")
        
        # Calculate the number of days selected
        num_days_selected = (a_date[1] - a_date[0]).days + 1  # Add 1 to include both start and end dates
        
        # Display the date range and number of days selected
        st.write('THE RANGE IS FROM :', start_date_formatted, 'to', end_date_formatted)
        st.write('NUMBER OF DAYS SELECTED:', num_days_selected)
    else:
        # If only one date is selected, display that date
        st.write('THE SELECTED DATE IS :', start_date_formatted)
