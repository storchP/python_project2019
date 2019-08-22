# coding: UTF-8

# MikuMikuWidget For MMD-CUP-ZERO2
# project name OpenWidget
# develop by storchP

import wx
import os
import webbrowser
import sys



sys.stdout = open(os.devnull, "w")


# URL LIST
url_1 ="https://ch.nicovideo.jp/BeamManP/blomaga/ar1668259"
url_2 ="https://www.nicovideo.jp/mylist/66007798"
url_3 ="https://www.nicovideo.jp/mylist/66007800"
url_4 ="https://www.nicovideo.jp/mylist/66007802"
url_5 ="http://angel-cup.ch2.cc/mz02_yo/"
url_6 ="http://angel-cup.ch2.cc/mz02/"
url_7 ="https://www.nicovideo.jp/tag/%E3%80%90MZ2%3A%E3%82%A2%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%80%91?sort=f&order=d"
url_8 ="https://www.nicovideo.jp/tag/%E3%80%90MZ2%3A%E3%83%89%E3%83%A9%E3%83%9E%E3%80%91?sort=f&order=d"
url_9 ="https://www.nicovideo.jp/tag/%E3%80%90MZ2%3A%E3%82%AE%E3%83%A3%E3%82%B0%E3%80%91?sort=f&order=d"
url_10 ="https://www.nicovideo.jp/tag/%E3%80%90MZ2%3A%E3%83%9F%E3%83%A5%E3%83%BC%E3%82%B8%E3%83%83%E3%82%AF%E3%83%93%E3%83%87%E3%82%AA%E3%80%91?sort=f&order=d"
url_11 ="https://www.nicovideo.jp/tag/%E3%80%90MZ2%3A%E3%81%9D%E3%81%AE%E4%BB%96%E3%80%91?sort=f&order=d"
url_12 ="https://www.nicovideo.jp/tag/%E3%80%90MZ2%E4%BA%88%3A%E3%82%A2%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%80%91?sort=f&order=d"
url_13 ="https://www.nicovideo.jp/tag/%E3%80%90MZ2%E4%BA%88%3A%E3%83%89%E3%83%A9%E3%83%9E%E3%80%91?sort=f&order=d"
url_14 ="https://www.nicovideo.jp/tag/%E3%80%90MZ2%E4%BA%88%3A%E3%82%AE%E3%83%A3%E3%82%B0%E3%80%91?sort=f&order=d"
url_15 ="https://www.nicovideo.jp/tag/%E3%80%90MZ2%E4%BA%88%3A%E3%83%9F%E3%83%A5%E3%83%BC%E3%82%B8%E3%83%83%E3%82%AF%E3%83%93%E3%83%87%E3%82%AA%E3%80%91?sort=f&order=d"
url_16 ="https://www.nicovideo.jp/tag/%E3%80%90MZ2%E4%BA%88%3A%E3%81%9D%E3%81%AE%E4%BB%96%E3%80%91?sort=f&order=d"
url_17 ="https://www.nicovideo.jp/tag/%e3%80%90MMD%e6%9d%afZERO2%e5%8f%82%e5%8a%a0%e5%8b%95%e7%94%bb%e3%80%91?sort=f&order=d"
url_18 ="https://tweetdeck.twitter.com/"

# URL展開
def click_button_1(event):
    webbrowser.open(url_1)

def click_button_2(event):
    webbrowser.open(url_2)

def click_button_3(event):
    webbrowser.open(url_3)

def click_button_4(event):
    webbrowser.open(url_4)

def click_button_5(event):
    webbrowser.open(url_5)

def click_button_6(event):
    webbrowser.open(url_6)

def click_button_7(event):
    webbrowser.open(url_7)

def click_button_8(event):
    webbrowser.open(url_8)

def click_button_9(event):
    webbrowser.open(url_9)

def click_button_10(event):
    webbrowser.open(url_10)

def click_button_11(event):
    webbrowser.open(url_11)

def click_button_12(event):
    webbrowser.open(url_12)

def click_button_13(event):
    webbrowser.open(url_13)

def click_button_14(event):
    webbrowser.open(url_14)

def click_button_15(event):
    webbrowser.open(url_15)

def click_button_16(event):
    webbrowser.open(url_16)

def click_button_17(event):
    webbrowser.open(url_17)

def click_button_18(event):
    webbrowser.open(url_18)

