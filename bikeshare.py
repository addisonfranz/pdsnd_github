import time
import pandas as pd
import numpy as np
import calendar as cal


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # getting user input for city (Chicago, New York City, Washington)
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington? ")
        city = city.title()
        if city == 'Chicago':
            print("You entered {}".format(city))
            break
        elif city == 'New York City':
            print("You entered {}".format(city))
            break
        elif city == 'Washington':
            print("You entered {}".format(city))
            break
        else:
            print("That is not a valid input.")
    # getting user input on the data filter they would like to apply (month, day, both, or none)
    while True:
        filter_q = input("Would you like to filter by month, day, both, or none? ")
        filter_q = filter_q.lower()
        if filter_q == 'month':
            break
        if filter_q == 'day':
            break
        if filter_q == 'both':
            break
        if filter_q == 'none':
            break
        else:
            print('That is not a valid input.')
    # getting user input for the specific month or day filter they would like to apply or applying no filter
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if filter_q == 'month':
        while True:
            month = input("What month would you like to filter by? January, February, March, April, May, June? ")
            month = month.title()
            day = 'all'
            if month in months:
                print('You have filtered by {}. There is no day filter.'.format(month))
                break
            else:
                print('Not a valid month input.')
    elif filter_q == 'day':
        while True:
            month = 'all'
            day = input("What day would you like to filter by? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday? ")
            day = day.title()
            if day in days:
                print('You have filtered by {}. There is no month filter.'.format(day))
                break
            else:
                print('Not a valid day input.')
    elif filter_q == 'both':
        while True:
            month = input("What month would you like to filter by? January, February, March, April, May, June? ")
            month = month.title()
            day = input("What day would you like to filter by? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday? ")
            day = day.title()
            if (month in months) and (day in days):
                print('You have filtered by {} and {}.'.format(month, day))
                break
            else:
                print('Not a valid input. You entered either an incorrect month or day.')
    elif filter_q == 'none':
        month = 'all'
        day = 'all'
        print('You have chosen not to filter by month or day.')

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
    # loading the CSV files based on the city filter and adding the city to the dataframe as its own column
    if city == 'Chicago':
        df = pd.read_csv('./chicago.csv')
        df['City'] = city
    elif city == 'New York City':
        df = pd.read_csv('./new_york_city.csv')
        df['City'] = city
    else:
        df = pd.read_csv('./washington.csv')
        df['City'] = city
    # converting dates into usable formats and adding to the data frame
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    # applying month filter
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # applying day filter
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
    df['hour'] = df['Start Time'].dt.hour
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # displaying the most common month (https://docs.python.org/2/library/calendar.html, 11/11/2018)
    most_common_month = df['month'].mode()[0]
    print('Most common month:', cal.month_name[most_common_month])
    # displaying the most common day of week
    most_common_day = df['day'].mode()[0]
    print('Most common day:', most_common_day)
    # displaying the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # displaying most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ', popular_start)

    # displaying most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('The most commonly used end station is: ', popular_end)

    # displaying most frequent combination of start station and end station trip
    df['Common Trip'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Common Trip'].mode()[0]
    print('The most popular trip is: ', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # displaying total travel time and mean travel time
    beg_time = pd.to_datetime(df['Start Time'])
    end_time = pd.to_datetime(df['End Time'])
    travel_time = end_time - beg_time
    total_travel_time = travel_time.sum()
    avg_travel_time = travel_time.mean()
    print('Total travel time is: ', total_travel_time)
    print('Average travel time is: ', avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # displaying counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # displaying counts of gender (where applicable)
    while True:
        if (df['City'].iloc[1]) == 'Washington':
            print('This data is not available for this city.')
            break
        else:
            gender_count = df['Gender'].value_counts()
            print(gender_count)
            break
    # displaying earliest, most recent, and most common year of birth (where applicable)
    while True:
        if (df['City'].iloc[1]) == 'Washington':
            print('This data is not available for this city.')
            break
        else:
            earliest_birth = int(df['Birth Year'].min())
            recent_birth = int(df['Birth Year'].max())
            common_birth = int(df['Birth Year'].mode()[0])
            print('The oldest rider was born in {}, the youngest rider was born in {}, and the most riders were born in {}.'.format(earliest_birth, recent_birth, common_birth))
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Gives the used the option to display raw data."""
    # asking for user input
    data_req = input('Would you like to see the first 5 rows of raw data? (Y/N) ')
    data_req = data_req.upper()
    start = 0
    end = 5
    # looping for Y/N answer
    while True:
        while data_req == 'Y':
            print(df.iloc[start: end])
            data_req = input('Would you like to see the next 5 rows of raw data? (Y/N) ')
            data_req = data_req.upper()
            start += 5
            end +=5
        if data_req == 'N':
            exit(print('Now exiting the program!'))
        else:
            print('That is not a valid entry')
        raw_data(df)
        break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
