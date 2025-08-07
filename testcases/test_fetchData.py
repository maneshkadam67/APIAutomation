import pytest
import requests
import json
import jsonpath
import softest
from softest import TestCase
<<<<<<< HEAD
class Test_FetchAPIData(softest.TestCase):
=======
class FetchAPIData(softest.TestCase):
>>>>>>> 1265467 (second commit)
    url="https://reqres.in/api/users?page=2"
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_fetch_data(self):
        global response
        response=requests.get(self.url)
        print(response.status_code)
        assert response.status_code==200
        # self.soft_assert(self.assertEqual, response.status_code, 200, "Status code should be 200")
        # self.soft_assert(self.assertNotEqual, response.status_code, 201, "Status code should not be 201")
        # self.assert_all()
<<<<<<< HEAD

=======
>>>>>>> 1265467 (second commit)
    @pytest.mark.sanity
    def test_specific_data(self):
        json_response = json.loads(response.content)
        #print(json_response)
        a = jsonpath.jsonpath(json_response, 'total_pages')
        assert a[0]==2

    def test_get_first_name(self):
        json_response = json.loads(response.content)
        for i in range(0, 3):
            first_name = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
            print(first_name)









