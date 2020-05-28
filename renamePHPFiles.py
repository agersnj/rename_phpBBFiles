import json
import os

with open('/YourSQLResult') as json_file:
    data = json.load(json_file)

for file in data:
    try:
        os.rename(str(file['real_file']), str(file['file_name']))
    except Exception as e:
        print(e)
