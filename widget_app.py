# coding: UTF-8

# MikuMikuWidget For MMD-CUP-ZERO2 [Contributor Edition]
# project name OpenWidget
# develop by storchP

import wx
import os
import webbrowser
import sys

sys.stdout = open(os.devnull, "w")


# URL LIST
url_11 = "https://www.3dcadbrowser.com/"
url_12 = "https://3dwarehouse.sketchup.com/"
url_13 = "http://artist-3d.com/free_3d_models"
url_14 = "http://www.3dmodelfree.com/"
url_15 = "https://dimensiva.com/"
url_16 = "https://www.turbosquid.com/ja/"
url_17 = "https://www.daz3d.com/shop/"
url_18 = "https://opengameart.org/"
url_19 = "https://bowlroll.net/"
url_20 = "https://www.nicovideo.jp/tag/MMD%e3%83%a2%e3%83%87%e3%83%ab%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=f&order=d"
url_21 = "http://seiga.nicovideo.jp/tag/MMD%e3%83%a2%e3%83%87%e3%83%ab%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=image_created"
url_22 = "https://www6.atwiki.jp/vpvpwiki/"
url_23 = "http://commons.nicovideo.jp/materials/"
url_24 = "https://dova-s.jp/"
url_25 = "https://soundeffect-lab.info/"
url_26 = "https://storyinvention.com/free-3d-model-matome/"
url_27 = "https://www.nicovideo.jp/tag/MMD%e3%82%a2%e3%82%af%e3%82%bb%e3%82%b5%e3%83%aa%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?ref=tagconcerned"
url_28 = "https://seiga.nicovideo.jp/tag/MMD%e3%82%a2%e3%82%af%e3%82%bb%e3%82%b5%e3%83%aa%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?target=illust"
url_29 = "https://www.nicovideo.jp/tag/MMD%e3%82%b9%e3%83%86%e3%83%bc%e3%82%b8%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=f&order=d"
url_30 = "https://seiga.nicovideo.jp/tag/MMD%e3%82%b9%e3%83%86%e3%83%bc%e3%82%b8%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=image_created"
url_31 = "https://www.nicovideo.jp/tag/MMD%e8%a1%a3%e8%a3%85%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=f&order=d"
url_32 = "http://seiga.nicovideo.jp/tag/MMD%e8%a1%a3%e8%a3%85%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=f&order=d?sort=image_created"
url_33 = "https://www.nicovideo.jp/tag/MME%e3%83%87%e3%83%bc%e3%82%bf%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=f&order=d"
url_34 = "http://seiga.nicovideo.jp/tag/MME%e3%83%87%e3%83%bc%e3%82%bf%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=image_created"
url_35 = "https://www.nicovideo.jp/tag/MMD%e3%83%84%e3%83%bc%e3%83%ab%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=f&order=d"
url_36 = "http://seiga.nicovideo.jp/tag/MMD%e3%83%84%e3%83%bc%e3%83%ab%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?target=illust"
url_37 = "https://www.nicovideo.jp/tag/MMD%e3%83%a2%e3%83%bc%e3%82%b7%e3%83%a7%e3%83%b3%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=f&order=d"
url_38 ="https://www.nicovideo.jp/tag/AviUtl%e3%82%b9%e3%82%af%e3%83%aa%e3%83%97%e3%83%88%e8%ac%9b%e5%ba%a7?sort=f&order=d"
url_39 ="https://www.nicovideo.jp/tag/AviUtl%e3%83%97%e3%83%ad%e3%82%b8%e3%82%a7%e3%82%af%e3%83%88%e3%83%95%e3%82%a1%e3%82%a4%e3%83%ab%e9%85%8d%e5%b8%83%e5%8b%95%e7%94%bb?sort=f&order=d"
url_40 ="http://photoshopvip.net/"
url_41 ="http://ae-users.com/jp/"
url_42 ="http://web.archive.org/web/20021214075533/www5a.biglobe.ne.jp/~oadas/compose/toppage.htm"

# URL展開

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

def click_button_40(event):
    webbrowser.open(url_40)

def click_button_41(event):
    webbrowser.open(url_41)

def click_button_42(event):
    webbrowser.open(url_42)


