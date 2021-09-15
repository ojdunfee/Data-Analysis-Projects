```python
import pandas as pd
```


```python
df = pd.read_csv('adult.data.csv')

race_count = df['race'].value_counts()

average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), ndigits=1)

percentage_bachelors = round(((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100), ndigits=1)

higher_education = df[df['education'].isin(['Bachelors','Masters','Doctorate'])]

lower_education = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]

higher_education_rich = round(((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100), ndigits=1)
lower_education_rich = round(((lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100), ndigits=1)

min_work_hours = df['hours-per-week'].min()

num_min_workers = df[df['hours-per-week'] == min_work_hours]

rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0] * 100), ndigits=1)

people = df['native-country'].value_counts()
rich = df[df['salary'] == '>50K']['native-country'].value_counts()
highest_earning_country = (rich / people).sort_values(ascending=False).keys()[0]

people_in_highest = df[df['native-country'] == highest_earning_country]
rich_in_highest = people_in_highest[people_in_highest['salary'] == '>50K']
highest_earning_country_percentage = round((rich_in_highest.shape[0] / people_in_highest.shape[0] * 100), ndigits=1)

top_IN_occupation = df[df['salary'] == '>50K']
top_IN_occupation = top_IN_occupation[top_IN_occupation['native-country'] == 'India']
top_IN_occupation = top_IN_occupation['occupation'].value_counts()._index[0]

print("Number of each race:\n", race_count) 
print("Average age of men:", average_age_men)
print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
print(f"Min work time: {min_work_hours} hours/week")
print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
print("Country with highest percentage of rich:", highest_earning_country)
print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
print("Top occupations in India:", top_IN_occupation)

```

    Number of each race:
     White                 27816
    Black                  3124
    Asian-Pac-Islander     1039
    Amer-Indian-Eskimo      311
    Other                   271
    Name: race, dtype: int64
    Average age of men: 39.4
    Percentage with Bachelors degrees: 16.4%
    Percentage with higher education that earn >50K: 46.5%
    Percentage without higher education that earn >50K: 17.4%
    Min work time: 1 hours/week
    Percentage of rich among those who work fewest hours: 10.0%
    Country with highest percentage of rich: Iran
    Highest percentage of rich people in country: 41.9%
    Top occupations in India: Prof-specialty

