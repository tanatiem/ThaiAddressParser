import unittest
from unittest.mock import patch
import ThaiAddressParser

class TestThaiAddressParser(unittest.TestCase):
    def setUp(self):
        self.parser = ThaiAddressParser

    def test_parse_bangkok_address(self):
        address = "123 ถนนเพชรบุรีตัดใหม่ แขวงบางกะปิ เขตห้วยขวาง กรุงเทพมหานคร 10310"
        expected_result = {
            'original_address': '123 ถนนเพชรบุรีตัดใหม่ แขวงบางกะปิ เขตห้วยขวาง กรุงเทพมหานคร 10310',
            'parsed_address': '123 ถนนเพชรบุรีตัดใหม่ บางกะปิ ห้วยขวาง กรุงเทพมหานคร',
            'province': {'thai': 'กรุงเทพมหานคร', 'en': 'Bangkok'},
            'district': {'thai': 'ห้วยขวาง', 'en': 'Khet Huai Khwang'},
            'sub_district': {'thai': 'บางกะปิ', 'en': 'Khet Bang Kapi'},
            'remaining_address': '123 ถนนเพชรบุรีตัดใหม่'
        }

        result = self.parser.parse(address)

        self.assertEqual(result['parsed_address'],
                         expected_result['parsed_address'])
        self.assertEqual(result['province'], expected_result['province'])
        self.assertEqual(result['district'], expected_result['district'])
        self.assertEqual(result['sub_district'],
                         expected_result['sub_district'])
        self.assertEqual(result['remaining_address'],
                         expected_result['remaining_address'])

    def test_parse_non_bangkok_address(self):
        address = "456 ตำบลแสนสุข อำเภอเมือง จังหวัดนครราชสีมา 30000"
        expected_result = {
            'original_address': '456 ตำบลแสนสุข อำเภอเมือง จังหวัดนครราชสีมา 30000',
            'parsed_address': '456 ต.โนนอุดม อ.เมืองยาง จ.นครราชสีมา',
            'province': {'thai': 'นครราชสีมา', 'en': 'Nakhon Ratchasima'},
            'district': {'thai': 'เมืองยาง', 'en': 'Mueang Yang'},
            'sub_district': {'thai': 'โนนอุดม', 'en': 'Non Udom'},
            'remaining_address': '456'
        }

        result = self.parser.parse(address)

        self.assertEqual(result['parsed_address'],
                         expected_result['parsed_address'])
        self.assertEqual(result['province'], expected_result['province'])
        self.assertEqual(result['district'], expected_result['district'])
        self.assertEqual(result['sub_district'],
                         expected_result['sub_district'])
        self.assertEqual(result['remaining_address'],
                         expected_result['remaining_address'])

    def test_parse_address_with_multiple_spaces(self):
        address = "   1    2   3   ถนน  ราชดำเนิน  แขวง ท่าพระ  เขต พระนคร กรุงเทพมหานคร"
        expected_result = {
            'original_address': '   1    2   3   ถนน  ราชดำเนิน  แขวง ท่าพระ  เขต พระนคร กรุงเทพมหานคร',
            'parsed_address': '1 2 3 ถนน ราชดำเนิน แขวง ท่าพระ ตลาดยอด พระนคร กรุงเทพมหานคร',
            'province': {'thai': 'กรุงเทพมหานคร', 'en': 'Bangkok'},
            'district': {'thai': 'พระนคร', 'en': 'Khet Phra Nakhon'},
            'sub_district': {'thai': 'ตลาดยอด', 'en': 'Talat Yot'},
            'remaining_address': '1 2 3 ถนน ราชดำเนิน แขวง ท่าพระ'
        }

        result = self.parser.parse(address)
        

        self.assertEqual(result['parsed_address'],
                         expected_result['parsed_address'])
        self.assertEqual(result['province'], expected_result['province'])
        self.assertEqual(result['district'], expected_result['district'])
        self.assertEqual(result['sub_district'],
                         expected_result['sub_district'])
        self.assertEqual(result['remaining_address'],
                         expected_result['remaining_address'])

    def test_parse_invalid_address(self):
        address = "Invalid address"
        with self.assertRaises(Exception):
            self.parser.parse(address)

    
    def test_set_download_path(self):
        json_file_path = 'test_path.json'
        translation_db = 'th_en_db.json'

        self.parser.set_download_path(json_file_path, translation_db)

        self.assertEqual(self.parser.get_file_path(), 'test_path.json')

if __name__ == '__main__':
    unittest.main()
