-- deleting irrelevant columns

-- creating new columns, named as 'ride_length','day_number','day_of_week' and 'month'

Before starting the combination and analysis processes, I have checked all the 12 tables individually on Excel.

Intially each table consist of **13 variables**, as shown in the following:-
| **No.**|  **Variable**       |  **Description**                                        |
|--------|------------------   | --------------------------------------------------------|
| 1      | ride_id             | Unique ID assigned to each ride                         |
| 2      | rideable_type       | classic, docked, or electric                            |
| 3      | started_at          | Date and time at the start of trip                      |
| 4      | ended_at            | Date and time at the end of trip                        |
| 5      | start_station_name  | Name of the station where the ride journey started from |
| 6      | start_station_id    | ID of the station where the ride journey started from   |
| 7      | end_station_name    | Name of the station where the ride trip ended at        |
| 8      | end_station_id      | ID of the station where the ride trip ended at          |
| 9      | start_lat           | Latitude of starting station                            |
| 10     | start_lng           | Longitude of starting station                           |
| 11     | end_lat             | Latitude of ending station                              |
| 12     | end_lng             | Longitude of ending station                             |                            
| 13     | member_casual       | Type of membership of each rider                        |

and the **data type** of each variable is depicted below:

<img width="352" alt="DataType" src="https://github.com/minbean/Google-Data-Analytics-Capstone-Project-Cyclistic-Case-Study/assets/101321188/3f2e5e1d-b18e-4c9b-92e8-c6e35ce8ae12">

I have deleted **9 variables** that are irrelevant to my objective of analysis:-
| **No.**|  **Variable**       |  **Description**                                        |
|--------|------------------   | --------------------------------------------------------|
| 1      | ride_id             | Unique ID assigned to each ride                         |
| 5      | start_station_name  | Name of the station where the ride journey started from |
| 6      | start_station_id    | ID of the station where the ride journey started from   |
| 7      | end_station_name    | Name of the station where the ride trip ended at        |
| 8      | end_station_id      | ID of the station where the ride trip ended at          |
| 9      | start_lat           | Latitude of starting station                            |
| 10     | start_lng           | Longitude of starting station                           |
| 11     | end_lat             | Latitude of ending station                              |
| 12     | end_lng             | Longitude of ending station                             |                            

And the created **4 new variables**, i.e. 'ride_length','day_number','day_of_week' and 'month', usig the following described formulas for each:-



          
