# Cyclistic Bike Share Project

## 📝 Introduction 
The **Cyclistic** is a fictional company that launched a bike-sharing program. In this project, as a junior data analyst, working on the marketing analyst team at Cyclistic, I will follow the data analysis process like: <ins>ask, prepare, process, analyze, share and act</ins> to analyze the data. 

## 💬 Background
Cyclistic is a bike-share company based in Chicago that launched its bike-sharing initiative in 2016. Since then, it has grown to include 5,824 bicycles and 692 geotracked stations distributed throughout the city. The system allows customers to rent bikes at one station and return them at any other, making it a convenient transportation option. This ease of use has helped Cyclistic's bike-sharing service become popular.

Cyclistic’s marketing efforts have mainly concentrated on raising general awareness and targeting a broad audience. The company offers flexible pricing models to accommodate different user needs, including single-ride tickets, day passes (collectively referred as <b>casual riders</b>), and yearly memberships(<b> referred as Cyclistic members</b>). Additionally, Cyclistic provides special bike options like reclining bikes, hand tricycles, and cargo bikes, making the service accessible to people with disabilities and those unable to use traditional two-wheeled bicycles. 

The marketing director believes the company's success will depend on increasing the number of annual memberships. As part of the junior data analysis team, my role is to study the differences between casual riders and annual members to develop a marketing strategy aimed at converting more casual riders into members.


## ⚙ Approach/Steps
### 1. Ask
**Business Task -** design marketing strategies to **convert casual riders to members** by understanding how annual and casual riders differ, why casual riders would buy a membership, and how digital media could affect their marketing tactics.<br>

> Questions for guiding future marketing program: 
> 1. How do annual members and casual riders use Cyclistic bikes differently?
> 2. Why would casual riders buy Cyclistic annual memberships?
> 3. How can Cyclistic use digital media to influence casual riders to become members?

As a junior data analyst, my focus is on answering the first question: <b>How do annual members and casual riders use Cyclistic bikes differently?</b>

