import json
import jsonpath
import requests as rq

# url = 'https://reqres.in/api/users?page'
#
# response = rq.get(url)
#
# json_response = json.loads(response.text)
# print(json_response)
#
# pages = jsonpath.jsonpath(json_response, 'data[0].id')
# print(pages[0])

odics='{"a1":1,"a2":2}'
odi_json=json.loads(odics)
print(odi_json('a1'))