# 基礎処理
class Main(wx.Frame):
    def __init__(self, parent, id, title):
        # TITLE
        title = "MikuMikuWidget for MMD-CUP ZERO2　[Audience Edition]"
        message="\n\r\n\r MikuMikuWidget\n\r for MMD-CUP ZERO2\n\r [Audience Edition]"

        # パネル設定
        wx.Frame.__init__(self, parent, id, title, size=(510, 780), pos=(500, 50))
        panel = wx.Panel(self, wx.ID_ANY)
        # 背景色
        panel.SetBackgroundColour('#2b6a6b')

        # 文字色
        font_color = '#a1b3b3'

        # ボタン色
        button_color = '#2f4f4f'

        # ボタン設定
        button_1 = wx.Button(panel, wx.ID_ANY, 'ビームマンPの\n\rブロ☆マガ\r\nMMD杯ZERO2告知', size=(110, 110),  style=wx.BORDER_NONE)
        button_2 = wx.Button(panel, wx.ID_ANY, 'MMD杯ZERO2\n\r進行動画マイリスト', size=(110, 110), style=wx.BORDER_NONE)
        button_3 = wx.Button(panel, wx.ID_ANY, 'MMD杯ZERO2\n\r予告動画マイリスト', size=(110, 110), style=wx.BORDER_NONE)
        button_4 = wx.Button(panel, wx.ID_ANY, 'MMD杯ZERO2\n\r参加動画マイリスト', size=(110, 110), style=wx.BORDER_NONE)
        button_5 = wx.Button(panel, wx.ID_ANY, 'Angel-cup\n\rMMD杯ZERO2予告', size=(110, 110) ,  style=wx.BORDER_NONE)
        button_6 = wx.Button(panel, wx.ID_ANY, 'Angel-cup\n\rMMD杯ZERO2本番', size=(110, 110) ,  style=wx.BORDER_NONE)
        button_7 = wx.Button(panel, wx.ID_ANY, 'MZ2:アクション', size=(110, 110),  style=wx.BORDER_NONE)
        button_8 = wx.Button(panel, wx.ID_ANY, 'MZ2:ドラマ', size=(110, 110),  style=wx.BORDER_NONE)
        button_9 = wx.Button(panel, wx.ID_ANY, 'MZ2:ギャグ', size=(110, 110),  style=wx.BORDER_NONE)
        button_10 = wx.Button(panel, wx.ID_ANY, 'MZ2\n\rミュージックビデオ', size=(110, 110),  style=wx.BORDER_NONE)
        button_11 = wx.Button(panel, wx.ID_ANY, 'MZ2:その他', size=(110, 110),  style=wx.BORDER_NONE)
        button_12 = wx.Button(panel, wx.ID_ANY, 'MZ2予:アクション', size=(110, 110),  style=wx.BORDER_NONE)
        button_13 = wx.Button(panel, wx.ID_ANY, 'MZ2予:ドラマ', size=(110, 110),  style=wx.BORDER_NONE)
        button_14 = wx.Button(panel, wx.ID_ANY, 'MZ2予:ギャグ', size=(110, 110),  style=wx.BORDER_NONE)
        button_15 = wx.Button(panel, wx.ID_ANY, 'MZ2予\n\rミュージックビデオ', size=(110, 110),  style=wx.BORDER_NONE)
        button_16 = wx.Button(panel, wx.ID_ANY, 'MZ2予:その他', size=(110, 110),  style=wx.BORDER_NONE)
        button_17 = wx.Button(panel, wx.ID_ANY, 'MMD杯ZERO2\n\r参加動画', size=(110, 110),  style=wx.BORDER_NONE)
        button_18 = wx.Button(panel, wx.ID_ANY, 'TweetDeck', size=(110, 110),  style=wx.BORDER_NONE)
        text = wx.StaticText(panel, -1, message)

        # fontスタイル
        font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,  False, "メイリオ")
        button_1.SetFont(font)
        button_2.SetFont(font)
        button_3.SetFont(font)
        button_4.SetFont(font)
        button_5.SetFont(font)
        button_6.SetFont(font)
        button_7.SetFont(font)
        button_8.SetFont(font)
        button_9.SetFont(font)
        button_10.SetFont(font)
        button_11.SetFont(font)
        button_12.SetFont(font)
        button_13.SetFont(font)
        button_14.SetFont(font)
        button_15.SetFont(font)
        button_16.SetFont(font)
        button_17.SetFont(font)
        button_18.SetFont(font)
        text.SetFont(font)
        # ボタンカラー
        button_1.SetBackgroundColour(button_color)
        button_2.SetBackgroundColour(button_color)
        button_3.SetBackgroundColour(button_color)
        button_4.SetBackgroundColour(button_color)
        button_5.SetBackgroundColour(button_color)
        button_6.SetBackgroundColour(button_color)
        button_7.SetBackgroundColour(button_color)
        button_8.SetBackgroundColour(button_color)
        button_9.SetBackgroundColour(button_color)
        button_10.SetBackgroundColour(button_color)
        button_11.SetBackgroundColour(button_color)
        button_12.SetBackgroundColour(button_color)
        button_13.SetBackgroundColour(button_color)
        button_14.SetBackgroundColour(button_color)
        button_15.SetBackgroundColour(button_color)
        button_16.SetBackgroundColour(button_color)
        button_17.SetBackgroundColour(button_color)
        button_18.SetBackgroundColour(button_color)

        # ボタン文字色
        button_1.SetForegroundColour(font_color)
        button_2.SetForegroundColour(font_color)
        button_3.SetForegroundColour(font_color)
        button_4.SetForegroundColour(font_color)
        button_5.SetForegroundColour(font_color)
        button_6.SetForegroundColour(font_color)
        button_7.SetForegroundColour(font_color)
        button_8.SetForegroundColour(font_color)
        button_9.SetForegroundColour(font_color)
        button_10.SetForegroundColour(font_color)
        button_11.SetForegroundColour(font_color)
        button_12.SetForegroundColour(font_color)
        button_13.SetForegroundColour(font_color)
        button_14.SetForegroundColour(font_color)
        button_15.SetForegroundColour(font_color)
        button_16.SetForegroundColour(font_color)
        button_17.SetForegroundColour(font_color)
        button_18.SetForegroundColour(font_color)
        text.SetForegroundColour(font_color)
        # ボタンクリック時のバインド
        button_1.Bind(wx.EVT_LEFT_DOWN, click_button_1)
        button_2.Bind(wx.EVT_LEFT_DOWN, click_button_2)
        button_3.Bind(wx.EVT_LEFT_DOWN, click_button_3)
        button_4.Bind(wx.EVT_LEFT_DOWN, click_button_4)
        button_5.Bind(wx.EVT_LEFT_DOWN, click_button_5)
        button_6.Bind(wx.EVT_LEFT_DOWN, click_button_6)
        button_7.Bind(wx.EVT_LEFT_DOWN, click_button_7)
        button_8.Bind(wx.EVT_LEFT_DOWN, click_button_8)
        button_9.Bind(wx.EVT_LEFT_DOWN, click_button_9)
        button_10.Bind(wx.EVT_LEFT_DOWN, click_button_10)
        button_11.Bind(wx.EVT_LEFT_DOWN, click_button_11)
        button_12.Bind(wx.EVT_LEFT_DOWN, click_button_12)
        button_13.Bind(wx.EVT_LEFT_DOWN, click_button_13)
        button_14.Bind(wx.EVT_LEFT_DOWN, click_button_14)
        button_15.Bind(wx.EVT_LEFT_DOWN, click_button_15)
        button_16.Bind(wx.EVT_LEFT_DOWN, click_button_16)
        button_17.Bind(wx.EVT_LEFT_DOWN, click_button_17)
        button_18.Bind(wx.EVT_LEFT_DOWN, click_button_18)

        # パネルレイアウト
        layout = wx.GridSizer(rows=6, cols=4, gap=(1, 1))

        # パーツ配置
        layout.Add(button_1, flag=wx.SHAPED)
        layout.Add(button_2, flag=wx.SHAPED)
        layout.Add(button_3, flag=wx.SHAPED)
        layout.Add(button_4, flag=wx.SHAPED)
        layout.Add(button_5, flag=wx.SHAPED)
        layout.Add(button_6, flag=wx.SHAPED)
        layout.Add(button_17, flag=wx.SHAPED)
        layout.Add(button_18, flag=wx.SHAPED)
        layout.Add(button_12, flag=wx.SHAPED)
        layout.Add(button_13, flag=wx.SHAPED)
        layout.Add(button_14, flag=wx.SHAPED)
        layout.Add(button_15, flag=wx.SHAPED)
        layout.Add(button_16, flag=wx.SHAPED)
        layout.Add(button_7, flag=wx.SHAPED)
        layout.Add(button_8, flag=wx.SHAPED)
        layout.Add(button_9, flag=wx.SHAPED)
        layout.Add(button_10, flag=wx.SHAPED)
        layout.Add(button_11, flag=wx.SHAPED)
        layout.Add(text)
        # アイコン定義
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap("icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        # パネル表示
        panel.SetSizer(layout)
        self.Show(True)

# 画面表示
def main():
    app = wx.App()
    Main(None, wx.ID_ANY, "")
    app.MainLoop()
if __name__ == "__main__":
    main()