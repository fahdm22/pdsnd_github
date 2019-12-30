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
    while True:
        city = input("Would you like to see data for Chicago, New York City or Washington?:   ")
        if city.lower() not in ['chicago', 'new york city', 'washington']:
            print("Sorry, please input Chicago, New York City or Washington.\n\n")
            continue
        else:
        #we're happy with the value given.
        #we're ready to exit the loop.
            print('-'*40)
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Would you like to filter the data by month of not all? \n Please choose january, february,.., june. \n For no month filter, choose all:  ")
        if month.lower() not in ['all', 'january','february','march','april','may','june']:
            print("Sorry, please input all, January, February, March, April, May, or June\n\n")
            continue
        else:
        #we're happy with the value given.
        #we're ready to exit the loop.
            print('-'*40)
            break



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Would you like to filter the data by day of not all? \n Please choose monday, tuesday,.., sunday. \n For no day filter, choose all:   ")
        if day.lower() not in ['all', 'monday','tuesday','wednesday','thursday','friday','saturday','sunday']:

            print("Sorry, please input all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday\n\n")
            continue
        else:
        #we're happy with the value given.
        #we're ready to exit the loop.
            print('-'*40)
            break


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
    # load data file into a dataframe

    df = pd.read_csv(CITY_DATA[city.lower()])
        # convert the Start Time column to datetime
    df['Start Time'] =  pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month.lower()
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
    # find the most common month
    months = ['January','February','March','April','May','June']
    common_month = df['month'].value_counts().idxmax()
    print('Most common month:', months[common_month-1])

    # TO DO: display the most common day of week
    #find the most common day of the week
    common_day = df['day_of_week'].value_counts().idxmax()
    print('Most common day of week is:', common_day)

    # TO DO: display the most common start hour
    #find the most common start hour
    common_hour = df['hour'].value_counts().idxmax()
    print('Most common hour of day:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print('Most common used start station:', df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    
    print('Most common used end station:', df['End Station'].value_counts().idxmax())


    # TO DO: display most frequent combination of start station and end station trip
    df['Start to End Station Combination'] = df['Start Station']+'  _to_  '+df['End Station']
    most_frequent_trip = df['Start to End Station Combination'].value_counts().idxmax()
    print('Most frequent combination of start station and end station trip is:', most_frequent_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is: {} seconds'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Mean travel time is: {} seconds'.format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\n Counts of user types is as below\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('\n Counts of gender is as below\n', df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\n Earliest year of birth is: ', df['Birth Year'].min())
        print('\n Most recent year of birth is: ', df['Birth Year'].max())
        print('\n Most common year of birth is: ', df['Birth Year'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(city):
    #the function displays data in its raw form.
    # all the data manuplation so far is done away with
    while True:
        display = input("Would you like to see the raw data? \n Please choose yes or no.:   ")
        if display.title() not in ['Yes', 'No']:
            print("\n\nSorry, please input 'yes' or 'no'.\n")
            continue
        elif display.title() == 'No':
            print("\n\nThank you, no raw data will be displayed.")
            print('-'*40)
            break
        else:
            raw_data(city.lower())
            break

def raw_data(city):
    count = 5
    print("\nThank you, Raw data will be displayed five lines at a time.:\n\n")
    df = pd.read_csv(CITY_DATA[city.lower()])
    print(df.iloc[:5])
    print('-'*40)
    while True:
        more_raw_data = input("Would you like to see the more 5 lines of raw data? \n Please choose yes or no.:   ")
        if more_raw_data.title() not in ['Yes', 'No']:
            print("\n\nSorry, please input 'yes' or 'no'.\n")
            continue
        elif more_raw_data.title() == 'No':
            print("\n\nThank you, no more raw data will be displayed.")
            print('-'*40)
            break
        else:
           print(df.iloc[count:count+5])
           count +=5
           continue


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
