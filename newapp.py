import pandas
import json
import utils.parse as parse
excel = pandas.read_excel('nou_task3.xlsx')

print(excel.head())

json_str = excel.to_json()
json_f = json.loads(json_str)
parse.parsing(json_f)



