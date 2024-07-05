# BatteryReporter
 Windows Laptop에서 배터리 성능상태를 간편하게 확인할 수 있는 프로그램입니다.
 macOS에서는 GUI로 시스템 및 배터리 리포트를 확인할 수 있는데, Windows에서는 CMD로 리포트 파일을 생성해야 하는 등 macOS 대비 번거로움이 있다는 점을 착안하여 개발 진행하였습니다.  
 개선 사항에 대한 PR은 언제든지 환영하며, 문제가 발생했을 경우 Issue 탭에 남겨주시면 빠르게 확인 후 수정하도록 하겠습니다.  

## System Report Tab
 ![Battery Reporter 01](https://github.com/0x000613/BatteryReporter/assets/77450463/2236e1e7-2c32-449f-bd3e-0ab807ca955f)
 
 | COMPUTER NAME       | 컴퓨터명                                    |   
 |---------------------|-----------------------------------------|
 | SYSTEM PRODUCT NAME | 컴퓨터 제품 공식 모델명                           |
 | BIOS                | 메인보드 바이오스 버전                            |
 | OS BUILD            | 현재 사용중인 Windows OS 버전                   |
 | PLATFORM ROLE       | 컴퓨터 플랫폼 (랩탑 전용 프로세서일 경우 Mobile로 표기됨)    |
 | CONNECTED STANDBY   | CONNECTED STANDBY 지원 여부 (절전 전원 관리 탑재여부) |
 | REPORT TIME         | 리포트가 생성된 시간                             |   |

## Battery Report Tab
 ![Battery Reporter 02](https://github.com/0x000613/BatteryReporter/assets/77450463/b8d23f54-1ca7-430b-b4ed-191df132e253)
 
 | 항목명                        | 설명                                    |
 |----------------------------|---------------------------------------|
 | NAME                       | 배터리 모델명                               |
 | MANUFACTURER               | 제조업체                                  |
 | SERIAL NUMBER              | 제품 시리얼 넘버                             |
 | CHEMISTRY                  | 배터리 종류                                |
 | DESIGN CAPACITY            | 최초 생산 배터리 최대 용량                       |
 | FULL CHARGE CAPACITY       | 현재 배터리 최대 충전용량                        |
 | CYCLE COUNT                | 배터리 충전 사이클 횟수 (일부 모델에서 제공되지 않음)       |
 | BATTERY PERFORMANCE STATUS | 배터리 성능 상태 (최초생산 대비 현재 배터리 효율을 나타냅니다.) |