# 基礎処理
class Main(wx.Frame):
    def __init__(self, parent, id, title):
        # TITLE
        title = "MikuMikuWidget2 [Contributor Edition]"
        message = "\n\r\n\r MikuMikuWidget2\n\r [Contributor Edition]"

        # パネル設定
        wx.Frame.__init__(self, parent, id, title, size=(780, 800), pos=(500, 40))
        panel = wx.Panel(self, wx.ID_ANY)
        # 背景色
        panel.SetBackgroundColour('#2b6a6b')

        # 文字色
        font_color = '#a1b3b3'

        # ボタン色
        button_color = '#2f4f4f'

        # ボタン設定
        button_11 = wx.Button(panel, wx.ID_ANY, '3D CAD\r\nBROUSER\r\nフリー地形・乗物', size=(450, 450), style=wx.BORDER_NONE)
        button_12 = wx.Button(panel, wx.ID_ANY, '3D warehouse\r\nフリー建築物', size=(450, 450), style=wx.BORDER_NONE)
        button_13 = wx.Button(panel, wx.ID_ANY, 'Artist3D\r\nFree Model', size=(450, 450), style=wx.BORDER_NONE)
        button_14 = wx.Button(panel, wx.ID_ANY, '3D Model Free\r\n3D家具', size=(450, 450), style=wx.BORDER_NONE)
        button_15 = wx.Button(panel, wx.ID_ANY, 'Dimensiva\r\n3D家具', size=(450, 450), style=wx.BORDER_NONE)
        button_16 = wx.Button(panel, wx.ID_ANY, 'TURBO SQUID\r\n3Dモデル', size=(450, 450), style=wx.BORDER_NONE)
        button_17 = wx.Button(panel, wx.ID_ANY, 'Daz3D\r\nShop', size=(450, 450), style=wx.BORDER_NONE)
        button_18 = wx.Button(panel, wx.ID_ANY, 'Open Game Art\r\nORG', size=(450, 450), style=wx.BORDER_NONE)
        button_19 = wx.Button(panel, wx.ID_ANY, 'bowlroll', size=(450, 450), style=wx.BORDER_NONE)
        button_20 = wx.Button(panel, wx.ID_ANY, 'MMDモデル配布あり\n\r(動画)', size=(450, 450), style=wx.BORDER_NONE)
        button_21 = wx.Button(panel, wx.ID_ANY, 'MMDモデル配布あり\n\r(静画)', size=(450, 450), style=wx.BORDER_NONE)
        button_22 = wx.Button(panel, wx.ID_ANY, 'VPVP Wiki', size=(450, 450), style=wx.BORDER_NONE)
        button_23 = wx.Button(panel, wx.ID_ANY, 'ニコニ・コモンズ\n\r素材ライブラリ', size=(450, 450), style=wx.BORDER_NONE)
        button_24 = wx.Button(panel, wx.ID_ANY, 'フリーBGM\n\rDOVA SYNDROME', size=(450, 450), style=wx.BORDER_NONE)
        button_25 = wx.Button(panel, wx.ID_ANY, '効果音ラボ', size=(450, 450), style=wx.BORDER_NONE)
        button_26 = wx.Button(panel, wx.ID_ANY, 'フリー3D\n\rモデルまとめ\n\r(MOMIZIZM)', size=(450, 450), style=wx.BORDER_NONE)
        button_27 = wx.Button(panel, wx.ID_ANY, 'MMDアクセサリ\n\r配布あり\n\r(動画)', size=(450, 450), style=wx.BORDER_NONE)
        button_28 = wx.Button(panel, wx.ID_ANY, 'MMDアクセサリ\n\r配布あり\n\r(静画)', size=(450, 450), style=wx.BORDER_NONE)
        button_29 = wx.Button(panel, wx.ID_ANY, 'MMDステージ\n\r配布あり\n\r(動画)', size=(450, 450), style=wx.BORDER_NONE)
        button_30 = wx.Button(panel, wx.ID_ANY, 'MMDステージ\n\r配布あり\n\r(静画)', size=(450, 450), style=wx.BORDER_NONE)
        button_31 = wx.Button(panel, wx.ID_ANY, 'MMD衣装配布あり\n\r(動画)', size=(450, 450), style=wx.BORDER_NONE)
        button_32 = wx.Button(panel, wx.ID_ANY, 'MMD衣装配布あり\n\r(静画)', size=(450, 450), style=wx.BORDER_NONE)
        button_33 = wx.Button(panel, wx.ID_ANY, 'MMEデータ配布あり\n\r(動画)', size=(450, 450), style=wx.BORDER_NONE)
        button_34 = wx.Button(panel, wx.ID_ANY, 'MMEデータ配布あり\n\r(静画)', size=(450, 450), style=wx.BORDER_NONE)
        button_35 = wx.Button(panel, wx.ID_ANY, 'MMDツール配布あり\n\r(動画)', size=(450, 450), style=wx.BORDER_NONE)
        button_36 = wx.Button(panel, wx.ID_ANY, 'MMDツール配布あり\n\r(静画)', size=(450, 450), style=wx.BORDER_NONE)
        button_37 = wx.Button(panel, wx.ID_ANY, 'MMDモーション\n\r配布あり', size=(450, 450), style=wx.BORDER_NONE)
        button_38 = wx.Button(panel, wx.ID_ANY, 'AviUtl\n\rスクリプト講座', size=(450, 450), style=wx.BORDER_NONE)
        button_39 = wx.Button(panel, wx.ID_ANY, 'AviUtl\n\rプロジェクトファイル\n\r配布動画', size=(450, 450), style=wx.BORDER_NONE)
        button_40 = wx.Button(panel, wx.ID_ANY, '静止画素材情報\n\rPHOTOSHOP VIP', size=(450, 450), style=wx.BORDER_NONE)
        button_41 = wx.Button(panel, wx.ID_ANY, 'AE tips集\n\rAEP Project', size=(450, 450), style=wx.BORDER_NONE)
        button_42 = wx.Button(panel, wx.ID_ANY, 'OADAS\n\r作曲入門講座', size=(450, 450), style=wx.BORDER_NONE)
        text = wx.StaticText(panel, -1, message)

        # fontスタイル
        font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ")
        title = wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ")

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
        button_41.SetFont(font)
        button_42.SetFont(font)
        text.SetFont(title)

        # ボタンカラー
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
        button_41.SetBackgroundColour(button_color)
        button_42.SetBackgroundColour(button_color)

        # ボタン文字色
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
        button_41.SetForegroundColour(font_color)
        button_42.SetForegroundColour(font_color)
        text.SetForegroundColour(font_color)

        # ボタンクリック時のバインド
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
        button_40.Bind(wx.EVT_LEFT_DOWN, click_button_40)
        button_41.Bind(wx.EVT_LEFT_DOWN, click_button_41)
        button_42.Bind(wx.EVT_LEFT_DOWN, click_button_41)
        # パネルレイアウト
        layout = wx.GridSizer(rows=6, cols=6, gap=(1, 1))

        # パーツ配置
        layout.Add(button_18, flag=wx.SHAPED)
        layout.Add(button_17, flag=wx.SHAPED)
        layout.Add(button_16, flag=wx.SHAPED)
        layout.Add(button_15, flag=wx.SHAPED)
        layout.Add(button_14, flag=wx.SHAPED)
        layout.Add(button_13, flag=wx.SHAPED)
        layout.Add(button_12, flag=wx.SHAPED)
        layout.Add(button_11, flag=wx.SHAPED)
        layout.Add(button_22, flag=wx.SHAPED)
        layout.Add(button_19, flag=wx.SHAPED)
        layout.Add(button_20, flag=wx.SHAPED)
        layout.Add(button_21, flag=wx.SHAPED)
        layout.Add(button_23, flag=wx.SHAPED)
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
        layout.Add(button_24, flag=wx.SHAPED)
        layout.Add(button_25, flag=wx.SHAPED)
        layout.Add(button_26, flag=wx.SHAPED)
        layout.Add(button_38, flag=wx.SHAPED)
        layout.Add(button_39, flag=wx.SHAPED)
        layout.Add(button_40, flag=wx.SHAPED)
        layout.Add(button_41, flag=wx.SHAPED)
        layout.Add(button_42, flag=wx.SHAPED)
        layout.Add(text)


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
