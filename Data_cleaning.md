-- Determine the ride length in minutes 
-- Remove rows with null values 

combined_csv.info()       --get the brie summary of the new table
 #   Column         Dtype 
---  ------         ----- 
 0   rideable_type  object
 1   started_at     object
 2   ended_at       object
 3   member_casual  object
 4   ride_length    object
 5   day_number     int64 
 6   day_of_week    object
 7   month          object
dtypes: int64(1), object(7)


