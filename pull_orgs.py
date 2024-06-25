import requests
import json
import pandas as pd

BASE_URL = "https://summerofcode.withgoogle.com/api/archive/programs/{YEAR}/organizations/"
ALL_YEARS = list(range(2016, 2024))
GSOC_URL = 'https://summerofcode.withgoogle.com/programs/{year}/organizations/{slug}'

def parse_org(org):
    return org


def orgs(year:int):
    year = str(year)
    
    response = requests.get(BASE_URL.format(YEAR=year))
    
    if response.status_code == 200:
        print(f"Successfull Response:   '{year}/organizations'")
        return response.json()
    else:
        print(f"ERR! Failure Response:  '{year}/organizations'")
        return None

orgs_list = []
keys = [
    "name",
    "website_url",
    "tech_tags",
    "topic_tags",
    "categories",
    "ideas_list_url"
]
for y in ALL_YEARS:
    print(f'START: {y: ^25}')
    year_orgs = orgs(y)
    
    for i in range(len(year_orgs)):
        element = year_orgs[i]
        item = {'year':y}
        for k in keys:
            item[k] = element[k]  
            if isinstance(item[k], list):
                item[k] = ', '.join(item[k])

        item['gsoc_url'] = GSOC_URL.format(slug=element['slug'], year=y)
        orgs_list.append(item)
    print(f'END: {y: <25}')
    
print()
print('Working...')
pd.DataFrame(orgs_list).to_excel(f'final_workbook.xlsx')
print("Done.")