### 2. Prepare
#### 🔗 Quick Links
**Data Source:** [divvy-tripdata](https://divvy-tripdata.s3.amazonaws.com/index.html) <br>
[Note that the data has been made available by Motivate International Inc. under this [<ins>license</ins>](https://www.divvybikes.com/data-license-agreement).]

**Tools:** <br>
- Data pre-processing - Excel.
- Data cleaning & combining - Python.
- Exploratory Data analysis - Python
- Data visualization - [Tableau](https://public.tableau.com/app/profile/sangeet.banik/viz/CyclisticProject_17298545186540/Dashboard1)

### 3. Process
The basis for this analysis is **2023** data and the steps for processing the data are as follow:
1) [Data Pre-processing](https://github.com/sangeetbanik/sangeetbanik.github.io/blob/main/1_Pre-processsing%20on%20excel.md)
2) [Data combination](https://github.com/sangeetbanik/sangeetbanik.github.io/blob/main/2_Data_combination.py)
3) [Data cleaning](https://github.com/sangeetbanik/sangeetbanik.github.io/blob/main/3_Data_cleaning.md)
4) [Exploratory_Data Analysis](https://github.com/sangeetbanik/sangeetbanik.github.io/blob/main/4_EDA.py)

#### Data Combining
The 12 tables from **January 2023 to December 2023** were stacked and combined into a single table. The table consists of 5,719,877 rows.

#### Data Exploration
My initial step was to check the individual tables one by one using Excel to determine the **data type** and to  uncover any **missing values, outliers, inconsistencies, and errors** within the tables. 

The data set consists of **13 variables**, as shown in the following: <br>

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

#### Data Cleaning
Before analyzing the data, the dataset was cleaned by:
- Removing the trips with **null values**.
- Removing 9 columns: '**ride_id**', '**start_station_name**', '**end_station_name**', '**start_station_id**', '**end_station_id**', '**start_lat**', '**start_lng**', '**end_lat**', and '**end_lng**'.
- Adding 3 columns: '**ride_length_in_mins**', '**day_of_week**' and '**month**'.
In a later satge of analyzing the data, due to inconsistency, we:
- Excluded the **rides with duration less than a minute** or **longer than a day**.

In total, 5,702,878 rows were returned, which means 16,999 rows were removed

### 4. Analyze
#### Data Analysis
The analysis question is: 
> How do annual members and casual riders use Cyclistic bikes differently?

The cleaned data is imported into Tableau for analysis and the figures plotted are displayed in the following.

### - Total Rides in 2023
The figure below shows the **total number of rides** carried out by Cyclistic members and casual riders in **2023**. 

![Membership Types](https://github.com/user-attachments/assets/75074177-ec8a-41f6-a268-771ce82230d8)

- **Cyclistic members** recorded a **greater bicycle activity** than casual riders. The total rides for Cyclistic members are 3,655,271 while 2,047,607 trips for casual riders. 
- **Cyclistic members** accounted for about **64.09%** of total rides whereas casual riders made up **35.91%** of total rides in 2023. 
<br>

### - Types of Bikes
The types of bicycles used for the trips are displayed as follow:

![Types of Bikes](https://github.com/user-attachments/assets/ae114b65-47d0-4382-a7b8-b8b0ef7756d0)
![Usage of bike](https://github.com/user-attachments/assets/85fb393c-4ba1-4643-8740-52e3675653c7)


- There are **three types of bicycles**: <ins>*classic, electric and docked bikes*</ins>.
- Cyclistic members and casual riders prefer show a higher preference for **classic bicycles over electric bicycles**.
- Casual riders have also used the docked bicycles. 
<br>

### - Average Ride Duration
The average ride length is plotted against the type of users (member vs. casual):

![Avg Ride Length (Year)](https://github.com/user-attachments/assets/33fa19b3-1cee-48b4-bad1-0b95920e5e56)


- **Cyclistic members** can ride on the bicycles for about **11.936 minutes** on average whereas **casual riders** have an average ride length of **20.079 minutes**. Hence, the ride duration of Cyclistic members are approximately two times smaller than casual riders.
<br>

### - Trips Taken in a Month
The preference of cycling activity can be determined by drawing the graph of trips taken against month from January to December 2023. 

![Total Rides (Month)](https://github.com/user-attachments/assets/9885d609-25c9-483f-9b26-9c74a1b2b332)


- The **lowest activity** observed for Cyclistic members was 147,279 rides in **February 2023** and for casual riders was 39,867 rides in **January 2023**.
- **Cyclistic members** have the **highest activity** (459,640 rides) in **August 2023**.
- **Casual riders** have the **highest activity** (329,363 rides) in **July 2023**.
<br>

### - Average Ride Length in a Month
The mean trip duration is depicted in the line graph below. 

![Avg  Ride Length (Month)](https://github.com/user-attachments/assets/0764018a-ecb7-4e46-ba8c-aa6d7d5bb3ff)

- The monthly average ride duration for **Cyclistic members** is the **highest** in **July** (13.08 minutes).
- For **casual riders**, the **highest** mean trip duration is in **July** (22.31 minutes).
<br>

### - Trips Taken in a Week
The bar chart below is used to study the daily user activity over a week.

![Total Rides (Week)](https://github.com/user-attachments/assets/af09497e-072d-4a97-8988-a81d6394b4ab)

- Generally, bike rides are **most frequented** on **Saturdays**, with a total trips of 883,566 trips. 
- **Cyclistic members** have the **highest activity** (588,795 rides) on **Thursdays** while the **lowest activity** (408,277 rides) on **Sundays**.
- **Casual riders** have the **greatest activity** (407,880 rides) on **Saturdays** while the **least activity** (233,678 rides) on **Mondays**.
<br>

### - Average Ride Length in a Week
The mean ride duration across the week is displayed as follow.

![Avg  Ride Length (Week)](https://github.com/user-attachments/assets/0ac09cba-19f6-4e97-8365-19f49ac59015)

- **Cyclistic members** cycled the **longest on Sunday** with an average ride length of 13.31 minutes.
- On the other hand, **casual riders cycled the longest on Sunday** with a mean trip duration of 23.50 minutes. 

### 5. Share
![Cyclistic Bike Share Dashboard](https://github.com/user-attachments/assets/6a765359-d29f-41a5-bcd3-523086d5a967)


View [Cyclistic Bike Share Dashboard](https://public.tableau.com/app/profile/sangeet.banik/viz/CyclisticProject_17298545186540/Dashboard1).

The similiarities and differences between Cyclistic members and casual riders were drawn from the dashboard above.

**Similarities:**
- Both Cyclistic members and casual riders **prefer riding bicycles in the spring and summer seasons** (from May to September). However, the number of rides decrease since September. This may be due to change of season in which the weather temperature drops and becomes uncomfortable for rides. 
- Both Cyclistic members and casual riders **prefer classic bicycles over electric bicycles**. 
- Both Cyclistic members and casual riders have **higher average ride duration on weekends as compared to on weekdays**.

**Differences:**
- **Cyclistic members** go on **more rides** than casual riders.
- **Cyclistic members** have **smaller average ride length** (12.01 minutes) than casual riders (19.72 minutes). Hence, this may suggest that the Cyclistic members take the bicycles for **short trips or short distance travel**. 
- **Cyclistic members** show **consistent rides** throughout the week while casual riders have the busiest activites on weekends and lowest activities during weekdays. This may indicate that the Cyclistic members use the bicycles for ***purpose-oriented rides** such as work or errands while the casual riders use bicycles for leisure or recreational activities.  

### 6. Act
#### <ins>Recommendations</ins>
From the analysis above, we can design marketing strategies to convert casual riders to Cyclistic members. Here are my suggested approach:

- **Free Trial Periods** <br>
Offer casual riders a limited-time free trial of the annual membership benefits. This lets them experience the advantages, such as unlimited rides or discounted pricing, and could motivate them to convert to paying members after the trial.

- **Personalized Promotions** <br>
Send targeted offers and discounts to casual riders based on their riding behavior. For instance, after completing a certain number of rides, they could receive a discount toward an annual membership, making the transition appealing.

- **Loyalty Program** <br>
Establish a loyalty rewards program where members earn points for every ride. Points can be redeemed for rewards such as discounts on future memberships, motivating frequent usage and enhancing customer retention.

- **Membership Personalisation** <br>
Provide various membership tiers such as annual, monthly, and daily plans. For instance, pricing could be set at $365 per year, $45 per month, and $3 per day. This flexibility allows users to select a plan that best suits their needs. Offering shorter-term memberships with tailored pricing can attract riders who may not require a full-year commitment.

- **Group Membership Discounts** <br>
Offer discounted plans for friends, students, and families can encourage collective memberships. Furthermore, it encourages users to cycle together and strengthen the bonds between people.

- **Exclusive Member Events** <br>
Host special events exclusively for members, such as group cycling tours, urban adventure challenges, or themed rides. This provides members with unique experiences, while also encouraging casual riders to upgrade to membership status.

- **Seasonal promotions** <br>
Run seasonal campaigns offering limited-time deals, weekday specials, or extended ride durations for members. These campaigns can help sustain membership growth and optimize service use during different times of the year.

- **Social Media interactions** <br>
Leverage social media platforms to engage with both casual riders and potential members. Share member success stories, testimonials, and user-generated content. Visually appealing posts highlighting the joy of cycling in various seasons can encourage casual riders to convert to members.


## 🔮 Conclusion
In short, this analysis provides valuable insights into the preferences and behaviors of Cyclistic members and casual riders. By tailoring strategies to the identified differences and preferences, Cyclistic can effectively convert casual riders into portential cyclistic members.
