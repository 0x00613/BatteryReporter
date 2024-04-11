import unittest
from unittest.mock import patch, MagicMock
from main import generateBatteryReport

class TestGenerateBatteryReport(unittest.TestCase):
    @patch('main.subprocess.Popen')
    def test_generate_battery_report(self, mock_popen):
        # 모의 객체 생성
        mock_process = MagicMock()
        # Popen()이 반환할 모의 객체 설정
        mock_popen.return_value = mock_process

        # 테스트 대상 함수 호출
        generateBatteryReport()

        # 모의 객체 메서드 호출 확인
        mock_popen.assert_called_once_with(['powercfg', '/batteryreport'], stdout=mock_process.stdout, stderr=mock_process.stderr, creationflags=mock_process.creationflags)

if __name__ == '__main__':
    unittest.main()