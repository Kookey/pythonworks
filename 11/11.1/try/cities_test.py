from city import formatted_city
import unittest


class CityTestCase(unittest.TestCase):
    """测试城市"""
    def test_city(self):
        name = formatted_city('sh', 'china')
        self.assertEqual(name, 'Sh China')

    def test_city_population(self):
        name = formatted_city('sh', 'china', '50000')
        self.assertEqual(name, 'Sh China - Population 50000')

unittest.main()
