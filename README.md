# About
**This project contains a python script that fetches orgs from GSOC Orgs API and writes it to Excel. There might as well be a Projects API but I was intrested in Orgs and Identifing which Org is most likely to be in next GSOC.**

# Requirements
The requirement for exporting to Excel is:
```pip install openpyxl```

# Output
This is a single element from the excel that is generated.

|year|	name	|website_url|	tech_tags|	topic_tags|	categories|	ideas_list_url|	gsoc_url|
|--|--|--|--|--|--|--|--|
|2020|	52° North GmbH|	https://52north.org|	python, javascript, android, java, react|	web services, floating car data, ogc standards, trajectory analytics|	Science and medicine|	https://wiki.52north.org/Projects/GSoC2020ProjectIdeas|	https://summerofcode.withgoogle.com/programs/2020/organizations/6309633414660096|

![image](https://github.com/AdityaBavadekar/gsoc_data/assets/64344960/bdc5094c-b5f2-492a-a716-9b01981ca7dd)

Final data is extracted at : [final_workbook.html](/final_workbook.html)
This very very easy thanks to api that google provides.

> For exporting to other formats go to https://pandas.pydata.org/docs/reference/io.html and then do `Ctrl+F` and type "to_"

License: Free to use and modify for everyone.
