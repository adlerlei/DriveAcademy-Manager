import unittest
from unittest.mock import MagicMock, patch
from ui.driving_test_roster import driving_test_roster, current_driving_test_number, save_student_data

class TestDrivingTestRoster(unittest.TestCase):
    def setUp(self):
        # 初始化測試環境
        self.content = MagicMock()
        driving_test_roster(self.content)

    @patch('ui.driving_test_roster.messagebox.showwarning')
    def test_increment_number_on_add(self, mock_showwarning):
        global current_driving_test_number

        # 模擬輸入學員資料
        self.content.student_number.get.return_value = '12345'
        self.content.student_name.get.return_value = '測試學員'
        self.content.register_number.get.return_value = '67890'
        self.content.national_id_no.get.return_value = 'A123456789'
        self.content.road_test_date.get.return_value = '2023-01-01'
        self.content.road_test_items_type.get.return_value = '1'
        self.content.driving_test_group.get.return_value = '1'
        self.content.batch.get.return_value = '1'

        # 呼叫新增學員資料的函數
        save_student_data()

        # 驗證號碼是否自動遞增
        self.assertEqual(current_driving_test_number, 1)

    @patch('ui.driving_test_roster.messagebox.showwarning')
    def test_no_increment_number_on_empty_add(self, mock_showwarning):
        global current_driving_test_number

        # 模擬未輸入學員資料
        self.content.student_number.get.return_value = ''
        self.content.student_name.get.return_value = ''
        self.content.register_number.get.return_value = ''
        self.content.national_id_no.get.return_value = ''
        self.content.road_test_date.get.return_value = ''
        self.content.road_test_items_type.get.return_value = ''
        self.content.driving_test_group.get.return_value = ''
        self.content.batch.get.return_value = ''

        # 呼叫新增學員資料的函數
        save_student_data()

        # 驗證號碼是否未遞增
        self.assertEqual(current_driving_test_number, 0)
        mock_showwarning.assert_called_once_with('警告', '請先搜尋學員資料！')

if __name__ == '__main__':
    unittest.main()