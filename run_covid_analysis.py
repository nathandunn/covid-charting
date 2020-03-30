import matplotlib.pyplot as plot
import pandas as pd

plot.close('all')
state_coverage_json_data_url = "https://covidtracking.com/api/states/daily"
us_county_cases_csv_url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
state_population_file = 'data/statepopulation.csv'

# LOAD the data
state_population_data = pd.read_csv(state_population_file)
us_county_cases_csv_data = pd.read_csv(us_county_cases_csv_url, parse_dates=True, header=0, index_col=0)
state_coverage_json_data = pd.read_json(state_coverage_json_data_url)


# FILTER for State
print('original shape')
print(us_county_cases_csv_data.head())

is_oregon = us_county_cases_csv_data['state'] == 'Oregon'
us_county_cases_csv_oregon = us_county_cases_csv_data[is_oregon]

print('oregon shape')
print(us_county_cases_csv_oregon.head())


# Convert to timeseries
df = us_county_cases_csv_oregon.groupby(us_county_cases_csv_oregon.county)
print(df.head())


ts = us_county_cases_csv_oregon.cumsum()

print('time series')
print(ts.head())
# print(ts)

print('#1')
# print(ts.date)
# print(ts.cases)
print('#1a')
# df = pd.DataFrame(ts.cases, index=ts.date)
pd.groupby(df.county)
df.head()

print('#2')
df = df.cumsum()
plot.figure()
df.plot()
# df.show()
plot.show()
print('#3')

# plot.figure()
# ts.plot()
# plot.show()
# pd.Series()
# hist = us_county_cases_csv_data.plot.hist(bins=12,alpha=0.5)
# hist.plot()
# hist = us_county_cases_csv_data.plot.
# plot.show()
