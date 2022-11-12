import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # create empty varibles for city, month, and day. Then use a while loop to handle any incorrect inputs
    city = ''
    while city not in CITY_DATA.keys():
        print("\nWould you like to look at Data for Chicago, New York City, or Washington?\n")    
        city = input().lower()
        if city not in CITY_DATA.keys():
            print("\nThat is not a valid city. Please enter either Chicago, New York City, or Washington.")

    # TO DO: get user input for month (all, january, february, ... , june)
    #create dictionary to store month variables
    month_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    
    month = ''
    while month not in month_dict.keys():
        print("\nWhich month would you like to get data for? Enter month name between January and June or type All to view all available months.\n")
        month = input().lower()
        if month not in month_dict.keys():
            print("\nThat is not a valid input for month.")
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #create list of days with an 'all' option to store avaiable options
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = ''
    while day not in day_list:
        print("\nLastly, which day of the week would you like to get data for? Enter a week day name between Monday and Sunday or enter all to view all days.\n")
        day = input().lower()
        if day not in day_list:
            print("\nThat is not a valid weekday name.")
        
    print('-'*40)
    
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month  
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    if day != 'all':   
        df = df[df['day_of_week'] == day.title()] 
        
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    start_time = time.time()

    # TO DO: display the most common month              
    common_month = df['month'].mode()[0]
    print("Most Common Month: ", common_month)
              
    # TO DO: display the most common day of week
    common_weekday = df['day_of_week'].mode()[0]

    print("Most Common Day of Week: ", common_weekday)
              
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print("Most Common Start Hour: ", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_starts = df['Start Station'].mode()[0]
    print("Most Common Start Station: ", common_starts)
    # TO DO: display most commonly used end station
    common_ends = df['End Station'].mode()[0]
    print("Most Common End Station: ", common_ends)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Stations'] = df['Start Station']+" "+df['End Station']
    freq_stations = df['Start End Stations'].mode().values[0]
    print("Most frequently used combination of start and end stations: ", freq_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = round(df['Trip Duration'].sum())
    print("Total travel time in seconds: ", total_time)

    # TO DO: display mean travel time
    avg_time = round(df['Trip Duration'].mean())
    print("Average travel time: ", avg_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Type and counts: ", user_types)

    # TO DO: Display counts of gender
    #Use try and except to handle the error message that will populate if Washington is selected as city as there is no gender or birth data available
    try:
        gender = df['Gender'].value_counts()
        print("Gender counts: ", gender)
    except:
        print("There is no gender data available")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = int(df['Birth Year'].min())
        print("Earliest Birth Year: ", earliest_birth)
        recent_birth = int(df['Birth Year'].max())
        print("The most recent Birth Year is: ", recent_birth)
        common_birth = int(df['Birth Year'].mode()[0])
        print("The most common Birth Year is: ", common_birth)
    except:
        print("There is not birth year data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_data(df):
    #function to get top 5 rows of data
    row = 0
    stop_row = 5
    raw_data = input("\nWould you like to view the raw data? Enter yes or no.\n").lower()
    pd.set_option('display.max_columns',200)
    
    while True:
        if raw_data == 'no':
            break
        elif raw_data == 'yes':
            print(df.iloc[row:stop_row,])
            raw_data = input("\nWould you like to view more of the raw data?\n").lower()
            row += 5
            stop_row += 5
        else:
            print("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
            
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        get_data(df)                

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
