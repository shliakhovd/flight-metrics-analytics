import pandas as pd


def read_data():
    flights_df = pd.read_csv('2008_rand.csv')
    airports_df = pd.read_csv('airports.csv')
    return flights_df, airports_df


def calculate_distance_stats(flights_df):
    average_distance_flight = flights_df['Distance'].mean()
    minimum_distance_flight = flights_df['Distance'].min()
    maximum_distance_flight = flights_df['Distance'].max()

    return average_distance_flight, minimum_distance_flight, maximum_distance_flight


def find_max_distance_flight(flights_df):
    max_distance_flight_row = flights_df.loc[flights_df['Distance'].idxmax()]
    maximum_distance_day = max_distance_flight_row['DayofMonth']
    maximum_flight_num = max_distance_flight_row['FlightNum']

    return maximum_distance_day, maximum_flight_num


def find_most_flights_day(flights_df):
    flights_df["DayOfWeekName"] = flights_df["DayOfWeek"].map(
        {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"})
    most_flights_day = flights_df["DayOfWeekName"].value_counts().idxmax()

    return most_flights_day


def find_top_origins_december(flights_df, airports_df):
    december_flights = flights_df[flights_df['Month'] == 12]

    top_origins = december_flights['Origin'].value_counts().head(5)

    top_origins_cities = airports_df[airports_df['iata'].isin(top_origins.index)][['iata', 'city']]
    top_origins_cities.columns = ['Origin', 'City']

    return top_origins_cities


def find_max_arrival_delay(flights_df):
    max_arrival_delay_row = flights_df.loc[flights_df["ArrDelay"].idxmax()]
    max_arrival_delay_airport = max_arrival_delay_row["Dest"]
    max_arrival_delay_minutes = max_arrival_delay_row["ArrDelay"]

    return max_arrival_delay_airport, max_arrival_delay_minutes


def print_results(average_distance, minimum_distance, maximum_distance,
                  maximum_distance_day, maximum_flight_num, most_flights_day,
                  top_origins_cities, max_arrival_delay_airport, max_arrival_delay_minutes):
    print(f"Average Distance: {average_distance}")
    print(f"Minimum Distance: {minimum_distance}")
    print(f"Maximum Distance: {maximum_distance}")
    print(f"Day with Maximum Distance: {maximum_distance_day}")
    print(f"Flight Number with Maximum Distance: {maximum_flight_num}")
    print(f"Day with Most Flights: {most_flights_day}")
    print("Top 5 Origins in December:")
    print(top_origins_cities)
    print(f"Airport with Maximum Arrival Delay: {max_arrival_delay_airport}")
    print(f"Maximum Arrival Delay (minutes): {max_arrival_delay_minutes}")


if __name__ == "__main__":
    flights_df, airports_df = read_data()
    average_distance, minimum_distance, maximum_distance = calculate_distance_stats(flights_df)
    maximum_distance_day, maximum_flight_num = find_max_distance_flight(flights_df)
    most_flights_day = find_most_flights_day(flights_df)
    top_origins_cities = find_top_origins_december(flights_df, airports_df)
    max_arrival_delay_airport, max_arrival_delay_minutes = find_max_arrival_delay(flights_df)

    print_results(average_distance, minimum_distance, maximum_distance,
                  maximum_distance_day, maximum_flight_num, most_flights_day,
                  top_origins_cities, max_arrival_delay_airport, max_arrival_delay_minutes)
