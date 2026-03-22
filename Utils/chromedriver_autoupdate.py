import os
import sys
import traceback
from datetime import datetime
from zipfile import ZipFile

import requests
from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException, WebDriverException


class ChromedriverAutoupdate:
    def __init__(self, operatingSystem):
        self.__errKeyWord = '\nDetail:'
        if operatingSystem == "linux64":
            self.__driverZipName = "chromedriver_linux64.zip"
        elif operatingSystem == "mac64":
            self.__driverZipName = "chromedriver_mac64.zip"
        elif operatingSystem == "mac64_m1":
            self.__driverZipName = "chromedriver_mac64_m1.zip"
        elif operatingSystem == "win":
            self.__driverZipName = "chromedriver_win32.zip"
        else:
            print('err:operatingSystem should be win or mac64_m1 or mac64 or linux64, \
                such as \nchromedriver_autoupdate(operatingSystem = "win")')
            sys.exit(1)

    def check(self) -> str:
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--headless")

        try:
            print('chromedriver run')
            driver = webdriver.Chrome()
            driver.quit()
            return 'OK'
        except SessionNotCreatedException as e:
            print('SessionNotCreatedException chromedriver')
            f = e.msg.find('Current browser version is') + 27
            t = e.msg.find('with binary path') - 1
            os.remove('chromedriver.exe')
            status = self.__update_driver(e.msg[f:t])
            if self.__errKeyWord in status:
                return status
            else:
                return self.check()
        except WebDriverException as e:
            print('[Error] WebDriverException chromedriver')
            status = self.__update_driver('latest')
            if self.__errKeyWord in status:
                return status
            else:
                return self.check()
        except Exception as e:
            return self.__errLog(e)

    def __update_driver(self, version):
        url = 'https://chromedriver.chromium.org/downloads'
        v = 0

        try:
            re = requests.get(url).text
        except Exception as e:
            return self.__errLog(e)
        else:
            if version == 'latest':
                temp = re.find('If you are using Chrome version')
                v = re[temp:temp + 100].split('\n')[0].split(' ')[-1]
            else:
                temp_end = re.find(
                    f'Supports Chrome version {version.split(".")[0]}')
                temp_start = re[:temp_end].rfind('ChromeDriver')
                v = re[temp_start:temp_end].split('</strong>')[0].split(' ')[1]

            driver_url = f'https://chromedriver.storage.googleapis.com/{v}/{self.__driverZipName}'

            try:
                ref = requests.get(driver_url)
            except Exception as e:
                return self.__errLog(e)

            print('download_file ')
            download_file = 'driver.zip'
            with open(download_file, 'wb') as f:
                f.write(ref.content)
            ZipFile(download_file, 'r').extractall()
            os.remove(download_file)

        return 'OK'

    def __errLog(self, e):
        log_file_name = f'{datetime.now().strftime("%Y-%m-%d %H_%M_%S")}.log'
        with open(log_file_name, 'a', encoding='UTF-8') as f:
            traceback.print_exc(file=f)
        return f'{e}\nDetail: {log_file_name}'


if __name__ == '__main__':
    ChromedriverAutoupdate(operatingSystem="win").check()

