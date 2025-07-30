import json

import jsonpath
import requests

url="https://reqres.in/api/users?page=2"

response=requests.get(url)
print(response.status_code)
print(response.headers.get('Server'))
print(response.cookies)
json_response= json.loads(response.content)
print(json_response)

a=jsonpath.jsonpath(json_response,'total_pages')
print(a[0])

for i in range(0,3):
    first_name=jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
    print(first_name)

# post request

