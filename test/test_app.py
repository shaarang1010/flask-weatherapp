import unittest
from app import app as tested_app
from app import get_weather_data
from flask_api import status


class FlaskAppTests(unittest.TestCase):
    
    def test_get_weather_endpoint(self):
        # test to check if endpoint returns 200 status code
        print(self._testMethodName)
        tester = tested_app.test_client(self)
        r = tester.get('/')
        self.assertTrue(status.is_success(r.status_code))

    def test_get_city_weather(self):
        # test to check if receiving all weather data for the city
        print(self._testMethodName)
        print('Testing for Melbourne')
        expected_response = get_weather_data('Melbourne')
        self.assertEqual(13, len(expected_response))


if __name__ == '__main__':
    unittest.main()