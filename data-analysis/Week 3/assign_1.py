import pandas as pd

data = pd.read_csv('data.csv')

# From given data set print first and last five rows

print(data.head(5))
print(data.tail(5))


# Find the most expensive car company name

company = data[['company', 'price']][data.price == data['price'].max()]
print(company)


# Print All Toyota Cars details

cars = data.groupby('company')
toyota = cars.get_group('toyota')
print(toyota)


# Count total cars per company

print(data['company'].value_counts())


# Find each company’s highest priced car

cars = data.groupby('company')
prices = cars['company', 'price'].max()
print(prices)


# Find the average mileage of each car making company

cars = data.groupby('company')
mileage = cars['company', 'average-mileage'].mean()
print(mileage)


# Sort all cars by Price column

cars = data.sort_values(['price'], ascending=False)
print(cars)
