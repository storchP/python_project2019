# coding: UTF-8

# Master widget
# project name OpenWidget
# develop by storchP

import wx
import os
import webbrowser
import sys

sys.stdout = open(os.devnull, "w")


# URL LIST
url_1 = "https://idolmaster.jp/"
url_2 = "https://columbia.jp/idolmaster/"
url_3 = "https://www.lantis.jp/imas/"
url_4 = "https://www.lantis.jp/sidem/"
url_5 = "http://imas-db.jp/"
url_6 = "http://imasnews765.com/"
url_7 = "https://ch.nicovideo.jp/dereradi"
url_8 = "https://ch.nicovideo.jp/cinderellaparty"
url_9 = "https://ch.nicovideo.jp/imas-music"
url_10 = "https://ch.nicovideo.jp/MillionRADIO"
url_11 = "https://ch.nicovideo.jp/sidem"
url_12 = "https://www.youtube.com/user/nbgi/videos"
url_13 ="https://www.jalan.net/"
url_14 ="https://www.trivago.jp/"
url_15 ="https://www.nta.co.jp/"
url_16 ="https://www.bushikaku.net/"
url_17 ="https://www.skyscanner.jp/"
url_18 ="https://www.eki-net.com/top/index.html"
url_19 ="https://www.hotpepper.jp/"
url_20 ="https://shop.asobistore.jp/"
url_21 ="https://www.amazon.co.jp/"
url_22 ="https://twipla.jp/"
url_23 ="https://atnd.org/"
url_24 ="https://twitter.com"
url_25 ="https://w.atwiki.jp/nicomasmaking/"
url_26 ="http://mol.s7.xrea.com/imasbpmv2.html"
url_27 ="http://spring-fragrance.mints.ne.jp/aviutl/"
url_28 ="https://bit.ly/2XcXHwE"
url_29 ="https://bit.ly/2XeLKXn"
url_30 ="https://bit.ly/354nDgC"
url_31 ="https://www.adobe.com/jp/creativecloud.html"
url_32 ="https://www.videocopilot.net/"
url_33 ="https://flashbackj.com/"
url_34 ="http://ae-users.com/jp/"
url_35 ="http://baaaf.com/"
url_36 ="http://foxcodex.html.xdomain.jp/"
url_37 ="http://photoshopvip.net/"
url_38 ="https://w.atwiki.jp/vpvpwiki/"
url_39 ="https://opengameart.org/"
url_40 ="https://artjuku.com/3d-cg-free-model/"

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

def click_button_19(event):
    webbrowser.open(url_19)

def click_button_20(event):
    webbrowser.open(url_20)

def click_button_21(event):
    webbrowser.open(url_21)

def click_button_22(event):
    webbrowser.open(url_22)

def click_button_23(event):
    webbrowser.open(url_23)

def click_button_24(event):
    webbrowser.open(url_24)

def click_button_25(event):
    webbrowser.open(url_25)

def click_button_26(event):
    webbrowser.open(url_26)

def click_button_27(event):
    webbrowser.open(url_27)

def click_button_28(event):
    webbrowser.open(url_28)

def click_button_29(event):
    webbrowser.open(url_29)

def click_button_30(event):
    webbrowser.open(url_30)

def click_button_31(event):
    webbrowser.open(url_31)

def click_button_32(event):
    webbrowser.open(url_32)

def click_button_33(event):
    webbrowser.open(url_33)

def click_button_34(event):
    webbrowser.open(url_34)

def click_button_35(event):
    webbrowser.open(url_35)

def click_button_36(event):
    webbrowser.open(url_36)

def click_button_37(event):
    webbrowser.open(url_37)

def click_button_38(event):
    webbrowser.open(url_38)

def click_button_39(event):
    webbrowser.open(url_39)

def click_button40(event):
    webbrowser.open(url_40)

