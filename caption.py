import os
import json

url = os.getenv('QUERY_STRING')
url = json.loads(url)
url = "https://" + url + "&fmt=json3"

print(url)

input()
