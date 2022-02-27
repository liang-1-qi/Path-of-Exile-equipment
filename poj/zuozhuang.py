import tkinter as tk  
import pyautogui
import pyperclip
import re
import time
import configparser
import win32con
import win32gui


conf = configparser.ConfigParser()
conf.read('data.ini')
pyautogui.FAILSAFE = True
# 装备位置
coordinate = conf['coordinate']['coordinate_1'].split(',')

# 蜕变石
metamorphosisStone = conf['coordinate']['metamorphosisStone'].split(',')

# 增幅石
amplifierStone = conf['coordinate']['amplifierStone'].split(',')

# 改造石
transformationStone = conf['coordinate']['transformationStone'].split(',')
# 重铸石
reforgedStone = conf['coordinate']['reforgedStone'].split(',')
# 富豪石
regalStone = conf['coordinate']['regalStone'].split(',')

window = tk.Tk()
window.title('清安的自动做装小工具 1.2.0')
tk.Label(window, text='需求词缀 :', font=('Arial', 12), ).place(x=280, y=20)
tk.Label(window, text='可选词缀 :', font=('Arial', 12), ).place(x=280, y=50)
sw = window.winfo_screenwidth()  # 得到屏幕宽度
sh = window.winfo_screenheight()  # 得到屏幕高度
ww = 600
wh = 400
x = (sw - ww) / 2
y = (sh - wh) / 2
window.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
#  词缀框
entry1 = tk.Entry(window, show=None, font=('Arial', 14))
entry1.place(x=360, y=20)  # 显示成明文形式
entry2 = tk.Entry(window, show=None, font=('Arial', 14))
entry2.place(x=360, y=50)


def lihai():
    pretend(entry1.get(), entry2.get())
    time.sleep(1)
    if pyperclip.paste() != "":
        pyperclip.copy("")
        print("清理完成继续点击")


class pretend():
    def __init__(self, affix, secondaryAffix):
        self.affix = affix  # 必有词缀
        self.secondaryAffix = secondaryAffix  # 可选词缀
        self.data_li()

    def data_li(self):
        data = pyperclip.paste().replace('\r', '')
        rarity = re.findall('稀 有 度: (.*)', data)

        #
        # rarity = RE_FINDALL  # 匹配 装备的稀有度
        rarity2 = re.findall(' (.*?)缀词缀', data)  # 匹配前缀后缀的数量
        if rarity:
            rarity = rarity[0]
            if rarity == '普通':
                pyautogui.moveTo(metamorphosisStone, duration=0.1)
                pyautogui.click(button='right')
                pyautogui.moveTo(coordinate, duration=0.1)
                pyautogui.click()
                print('蜕变石')
                self.gettingInformation()
            elif rarity == '魔法':
                if len(rarity2) == 1:
                    pyautogui.moveTo(amplifierStone, duration=0.1)
                    pyautogui.click(button='right')
                    pyautogui.moveTo(coordinate, duration=0.1)
                    pyautogui.click()
                    print('增幅石')
                    self.gettingInformation()
                elif len(rarity2) == 2:
                    if self.affix != "" and self.secondaryAffix != "":
                        if self.affix in data or self.secondaryAffix in data:
                            pyautogui.moveTo(regalStone, duration=0.1)
                            pyautogui.click(button='right')
                            pyautogui.moveTo(coordinate, duration=0.1)
                            pyautogui.click()
                            print('富豪石')
                            self.gettingInformation()
                        else:
                            pyautogui.moveTo(transformationStone, duration=0.1)
                            pyautogui.click(button='right')
                            pyautogui.moveTo(coordinate, duration=0.1)
                            pyautogui.click()
                            print('改造石')
                            self.gettingInformation()

            elif rarity == '稀有':
                if len(rarity2) >= 3:

                    if self.affix in data and self.secondaryAffix in data:
                        print('装备完成了')
                        # win32clipboard.EmptyClipboard()
                    else:
                        pyautogui.moveTo(reforgedStone, duration=0.1)
                        pyautogui.click(button='right')
                        pyautogui.moveTo(coordinate, duration=0.1)
                        pyautogui.click()
                        print('重铸石')
                        self.gettingInformation()
        else:
            print('没有数据')
            time.sleep(1)
            win = win32gui.FindWindow(u'POEWindowClass', None)
            # 将窗口调到前台
            win32gui.SetForegroundWindow(win)
            win32gui.ShowWindow(win, win32con.SW_SHOW)
            pyautogui.moveTo(coordinate, duration=0.1)
            pyautogui.hotkey('alt', 'ctrl', 'c')
            self.data_li()

    def gettingInformation(self):
        pyautogui.moveTo(coordinate, duration=0.1)
        pyautogui.hotkey('alt', 'ctrl', 'c')
        self.data_li()


def guanbi_1():
    window.quit()


tk.Label(window, text="""# 装备位置\n
coordinate_1 =装备位置\n
# 蜕变石\n
metamorphosisStone = 蜕变石位置\n
# 增幅石\n
 amplifierStone= 增幅石位置\n
# 改造石\n
transformationStone = 改造石位置\n
# 重铸石\n
reforgedStone = 重铸石位置\n
# 富豪石\n
regalStone =  富豪石位置""", bg='yellow', font=('Arial', 10), width=30,
         height=30).pack(side='left')
tk.Button(window, text='开始', font=('Arial', 12), width=10, height=1, command=lihai). \
    place(x=400, y=200)
window.mainloop()