# 基礎処理
class Main(wx.Frame):
    def __init__(self, parent, id, title):
        # TITLE
        title = "アイマスウィジェット for windows アイマスPとニコマスPの為のウィジェット"
        message = "Powered by OpenWidget"

        # パネル設定
        wx.Frame.__init__(self, parent, id, title, size=(805, 960), pos=(500, 40))
        panel = wx.Panel(self, wx.ID_ANY)
        # 背景色
        panel.SetBackgroundColour('#ff99ce')

        # 文字色
        font_color = '#000000'

        # ボタン色
        button_color = '#ffe6e6'

        # ボタン設定
        button_1 = wx.Button(panel, wx.ID_ANY, 'アイドルマスター公式', size=(450, 450), style=wx.BORDER_NONE)
        button_2 = wx.Button(panel, wx.ID_ANY, 'アイドルマスター\r\nコロムビア公式', size=(450, 450), style=wx.BORDER_NONE)
        button_3 = wx.Button(panel, wx.ID_ANY, 'アイドルマスター\r\nミリオンライブ！\n\rランティス公式', size=(450, 450), style=wx.BORDER_NONE)
        button_4 = wx.Button(panel, wx.ID_ANY, 'アイドルマスター\n\rsideM\r\nランティス公式', size=(450, 450), style=wx.BORDER_NONE)
        button_5 = wx.Button(panel, wx.ID_ANY, 'アイマスDB', size=(450, 450), style=wx.BORDER_NONE)
        button_6 = wx.Button(panel, wx.ID_ANY, 'im@s news 765', size=(450, 450), style=wx.BORDER_NONE)
        button_7 = wx.Button(panel, wx.ID_ANY, 'デレラジ☆スター', size=(450, 450), style=wx.BORDER_NONE)
        button_8 = wx.Button(panel, wx.ID_ANY, 'シンデレラ\r\nパーティー', size=(450, 450), style=wx.BORDER_NONE)
        button_9 = wx.Button(panel, wx.ID_ANY, 'アイドルマスター\r\nミュージック\r\nオンザレイディオ', size=(450, 450), style=wx.BORDER_NONE)
        button_10 = wx.Button(panel, wx.ID_ANY, 'アイドルマスター\r\nミリオンラジオ！', size=(450, 450), style=wx.BORDER_NONE)
        button_11 = wx.Button(panel, wx.ID_ANY, 'アイドルマスター\r\nSideM ラジオ', size=(450, 450), style=wx.BORDER_NONE)
        button_12 = wx.Button(panel, wx.ID_ANY, '876TV', size=(450, 450), style=wx.BORDER_NONE)
        button_13 = wx.Button(panel, wx.ID_ANY, 'じゃらんホテル予約', size=(450, 450), style=wx.BORDER_NONE)
        button_14 = wx.Button(panel, wx.ID_ANY, 'トリバゴホテル予約', size=(450, 450), style=wx.BORDER_NONE)
        button_15 = wx.Button(panel, wx.ID_ANY, '日本旅行\n\rホテル/交通機関予約', size=(450, 450), style=wx.BORDER_NONE)
        button_16 = wx.Button(panel, wx.ID_ANY, 'バス比較なび', size=(450, 450), style=wx.BORDER_NONE)
        button_17 = wx.Button(panel, wx.ID_ANY, 'スカイスキャナー\n\r航空券比較予約', size=(450, 450), style=wx.BORDER_NONE)
        button_18 = wx.Button(panel, wx.ID_ANY, 'えきねっと\r\n新幹線予約', size=(450, 450), style=wx.BORDER_NONE)
        button_19 = wx.Button(panel, wx.ID_ANY, 'ホットペッパー\r\n飲食店予約検索', size=(450, 450), style=wx.BORDER_NONE)
        button_20 = wx.Button(panel, wx.ID_ANY, 'アソビストア', size=(450, 450), style=wx.BORDER_NONE)
        button_21 = wx.Button(panel, wx.ID_ANY, 'Amazon', size=(450, 450), style=wx.BORDER_NONE)
        button_22 = wx.Button(panel, wx.ID_ANY, 'Twipla', size=(450, 450), style=wx.BORDER_NONE)
        button_23 = wx.Button(panel, wx.ID_ANY, 'ATND', size=(450, 450), style=wx.BORDER_NONE)
        button_24 = wx.Button(panel, wx.ID_ANY, 'Twitter', size=(450, 450), style=wx.BORDER_NONE)
        button_25 = wx.Button(panel, wx.ID_ANY, 'アイマスMAD/PV\r\n制作TIPSまとめwiki', size=(450, 450), style=wx.BORDER_NONE)
        button_26 = wx.Button(panel, wx.ID_ANY, 'てんぶくろ\r\nimasBPM計測', size=(450, 450), style=wx.BORDER_NONE)
        button_27 = wx.Button(panel, wx.ID_ANY, 'AviUtl公式', size=(450, 450), style=wx.BORDER_NONE)
        button_28 = wx.Button(panel, wx.ID_ANY, 'AviUtl講座', size=(450, 450), style=wx.BORDER_NONE)
        button_29 = wx.Button(panel, wx.ID_ANY, 'AviUtl\r\nスクリプト講座', size=(450, 450), style=wx.BORDER_NONE)
        button_30 = wx.Button(panel, wx.ID_ANY, 'Aviutl\r\nプロジェクトファイル\r\n配布動画', size=(450, 450), style=wx.BORDER_NONE)
        button_31 = wx.Button(panel, wx.ID_ANY, 'Adobe公式', size=(450, 450), style=wx.BORDER_NONE)
        button_32 = wx.Button(panel, wx.ID_ANY, 'VideoCopilot', size=(450, 450), style=wx.BORDER_NONE)
        button_33 = wx.Button(panel, wx.ID_ANY, 'FlashbackJapan', size=(450, 450), style=wx.BORDER_NONE)
        button_34 = wx.Button(panel, wx.ID_ANY, 'AEP Project', size=(450, 450), style=wx.BORDER_NONE)
        button_35 = wx.Button(panel, wx.ID_ANY, 'バカ・アフター', size=(450, 450), style=wx.BORDER_NONE)
        button_36 = wx.Button(panel, wx.ID_ANY, 'モーション周期表\r\n(foxcodex MGレシピ)', size=(450, 450), style=wx.BORDER_NONE)
        button_37 = wx.Button(panel, wx.ID_ANY, 'Photoshop Vip\r\n静止画素材・フォント', size=(450, 450), style=wx.BORDER_NONE)
        button_38 = wx.Button(panel, wx.ID_ANY, 'VPVP wiki\n\rMMDポータル', size=(450, 450), style=wx.BORDER_NONE)
        button_39 = wx.Button(panel, wx.ID_ANY, 'OpenGameArt\r\n2D＆3Dフリー素材', size=(450, 450), style=wx.BORDER_NONE)
        button_40 = wx.Button(panel, wx.ID_ANY, 'ARTJUKU\r\n3Dフリー素材まとめ', size=(450, 450), style=wx.BORDER_NONE)
        text = wx.StaticText(panel, -1, message)

        # fontスタイル
        font = wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ")
        title = wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ")

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
        button_19.SetFont(font)
        button_20.SetFont(font)
        button_21.SetFont(font)
        button_22.SetFont(font)
        button_23.SetFont(font)
        button_24.SetFont(font)
        button_25.SetFont(font)
        button_26.SetFont(font)
        button_27.SetFont(font)
        button_28.SetFont(font)
        button_29.SetFont(font)
        button_30.SetFont(font)
        button_31.SetFont(font)
        button_32.SetFont(font)
        button_33.SetFont(font)
        button_34.SetFont(font)
        button_35.SetFont(font)
        button_36.SetFont(font)
        button_37.SetFont(font)
        button_38.SetFont(font)
        button_39.SetFont(font)
        button_40.SetFont(font)
        text.SetFont(title)

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
        button_18.SetBackgroundColour(button_color)
        button_19.SetBackgroundColour(button_color)
        button_20.SetBackgroundColour(button_color)
        button_21.SetBackgroundColour(button_color)
        button_22.SetBackgroundColour(button_color)
        button_23.SetBackgroundColour(button_color)
        button_24.SetBackgroundColour(button_color)
        button_25.SetBackgroundColour(button_color)
        button_26.SetBackgroundColour(button_color)
        button_27.SetBackgroundColour(button_color)
        button_28.SetBackgroundColour(button_color)
        button_29.SetBackgroundColour(button_color)
        button_30.SetBackgroundColour(button_color)
        button_31.SetBackgroundColour(button_color)
        button_32.SetBackgroundColour(button_color)
        button_33.SetBackgroundColour(button_color)
        button_34.SetBackgroundColour(button_color)
        button_35.SetBackgroundColour(button_color)
        button_36.SetBackgroundColour(button_color)
        button_37.SetBackgroundColour(button_color)
        button_38.SetBackgroundColour(button_color)
        button_39.SetBackgroundColour(button_color)
        button_40.SetBackgroundColour(button_color)

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
        button_19.SetForegroundColour(font_color)
        button_20.SetForegroundColour(font_color)
        button_21.SetForegroundColour(font_color)
        button_22.SetForegroundColour(font_color)
        button_23.SetForegroundColour(font_color)
        button_24.SetForegroundColour(font_color)
        button_25.SetForegroundColour(font_color)
        button_26.SetForegroundColour(font_color)
        button_27.SetForegroundColour(font_color)
        button_28.SetForegroundColour(font_color)
        button_29.SetForegroundColour(font_color)
        button_30.SetForegroundColour(font_color)
        button_31.SetForegroundColour(font_color)
        button_32.SetForegroundColour(font_color)
        button_33.SetForegroundColour(font_color)
        button_34.SetForegroundColour(font_color)
        button_35.SetForegroundColour(font_color)
        button_36.SetForegroundColour(font_color)
        button_37.SetForegroundColour(font_color)
        button_38.SetForegroundColour(font_color)
        button_39.SetForegroundColour(font_color)
        button_40.SetForegroundColour(font_color)

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
        button_19.Bind(wx.EVT_LEFT_DOWN, click_button_19)
        button_20.Bind(wx.EVT_LEFT_DOWN, click_button_20)
        button_21.Bind(wx.EVT_LEFT_DOWN, click_button_21)
        button_22.Bind(wx.EVT_LEFT_DOWN, click_button_22)
        button_23.Bind(wx.EVT_LEFT_DOWN, click_button_23)
        button_24.Bind(wx.EVT_LEFT_DOWN, click_button_24)
        button_25.Bind(wx.EVT_LEFT_DOWN, click_button_25)
        button_26.Bind(wx.EVT_LEFT_DOWN, click_button_26)
        button_27.Bind(wx.EVT_LEFT_DOWN, click_button_27)
        button_28.Bind(wx.EVT_LEFT_DOWN, click_button_28)
        button_29.Bind(wx.EVT_LEFT_DOWN, click_button_29)
        button_30.Bind(wx.EVT_LEFT_DOWN, click_button_30)
        button_31.Bind(wx.EVT_LEFT_DOWN, click_button_31)
        button_32.Bind(wx.EVT_LEFT_DOWN, click_button_32)
        button_33.Bind(wx.EVT_LEFT_DOWN, click_button_33)
        button_34.Bind(wx.EVT_LEFT_DOWN, click_button_34)
        button_35.Bind(wx.EVT_LEFT_DOWN, click_button_35)
        button_36.Bind(wx.EVT_LEFT_DOWN, click_button_36)
        button_37.Bind(wx.EVT_LEFT_DOWN, click_button_37)
        button_38.Bind(wx.EVT_LEFT_DOWN, click_button_38)
        button_39.Bind(wx.EVT_LEFT_DOWN, click_button_39)
        button_40.Bind(wx.EVT_LEFT_DOWN, click_button_39)

        # パネルレイアウト
        layout = wx.GridSizer(rows=7, cols=6, gap=(1, 1))

        # パーツ配置
        layout.Add(button_1, flag=wx.SHAPED)
        layout.Add(button_2, flag=wx.SHAPED)
        layout.Add(button_3, flag=wx.SHAPED)
        layout.Add(button_4, flag=wx.SHAPED)
        layout.Add(button_5, flag=wx.SHAPED)
        layout.Add(button_6, flag=wx.SHAPED)
        layout.Add(button_7, flag=wx.SHAPED)
        layout.Add(button_8, flag=wx.SHAPED)
        layout.Add(button_9, flag=wx.SHAPED)
        layout.Add(button_10, flag=wx.SHAPED)
        layout.Add(button_11, flag=wx.SHAPED)
        layout.Add(button_12, flag=wx.SHAPED)
        layout.Add(button_13, flag=wx.SHAPED)
        layout.Add(button_14, flag=wx.SHAPED)
        layout.Add(button_15, flag=wx.SHAPED)
        layout.Add(button_16, flag=wx.SHAPED)
        layout.Add(button_17, flag=wx.SHAPED)
        layout.Add(button_18, flag=wx.SHAPED)
        layout.Add(button_19, flag=wx.SHAPED)
        layout.Add(button_20, flag=wx.SHAPED)
        layout.Add(button_21, flag=wx.SHAPED)
        layout.Add(button_22, flag=wx.SHAPED)
        layout.Add(button_23, flag=wx.SHAPED)
        layout.Add(button_24, flag=wx.SHAPED)
        layout.Add(button_25, flag=wx.SHAPED)
        layout.Add(button_26, flag=wx.SHAPED)
        layout.Add(button_27, flag=wx.SHAPED)
        layout.Add(button_28, flag=wx.SHAPED)
        layout.Add(button_29, flag=wx.SHAPED)
        layout.Add(button_30, flag=wx.SHAPED)
        layout.Add(button_31, flag=wx.SHAPED)
        layout.Add(button_32, flag=wx.SHAPED)
        layout.Add(button_33, flag=wx.SHAPED)
        layout.Add(button_34, flag=wx.SHAPED)
        layout.Add(button_35, flag=wx.SHAPED)
        layout.Add(button_36, flag=wx.SHAPED)
        layout.Add(button_37, flag=wx.SHAPED)
        layout.Add(button_38, flag=wx.SHAPED)
        layout.Add(button_39, flag=wx.SHAPED)
        layout.Add(button_40, flag=wx.SHAPED)
        layout.Add(text)
        panel.SetSizer(layout)
        self.Show(True)

# 画面表示
def main():
    app = wx.App()
    Main(None, wx.ID_ANY, "")
    app.MainLoop()


if __name__ == "__main__":
    main()
