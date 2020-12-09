import unittest
from app.main.service.id_service import check_id, check_structure, check_rule_Z, check_key_calculation

class TestCheckIdCases(unittest.TestCase):
    def test_id_structure_check(self):
        self.assertTrue(check_structure("A123456789") == 1)
        self.assertFalse(check_structure("A12345678") == 1)
        self.assertFalse(check_structure("Q123456789") == 1)

    def test_id_Z_rule_check(self):
        self.assertTrue(check_rule_Z('Z009999999') == 1)
        self.assertFalse(check_rule_Z('Z099999999') == 1)
        self.assertFalse(check_rule_Z('A009999999') == 1)

    def test_id_key_calculation_check(self):
        self.assertFalse(check_key_calculation('A123456789') == 0)
        self.assertTrue(check_key_calculation('J123456789') == 0)

    def test_id_check(self):
        good_api_response = check_id('J123456789')
        self.assertTrue(good_api_response == {
            "status":"success",
            "request":"J123456789",
            "result":1
        })
        bad_api_response = check_id('A123456789')
        self.assertTrue(bad_api_response == {
            "status":"failed",
            "request":"A123456789",
            "result":0
        })

        
if __name__ == '__main__':
    unittest.main()