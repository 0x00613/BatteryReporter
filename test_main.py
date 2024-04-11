import pytest
from unittest.mock import patch
from bs4 import BeautifulSoup
from app_file import generateBatteryReport, BatteryMonitorApp

# generateBatteryReport 함수 테스트
def test_generateBatteryReport():
    with patch('subprocess.Popen') as mock_popen:
        mock_process = mock_popen.return_value
        mock_process.communicate.return_value = (b'Some output', b'')

        generateBatteryReport()

        mock_popen.assert_called_once_with(['powercfg', '/batteryreport'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)

# update_battery_info 메서드 테스트
def test_update_battery_info():
    # 가짜 HTML 파일 생성
    fake_html_content = """
    <html>
        <body>
            <table>
                <tr><th>Label 1</th><td>Value 1</td></tr>
                <tr><th>Label 2</th><td>Value 2</td></tr>
            </table>
            <table>
                <tr><th>Label 3</th><td>Value 3</td></tr>
                <tr><th>Label 4</th><td>Value 4</td></tr>
            </table>
        </body>
    </html>
    """

    # 가짜 HTML 파일로 BeautifulSoup 객체 생성
    soup = BeautifulSoup(fake_html_content, 'html.parser')

    # 가짜 파일을 읽어올 때 사용할 mock_open 함수 정의
    def mock_open(*args, **kwargs):
        return fake_html_content

    # open 함수를 mock_open 함수로 대체
    with patch('builtins.open', mock_open):
        # BatteryMonitorApp 인스턴스 생성
        root = tk.Tk()
        app = BatteryMonitorApp(root)

        # update_battery_info 메서드 호출
        app.update_battery_info()

        # Treeview에 삽입된 아이템 확인
        assert app.tree1.get_children() == ('', '')
        assert app.tree2.get_children() == ('', '')

        # Treeview의 열 너비 확인
        assert app.tree1.column("Label")['width'] == 250
        assert app.tree1.column("Value")['width'] == 250
        assert app.tree2.column("Label")['width'] == 250
        assert app.tree2.column("Value")['width'] == 250