import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'ch': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'ny': 'new_york_city.csv',
              'nyc': 'new_york_city.csv',
              'washington': 'washington.csv',
              'wa': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('\n(chicago, new york city, washington)')
    
    city = str(input('Please type in the city from the list above:').lower())
    while city not in CITY_DATA.keys():
        try:
            print(' *** Ooops.. check for typoo ***')
            city = str(input('Please type in the city from the list above:').lower())
        except:
            print('Invalid')
            

    # TO DO: get user input for month (all, january, february, ... , june)
    print('\nfilter by month?(eg. january) or type all:')
    month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all']
    month = input('Please type in the month:')
    while month not in month_list:
        try:
            print(' *** Ooops.. not in the list ***')
            month = str(input('Please type in a valid month:'))
        except:
            print('Invalid')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #calendar.month_name
    print('\nfilter by day?(eg. monday) or type all:')
    day_list = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    day = str(input('Please type in the day:'))
    while day not in day_list:
        try:
            print(' *** Ooops.. choose a valid day ***')
            day = str(input('Please type in the day:'))
        except:
            print('Invalid')
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

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    
        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    most_comon_month = calendar.month_name[df['month'].mode()[0]]
    print('Most Common Month: ', most_comon_month)

    # TO DO: display the most common day of week

    most_comon_day = df['day_of_week'].mode()[0]
    print('Most Common Day: ', most_comon_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_comon_hour = df['hour'].mode()[0]
    print('Most Common Hour: ', most_comon_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_comon_SS = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station: ', most_comon_SS)

    # TO DO: display most commonly used end station
    most_comon_ES = df['End Station'].mode()[0]
    print('Most Commonly Used End Station: ', most_comon_ES)

    # TO DO: display most frequent combination of start station and end station trip
    most_comon_SSES= df[['Start Station', 'End Station']].mode().loc[0]
    print('Most Commonly Used Start And End Station: ', most_comon_SSES)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: ', round(mean_travel_time, 2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of User Types:\n', user_types)
    print('\n')
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Counts of Genders:\n', gender)


    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_yob = int(df['Birth Year'].min())
        most_recent_yob = int(df['Birth Year'].max())
        most_common_yob = int(df['Birth Year'].mode()[0])
    
        print('Earliest Year of Birth: ', earliest_yob)
        print('Most Recent Year of Birth: ', most_recent_yob)
        print('Most Comon Year of Birth: ', most_common_yob)
        
    except KeyError:
        print('')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        view_data = input(('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower())
        start_loc = 0
        while view_data == 'yes':
            try:
                print(df.iloc[start_loc:start_loc + 5])
                start_loc += 5
                view_data = input("Do you wish to continue?: ").lower()
            except:
                continue
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
