import json

import pytest
import requests

class Test_Post_Req:

    def test_create_new_resource(self):
        url = "https://reqres.in/api/users"
        file = open("/Users/maneshmohankadam/PycharmProjects/ApiAutomation/testcases/data.json", "r")
        f = file.read()
        jason_input = json.loads(f)
        print(jason_input)
        response = requests.post(url, jason_input)
        print(response.content)
<<<<<<< HEAD
        assert response.status_code == 201
=======
        assert response.status_code == 401
>>>>>>> 1265467 (second commit)
