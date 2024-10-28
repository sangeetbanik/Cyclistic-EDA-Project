--Here we perform the **Exploratory Data Analysis (EDA)** .

#Total rides in 2023 by diferent users
df_rider_group = df.groupby('member_casual').size().reset_index(name='count')
print(df_rider_group)
sns.countplot(x='member_casual'  , hue = 'member_casual', data=df, palette=sns.color_palette("colorblind",  n_colors=2))
plt.title('Distribution of Member and casual user types', fontsize=15)
plt.xlabel('User Type', fontsize=12)
plt.ylabel('Count', fontsize=12)

ax = plt.gca()
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2., height + 0.1,
            '{:1.0f}'.format(height), ha="center") 
plt.show()

#Types of bike and their distribution
print("Total rides in the year:", df["rideable_type"].count())
df_rides_grouped = df.groupby('rideable_type').size().reset_index(name='count')
print(df_rides_grouped)
sns.countplot(x='rideable_type', hue = 'rideable_type', data=df, palette=sns.color_palette("colorblind", n_colors=3))
plt.title('Distribution of vaious rideable types', fontsize=15)
plt.xlabel('Rideable Type', fontsize=12)
plt.ylabel('Count', fontsize=12)

ax = plt.gca()
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2., height + 0.1,
            '{:1.0f}'.format(height), ha="center") 
plt.show()

#Usage of different bikes by different users
sns.countplot(x='rideable_type', hue = 'member_casual', data=df, palette=sns.color_palette("colorblind", n_colors=2))
plt.title('Rideable Type distribution for Member and Casual user types',  fontsize=15)
plt.xlabel('User type',  fontsize=12)
plt.ylabel('Count',  fontsize=12)

ax = plt.gca()
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2., height + 0.1,
            '{:1.0f}'.format(height), ha="center") 
 
plt.legend(title='User Type', title_fontsize='13', loc='upper right')

plt.show()

#Weekly ride distribution
df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=
    ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday'],
    ordered=True)

df_day_grouped = df.groupby("day_of_week").size().reset_index(name='count')
print(df_day_grouped)

sns.countplot(x='day_of_week', hue='day_of_week', data=df, palette=sns.color_palette("colorblind", n_colors=7))
plt.title("Usage of cycle throughout the week", fontsize=15)
plt.xlabel(" days of week ", fontsize=12)
plt.ylabel("count", fontsize=12)



ax = plt.gca()
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2., height + 0.1,
            '{:1.0f}'.format(height), ha="center") 

plt.show()
sns.countplot(x='day_of_week', hue='member_casual', data=df, palette=sns.color_palette("colorblind", 2))

plt.title('Distribution of Rides by Day of the Week for Casual and Member Users', fontsize=15)
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Count', fontsize=12)

plt.legend(title='User Type', title_fontsize='13')

plt.show()

#Monthly ride distribution
df_month_grp = df.groupby('month').size().reset_index(name='count')
print(df_month_grp)

sns.countplot(x='month', hue='month', data=df, palette=sns.color_palette("colorblind",12))
plt.title('Distribution of Rides by months', fontsize=15)
plt.xlabel('months', fontsize=12)
plt.ylabel('Count', fontsize=12)

plt.show()

sns.countplot(x='month',hue='member_casual',data = df,palette=sns.color_palette('colorblind',2))
plt.title('Member vs Casual Distribution by Month', fontsize=15)
plt.xlabel('Months',fontsize=12)
plt.ylabel('Count',fontsize=12)
plt.legend(title = 'User type', title_fontsize=13, loc = 'upper right')

plt.show()

