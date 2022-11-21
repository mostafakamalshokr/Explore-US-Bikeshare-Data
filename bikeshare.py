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
    city= input('choose a city name (chicago , new york city , washington ,\ninput:').lower()
    while city  not in CITY_DATA.keys():
         print('your input is wrong ')
         city= input('choose a city  (chicago , new york city , washington ,\n input:').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    months= ['january', 'february', 'march', 'april', 'may', 'june','all']
    while True:
         month= input('choose a month from list (january, february, march, april, may, june)\n or choose: all\n input:').lower()
         if month in months :
             break
         else:      
             print("wrong entry")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
    while True:
       day= input('choose a day from list (saturday,sunday,monday,tuesday,wednesday,thursday,friday)\n or choose: all\n input:').lower()
       if day in days :
           break
       else:      
           print("wrong entry")

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
    df = pd.read_csv(CITY_DATA[city]) 

# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


 # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # extract hour from the Start Time column to create an hour column
    df['start_hour'] = df['Start Time'].dt.hour
# filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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
    popular_month = df['month'].mode()[0]
    print('the most common month is:',popular_month)

    # TO DO: display the most common day of week

    popular_week = df['day_of_week'].mode()[0]
    print('the most common day of week is:',popular_week)
    # TO DO: display the most common start hour
    popular_hour = df['start_hour'].mode()[0]
    print('the most common start hour is:',popular_hour)
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('most commonly used start station is ',start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('most commonly used end station is ',end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['most frequent combination route']=df['Start Station'] + "-" + df['End Station']
    print('most frequent combination trip is {}'.format(df['most frequent combination route'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration_time=df['Trip Duration'].sum().round() 
    print('total time of trips in second:',total_duration_time)
    # TO DO: display mean travel time
    mean_duaration_time=df['Trip Duration'].mean().round(2) #two decimal
    print('average time of tripsin seconds:',mean_duaration_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city, month, day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
     # TO DO: Display counts of user types
    print(df.groupby(['User Type'])['User Type'].count())
    # load data file into a dataframe
    print('- -'*40)
    df = pd.read_csv(CITY_DATA[city])
    if city== 'washington':
        print('no available data about gender for washington city')
    else:
   


    # TO DO: Display counts of gender
        gender_count=df.groupby(['Gender'])['Gender'].count()
        print(df.groupby(['Gender'])['Gender'].count())
        
        print('- -'*40)
    # TO DO: Display earliest, most recent, and most common year of birth
        print('the earliest year of birth is       : ',int(df['Birth Year'].min()))
        print('the most recent year of birth is     : ',int(df['Birth Year'].max()))
        print('the most common year of birth is     : ',int(df['Birth Year'].mode()[0]))
         
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def Look_at(df):
    """look at  5 rows of the data at a time when user accept to view data"""
    print('\ Takeing a look at the first few rows ...\n')
    start_time = time.time()
    n=0
    view_input=input('would you like to view  5 row of data press (yes) or (no)').lower()
    if  view_input not in['yes','no']:
        print("wrong entry")
        view_input=input('would you like to view  5 row of data press (yes) or (no)').lower()
    elif  view_input!= 'yes':
        print('finished')
    else:    
        
        n=0
        while n+5>=0:
            print(df[n:n+5])
            n = n+5
            view_input=input('would you like to view  5 row of data press (yes) or (no)').lower()
            if  view_input!= 'yes':
                break
            
            
        
           
    print("\nThis took %s seconds." % (time.time() - start_time))    
       
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city, month, day)
        Look_at(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('finished all,thanks')
            print('-'*40)
            print('-'*40)
            print('-'*40)
            break
    


if __name__ == "__main__":
    main()
