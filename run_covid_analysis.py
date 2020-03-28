import matplotlib.pyplot as plt
import pandas as pd


state_coverage_json_data_url = "https://covidtracking.com/api/states/daily"
us_county_cases_csv_url="https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
state_population_file = 'data/statepopulation.csv'

state_population_data = pd.read_csv(state_population_file)
us_county_cases_csv_data = pd.read_csv(us_county_cases_csv_url)
state_coverage_json_data = pd.read_json(state_coverage_json_data_url)

oregon_cases = []
for index, row in us_county_cases_csv_data.iterrows():
    if row['state']=='Oregon':
        oregon_cases.extend(row)

print (oregon_cases) 
hist = us_county_cases_csv_data.plot.hist(bins=12,alpha=0.5)
hist.plot()
plt.show()

