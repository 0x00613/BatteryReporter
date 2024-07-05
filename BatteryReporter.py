import os
import time
import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import webbrowser
import subprocess
from libs import calcModule

softwareVersion = '1.0.0beta'
softwareName = 'Battery Reporter'

# 배터리 리포트 생성 함수
def generateBatteryReport():
    # powercfg /batteryreport 명령을 실행하고 결과를 캡처
    process = subprocess.Popen(['powercfg', '/batteryreport'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
    output, error = process.communicate()

    # 결과 처리
    if error:
        print("Error:", error.decode('utf-8'))
    else:
        print("Battery report generated successfully.")

class BatteryMonitorApp:
    def __init__(self, root):
        self.root = root
        self.set_working_directory()
        self.root.title(softwareName + 'v' + softwareVersion)
        self.root.geometry("700x350")  # 창 크기 설정

        # Notebook 생성
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        # 첫 번째 탭 생성 (System Info)
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="System Report")

        # 두 번째 탭 생성 (Battery Info)
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Battery Report")

        # 첫 번째 탭 - 배터리 정보 표시를 위한 라벨과 Treeview 위젯
        self.label1 = ttk.Label(self.tab1, text="SYSTEM REPORT", font=("Helvetica", 14))
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.tree1 = ttk.Treeview(self.tab1, columns=("Label", "Value"), show="headings")
        self.tree1.heading("Label", text="Label")
        self.tree1.heading("Value", text="Value")
        self.tree1.column("Label", width=250)  # Label 열의 너비 설정
        self.tree1.column("Value", width=250)  # Value 열의 너비 설정
        self.tree1.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")  # 아래 여백 추가

        # 첫 번째 탭 - 배터리 정보 업데이트 버튼
        self.update_button1 = ttk.Button(self.tab1, text="Update Report", command=self.update_battery_info)
        self.update_button1.grid(row=2, column=0, padx=10, pady=10)

        # Developer 버튼 추가
        self.developer_button = ttk.Button(self.tab1, text="Developer", command=self.open_developer_website)
        self.developer_button.grid(row=2, column=1, padx=10, pady=10)

        # 두 번째 탭 - 배터리 정보 표시를 위한 라벨과 Treeview 위젯
        self.label2 = ttk.Label(self.tab2, text="BATTERY REPORT", font=("Helvetica", 14))
        self.label2.grid(row=0, column=0, padx=10, pady=10)

        self.tree2 = ttk.Treeview(self.tab2, columns=("Label", "Value"), show="headings")
        self.tree2.heading("Label", text="Label")
        self.tree2.heading("Value", text="Value")
        self.tree2.column("Label", width=250)  # Label 열의 너비 설정
        self.tree2.column("Value", width=250)  # Value 열의 너비 설정
        self.tree2.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")  # 아래 여백 추가

        # 두 번째 탭 - 배터리 정보 업데이트 버튼
        self.update_button2 = ttk.Button(self.tab2, text="Update Report", command=self.update_battery_info)
        self.update_button2.grid(row=2, column=0, padx=10, pady=10)

        # 배터리 정보 초기 업데이트
        self.update_battery_info()

        # 창 크기 변경 시 Treeview의 가로 스크롤바 동기화
        self.root.bind("<Configure>", self.sync_treeview_width)

    def set_working_directory(self):
        # 작업 디렉토리 확인
        documents_path = os.path.join(os.path.expanduser('~'), 'Documents', 'BatteryMonitor')

        # 디렉토리가 없는 경우 생성
        if not os.path.exists(documents_path):
            try:
                os.makedirs(documents_path)
                print("Directory created:", documents_path)
            except OSError as e:
                print("Failed to create directory:", e)
                return False

        # 작업 디렉토리 설정
        try:
            os.chdir(documents_path)
            print("Current working directory:", os.getcwd())
            return True
        except OSError as e:
            print("Failed to change working directory:", e)
            return False

    def update_battery_info(self):
        # 배터리 리포트 생성
        generateBatteryReport()

        # 1초 대기
        time.sleep(1)

        # HTML 파일 읽기
        with open('battery-report.html', 'r', encoding='utf-8') as f:
            html_content = f.read()

        # BeautifulSoup으로 HTML 파싱
        soup = BeautifulSoup(html_content, 'html.parser')

        # 첫 번째 탭 - 배터리 정보 테이블에서 데이터 추출하여 Treeview에 표시
        batteryReport = []
        battery_table1 = soup.find('table')
        if battery_table1:
            rows = battery_table1.find_all('tr')
            for row in rows:
                cells = row.find_all(['td', 'th'], recursive=False)
                if len(cells) == 2:
                    label = cells[0].text.strip()
                    value = cells[1].text.strip()
                    batteryReport.append((label, value))

        # Treeview 업데이트
        self.tree1.delete(*self.tree1.get_children())
        for item in batteryReport:
            self.tree1.insert("", "end", values=item)

        # 두 번째 탭 - 배터리 정보 테이블에서 데이터 추출하여 Treeview에 표시
        batteryReport = []
        battery_table2 = soup.select('body > table:nth-child(5)')[0]  # Selector 적용
        if battery_table2:
            rows = battery_table2.find_all('tr')
            for row in rows:
                cells = row.find_all(['td', 'th'], recursive=False)
                if len(cells) == 2:
                    label = cells[0].text.strip()
                    value = cells[1].text.strip()
                    batteryReport.append((label, value))

        # BATTERY PERFORMANCE STATUS (배터리 성능상태 계산 및 표기)
        batteryReport.append(("BATTERY PERFORMANCE STATUS", str(round(calcModule.extractNumbers(batteryReport[6][1]) / calcModule.extractNumbers(batteryReport[5][1]) * 100, 1)) + '%'))

        # Treeview 업데이트
        self.tree2.delete(*self.tree2.get_children())
        for item in batteryReport:
            self.tree2.insert("", "end", values=item)

    def sync_treeview_width(self, event):
        # 창 크기 변경 시 Treeview의 가로 스크롤바 동기화
        self.tree1.column("Label", width=(self.root.winfo_width() - 20) // 2)
        self.tree1.column("Value", width=(self.root.winfo_width() - 20) // 2)
        self.tree2.column("Label", width=(self.root.winfo_width() - 20) // 2)
        self.tree2.column("Value", width=(self.root.winfo_width() - 20) // 2)

    def open_developer_website(self):
        webbrowser.open_new("https://abyssventures.com")

if __name__ == "__main__":
    root = tk.Tk()
    app = BatteryMonitorApp(root)
    root.mainloop()
