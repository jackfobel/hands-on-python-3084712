import requests
from pprint import pprint

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20]

#pprint(last_twenty_years)

for year in last_twenty_years:              # // is floor division which means discard remainder (5 // 2 = 2)
    display_width = year["value"] // 10_000_000                     # 10_000_000 just makes it more readible, still a number
    #print(year["date"], "=" * display_width)                       #
    print(f'{year["date"]}: {year["value"]}', "=" * display_width)  # interpolation 'f'
                                                                    # multiply the = times the dsiplay width value. prints =======