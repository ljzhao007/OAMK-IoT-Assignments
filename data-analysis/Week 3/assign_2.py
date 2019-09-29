import pandas as pd

data = pd.read_csv('adults.csv')


# How many men and women(sex feature) are represented in this dataset?​

print(data['sex'].value_counts())


# What is the average age(age feature) of women?

print(data[data['sex'] == 'Female']['age'].mean())


# What is the percentage of German citizens(native-country feature)?

print(float((data['native-country'] == 'Germany').sum()) / data.shape[0])


# What are the mean and standard deviation of age for those who earn more
# than 50K per year(salary feature) and those who earn less than 50K per year?

ages1 = data[data['salary'] == '>50K']['age']
ages2 = data[data['salary'] == '<=50K']['age']

ages1mean = round(ages1.mean())
ages1std = round(ages1.std(), 1)
ages2mean = round(ages2.mean())
ages2std = round(ages2.std(), 1)

print(
    F'The average age of the rich: {ages1mean} +- {ages1std} years, poor - {ages2mean} +- {ages2std} years.')


# Is it true that people who earn more than 50K have at least high school education?
# (education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters or Doctorate feature)

print(data[data['salary'] == '>50K']['education'].unique())
#
# No, it is not true.
# Output:
# ['HS-grad' 'Masters' 'Bachelors' 'Some-college' 'Assoc-voc' 'Doctorate'
#  'Prof-school' 'Assoc-acdm' '7th-8th' '12th' '10th' '11th' '9th' '5th-6th'
#  '1st-4th']
#


# Display age statistics for each race(race feature) and each gender(sex feature).
# Use groupby() and describe(). Find the maximum age of men of Amer-Indian-Eskimo race.

for (race, sex), racesex in data.groupby(['race', 'sex']):
    print(F'Race: {race}, sex: {sex}')
    print(racesex['age'].describe())


# Among whom is the proportion of those who earn a lot (> 50K) greater:
# married or single men (marital-status feature)?
# Consider as married those who have a marital-status starting with Married (Married-civ-spouse, Married-spouse-absent or Married-AF-spouse),
# the rest are considered bachelors.


unmarried_men = data[(data['sex'] == 'Male') & (data['marital-status'].isin(['Never-married',
                                                                             'Separated', 'Divorced']))]['salary'].value_counts()

print(unmarried_men)

married_men = data[(data['sex'] == 'Male') &
                   (data['marital-status'].str.startswith('Married'))]['salary'].value_counts()

print(married_men)

print(data['marital-status'].value_counts())


# What is the maximum number of hours a person works per week (hours-per-week feature)?
# How many people work such a number of hours, and what is the percentage of those who earn a lot (> 50K) among them?

max_hours = data['hours-per-week'].max()
print(F'Maximum hours - {max_hours} per week.')

nofHardWorkers = data[data['hours-per-week'] == max_hours].shape[0]
print(F'No. hard workers: {nofHardWorkers}')

richWorkers = float(data[(data['hours-per-week'] == max_hours)
                         & (data['salary'] == '>50K')].shape[0]) / nofHardWorkers
print(F'Rich percentage: {int(100 * richWorkers)}%')


# Count the average time of work(hours-per-week) for those who earn a little and a lot(salary)
# for each country(native-country). What will these be for Japan?

for (country, salary), grouped in data.groupby(['native-country', 'salary']):
    print(country, salary, round(grouped['hours-per-week'].mean(), 2))
