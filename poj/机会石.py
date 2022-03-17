import configparser
import re
import time
import win32con
import pyautogui
import pyperclip
import win32gui

conf = configparser.ConfigParser()
conf.read('data.ini')
pyautogui.FAILSAFE = True
# 装备位置
coordinate = 1322, 611
# 重铸石
reforgedStone = conf['coordinate']['reforgedStone'].split(',')
# 机会石
stoneOfOpportunity = conf['coordinate']['stoneOfOpportunity'].split(',')


def coordinate():
    for i in range(0, 5):
        for j in range(0, 2):
            coordinate_y = int(612 + 52.6 * i)
            coordinate_x = int(1322 + (52.6 * 2) * j)
            coordinates = coordinate_x, coordinate_y
            print(coordinate_x, coordinate_y)
            pyautogui.moveTo(coordinates, duration=0.1)
            pretend(coordinates)


class pretend():
    def __init__(self, coordinates):
        # self.affix = affix  # 必有词缀
        # self.secondaryAffix = secondaryAffix  # 可选词缀
        self.coordinates = coordinates
        self.data_li()

    def data_li(self):
        data = pyperclip.paste().replace('\r', '')
        rarity = re.findall('稀 有 度: (.*)', data)

        #
        # rarity = RE_FINDALL  # 匹配 装备的稀有度
        # rarity2 = re.findall(' (.*?)缀词缀', data)  # 匹配前缀后缀的数量
        if rarity:
            rarity = rarity[0]
            if rarity == '普通':
                pyautogui.moveTo(stoneOfOpportunity, duration=0.1)
                pyautogui.click(button='right')
                pyautogui.moveTo(self.coordinates, duration=0.1)
                pyautogui.click()
                print('机会石')
                # self.gettingInformation()
            elif rarity == '魔法':
                # if len(rarity2) == 1:
                pyautogui.moveTo(reforgedStone, duration=0.1)
                pyautogui.click(button='right')
                pyautogui.moveTo(self.coordinates, duration=0.1)
                pyautogui.click()
                print('重铸石')
                # self.gettingInformation()
            elif rarity == '稀有':
                pyautogui.moveTo(reforgedStone, duration=0.1)
                pyautogui.click(button='right')
                pyautogui.moveTo(self.coordinates, duration=0.1)
                pyautogui.click()
                print('重铸石')
                # self.gettingInformation()
            elif rarity == '传奇':
                print('完成了')
        else:
            time.sleep(1)
            print('没有数据')
            win = win32gui.FindWindow(u'POEWindowClass', None)
            # 将窗口调到前台
            win32gui.SetForegroundWindow(win)
            win32gui.ShowWindow(win, win32con.SW_SHOW)
            pyautogui.moveTo(self.coordinates, duration=0.1)
            pyautogui.hotkey('alt', 'ctrl', 'c')
            self.data_li()

    def gettingInformation(self):
        pyautogui.moveTo(self.coordinates, duration=0.1)
        pyautogui.hotkey('alt', 'ctrl', 'c')
        self.data_li()


if __name__ == '__main__':
    while True:
        if pyperclip.paste() != "":
            pyperclip.copy("")
            print("清理完成继续点击")
        else:
            coordinate()
