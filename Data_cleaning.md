-- Determine the ride length in minutes 
-- Remove rows with null values 

# Get the brief summary of the new table

**combined_csv.info()**       

| **#**|  **Columns**          |  **Dtype** |
|--------|------------------   | -----------|
| 0      | rideable_type       | object     |
| 1      | started_at          | object     |
| 2      | ended_at            | object     |
| 3      | member_casual       | object     | 
| 4      | ride_length         | object     |
| 5      | day_number          | int64      |
| 6      | day_of_week         | object     |
| 7      | month               | object     |

dtypes: int64(1), object(7)

-We see that, the data type for "started_at" and "ended_at" has changed to object-type data.

-So, we have to change it back to datetime64 - type data:-

**combined_csv["started_at"] = combined_csv["started_at"].astype("datetime64[ns]")**

**combined_csv["ended_at"] = combined_csv["ended_at"].astype("datetime64[ns]")**

**combined_csv['ride_length'] = (combined_csv['ended_at'] - combined_csv['started_at']).dt.total_seconds() / 60**

**combined_csv.info()**
| **#**  |  **Columns**        |  **Dtype**    |
|--------|------------------   | --------------|
| 0      | rideable_type       | object        |
| 1      | started_at          | datetime64[ns]|
| 1      | started_at          | datetime64[ns]|
| 2      | ended_at            | object        |
| 3      | member_casual       | object        |   
| 4      | ride_length         | float64       |
| 5      | day_number          | int64         |
| 6      | day_of_week         | object        |
| 7      | month               | object        |

dtypes: datetime64[ns] (2), float64(1), int64(1), object(4)

# Checking for null values

**df = combined_csv**

**df.isna().sum()**
|  |  |
|-------------|----|
|rideable_type|  0 |
|started_at   |  0 |
|ended_at     |  0 |
|member_casual|  0 |
|ride_length  |  0 | 
|day_number   |  0 |
|day_of_week  |  0 |
|month        |  0 |

dtype: int64

-Since, there is no null values in any of the columns, we don't have to delete any rows or columns.

-Thus, we can proceed with to our **analysis** stage now.









