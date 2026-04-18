# coding: UTF-8


# MikuMikuWidget For MikuMikuWidget2.6 [Contributor Edition]
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
url_14 = "http://www.3dmodelfree.com/"
url_15 = "https://dimensiva.com/"
url_16 = "https://www.turbosquid.com/ja/"
url_17 = "https://www.daz3d.com/shop/"
url_18 = "https://opengameart.org/"
url_19 = "https://bowlroll.net/"
url_20 = "https://www.nicovideo.jp/tag/MMD%e3%83%a2%e3%83%87%e3%83%ab%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=f&order=d"
url_21 = "http://seiga.nicovideo.jp/tag/MMD%e3%83%a2%e3%83%87%e3%83%ab%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=image_created"
url_22 = "https://www6.atwiki.jp/vpvpwiki/"
url_23 = "http://commons.nicovideo.jp/"
url_24 = "https://dova-s.jp/"
url_25 = "https://soundeffect-lab.info/"
url_26 = "https://storyinvention.com/free-3d-model-matome/"
url_27 = "https://www.nicovideo.jp/tag/MMD%e3%82%a2%e3%82%af%e3%82%bb%e3%82%b5%e3%83%aa%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?ref=tagconcerned"
url_28 = "https://seiga.nicovideo.jp/tag/MMD%e3%82%a2%e3%82%af%e3%82%bb%e3%82%b5%e3%83%aa%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?target=illust"
url_29 = "https://www.nicovideo.jp/tag/MMD%e3%82%b9%e3%83%86%e3%83%bc%e3%82%b8%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=f&order=d"
url_30 = "https://seiga.nicovideo.jp/tag/MMD%e3%82%b9%e3%83%86%e3%83%bc%e3%82%b8%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=image_created"
url_31 = "https://www.nicovideo.jp/tag/MMD%e8%a1%a3%e8%a3%85%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=f&order=d"
url_32 = "https://seiga.nicovideo.jp/tag/MMD%E8%A1%A3%E8%A3%85%E9%85%8D%E5%B8%83%E3%81%82%E3%82%8A?sort=image_created"
url_33 = "https://www.nicovideo.jp/tag/MME%e3%83%87%e3%83%bc%e3%82%bf%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=f&order=d"
url_34 = "http://seiga.nicovideo.jp/tag/MME%e3%83%87%e3%83%bc%e3%82%bf%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=image_created"
url_35 = "https://www.nicovideo.jp/tag/MMD%e3%83%84%e3%83%bc%e3%83%ab%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?sort=f&order=d"
url_36 = "http://seiga.nicovideo.jp/tag/MMD%e3%83%84%e3%83%bc%e3%83%ab%e9%85%8d%e5%b8%83%e3%81%82%e3%82%8a?target=illust"
url_38 ="https://www.nicovideo.jp/tag/AviUtl%e3%82%b9%e3%82%af%e3%83%aa%e3%83%97%e3%83%88%e8%ac%9b%e5%ba%a7?sort=f&order=d"
url_39 ="https://www.nicovideo.jp/tag/AviUtl%e3%83%97%e3%83%ad%e3%82%b8%e3%82%a7%e3%82%af%e3%83%88%e3%83%95%e3%82%a1%e3%82%a4%e3%83%ab%e9%85%8d%e5%b8%83%e5%8b%95%e7%94%bb?sort=f&order=d"
url_40 ="http://photoshopvip.net/"
url_41 ="http://ae-users.com/jp/"
url_42 ="http://web.archive.org/web/20021214075533/www5a.biglobe.ne.jp/~oadas/compose/toppage.htm"

# MMDモデル配布あり\r\n(ニコニ立体)
url_43 ="https://3d.nicovideo.jp/search?word_type=tag&word=MMD%E3%83%A2%E3%83%87%E3%83%AB%E9%85%8D%E5%B8%83%E3%81%82%E3%82%8A"

#MMDアクセサリ配布あり\r\n(ニコニ立体)
url_44 ="https://3d.nicovideo.jp/search?word_type=tag&word=MMD%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B5%E3%83%AA%E9%85%8D%E5%B8%83%E3%81%82%E3%82%8A"

#MMDステージ配布あり\r\n(ニコニ立体)
url_45 ="https://3d.nicovideo.jp/search?word_type=tag&word=MMD%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8%E9%85%8D%E5%B8%83%E3%81%82%E3%82%8A"

#MMD衣装配布あり\r\n(ニコニ立体)
url_46 ="https://3d.nicovideo.jp/search?word_type=tag&word=MMD%E8%A1%A3%E8%A3%85%E9%85%8D%E5%B8%83%E3%81%82%E3%82%8A"

#MMDモーション配布あり\r\n(ニコニコ動画)
url_47 ="https://www.nicovideo.jp/tag/MMD%E3%83%A2%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E9%85%8D%E5%B8%83%E3%81%82%E3%82%8A"

#MMDポーズ配布あり\r\n(ニコニコ動画)
url_48 ="https://www.nicovideo.jp/tag/MMD%E3%83%9D%E3%83%BC%E3%82%BA%E9%85%8D%E5%B8%83%E3%81%82%E3%82%8A"

#MMDポーズ配布あり\r\n(ニコニコ静画)
url_49 ="https://seiga.nicovideo.jp/tag/MMD%E3%83%9D%E3%83%BC%E3%82%BA%E9%85%8D%E5%B8%83%E3%81%82%E3%82%8A?sort=image_created"

#AviUtlスクリプト講座\r\n(ニコニコ動画)
url_50 ="https://www.nicovideo.jp/tag/AviUtl%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88%E8%AC%9B%E5%BA%A7"

#MMD\r\nUGSFモデルまとめ
url_51 ="https://ugsf.org/mmd-sf-fes-site/model_db/"
# URL展開


url_52 = "https://www.amazon.co.jp/hz/wishlist/ls/IYVIJXMHB9O0?type=wishlist&filter=unpurchased&sort=custom&viewType=list"

# https://chatgpt.com/
url_53 = "https://chatgpt.com/"

def click_button_11(event):
    webbrowser.open(url_11)

def click_button_12(event):
    webbrowser.open(url_12)

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

def click_button_43(event):
    webbrowser.open(url_43)

def click_button_44(event):
    webbrowser.open(url_44)

def click_button_45(event):
    webbrowser.open(url_45)

def click_button_46(event):
    webbrowser.open(url_46)

def click_button_47(event):
    webbrowser.open(url_47)

def click_button_48(event):
    webbrowser.open(url_48)

def click_button_49(event):
    webbrowser.open(url_49)

def click_button_50(event):
    webbrowser.open(url_50)

def click_button_51(event):
    webbrowser.open(url_51)

def click_button_52(event):
    webbrowser.open(url_52)

def click_button_53(event):
    webbrowser.open(url_53)

# 基礎処理
class Main(wx.Frame):
    def __init__(self, parent, id, title):
        # TITLE
        title = "MikuMikuWidget2.6 [Contributor Edition]"
        message = ("\r\n\r\n MikuMikuWidget2.6"
                   "\r\n [Contributor Edition]")

        # パネル設定
        wx.Frame.__init__(self, parent, id, title, size=(1000, 1000), pos=(500, 40))

        # ウィンドウアイコン
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(sys.argv[0])))
        icon_path = os.path.join(base_path, "icon.ico")
        if os.path.exists(icon_path):
            self.SetIcon(wx.Icon(icon_path, wx.BITMAP_TYPE_ICO))

        panel = wx.Panel(self, wx.ID_ANY)
        # 背景色
        panel.SetBackgroundColour('#2b6a6b')

        # 文字色
        font_color = '#a1b3b3'

        # ボタン色
        button_color = '#2f4f4f'

        # ボタン設定
        button_11 = wx.Button(panel, wx.ID_ANY, '3D CAD\r\nBROUSER\r\nフリー地形・乗物\r\n3Dモデル', size=(560, 560), style=wx.BORDER_NONE)
        button_12 = wx.Button(panel, wx.ID_ANY, '3D warehouse\r\nフリー建築物\r\n3Dモデル', size=(560, 560), style=wx.BORDER_NONE)
        button_14 = wx.Button(panel, wx.ID_ANY, '3D Model Free\r\n3D家具モデル', size=(560, 560), style=wx.BORDER_NONE)
        button_15 = wx.Button(panel, wx.ID_ANY, 'Dimensiva\r\n3D家具モデル', size=(560, 560), style=wx.BORDER_NONE)
        button_16 = wx.Button(panel, wx.ID_ANY, 'TURBO SQUID\r\n3Dモデル', size=(560, 560), style=wx.BORDER_NONE)
        button_17 = wx.Button(panel, wx.ID_ANY, 'Daz3D\r\nShop\r\n3Dモデルショップ', size=(560, 560), style=wx.BORDER_NONE)
        button_18 = wx.Button(panel, wx.ID_ANY, 'Open Game Art\r\nORG\r\n各種素材', size=(560, 560), style=wx.BORDER_NONE)
        button_19 = wx.Button(panel, wx.ID_ANY, 'bowlroll', size=(560, 560), style=wx.BORDER_NONE)
        button_20 = wx.Button(panel, wx.ID_ANY, 'MMDモデル配布あり\r\n(動画)', size=(560, 560), style=wx.BORDER_NONE)
        button_21 = wx.Button(panel, wx.ID_ANY, 'MMDモデル配布あり\r\n(静画)', size=(560, 560), style=wx.BORDER_NONE)
        button_22 = wx.Button(panel, wx.ID_ANY, 'VPVP Wiki', size=(560, 560), style=wx.BORDER_NONE)
        button_23 = wx.Button(panel, wx.ID_ANY, 'ニコニ・コモンズ\r\n素材ライブラリ', size=(560, 560), style=wx.BORDER_NONE)
        button_24 = wx.Button(panel, wx.ID_ANY, 'フリーBGM\r\nDOVA SYNDROME', size=(560, 560), style=wx.BORDER_NONE)
        button_25 = wx.Button(panel, wx.ID_ANY, '効果音ラボ', size=(560, 560), style=wx.BORDER_NONE)
        button_26 = wx.Button(panel, wx.ID_ANY, 'フリー3D\r\nモデルまとめ\r\n(MOMIZIZM)', size=(560, 560), style=wx.BORDER_NONE)
        button_27 = wx.Button(panel, wx.ID_ANY, 'MMDアクセサリ\r\n配布あり\r\n(動画)', size=(560, 560), style=wx.BORDER_NONE)
        button_28 = wx.Button(panel, wx.ID_ANY, 'MMDアクセサリ\r\n配布あり\r\n(静画)', size=(560, 560), style=wx.BORDER_NONE)
        button_29 = wx.Button(panel, wx.ID_ANY, 'MMDステージ\r\n配布あり\r\n(動画)', size=(560, 560), style=wx.BORDER_NONE)
        button_30 = wx.Button(panel, wx.ID_ANY, 'MMDステージ\r\n配布あり\r\n(静画)', size=(560, 560), style=wx.BORDER_NONE)
        button_31 = wx.Button(panel, wx.ID_ANY, 'MMD衣装配布あり\r\n(動画)', size=(560, 560), style=wx.BORDER_NONE)
        button_32 = wx.Button(panel, wx.ID_ANY, 'MMD衣装配布あり\r\n(静画)', size=(560, 560), style=wx.BORDER_NONE)
        button_33 = wx.Button(panel, wx.ID_ANY, 'MMEデータ配布あり\r\n(動画)', size=(560, 560), style=wx.BORDER_NONE)
        button_34 = wx.Button(panel, wx.ID_ANY, 'MMEデータ配布あり\r\n(静画)', size=(560, 560), style=wx.BORDER_NONE)
        button_35 = wx.Button(panel, wx.ID_ANY, 'MMDツール配布あり\r\n(動画)', size=(560, 560), style=wx.BORDER_NONE)
        button_36 = wx.Button(panel, wx.ID_ANY, 'MMDツール配布あり\r\n(静画)', size=(560, 560), style=wx.BORDER_NONE)
        button_38 = wx.Button(panel, wx.ID_ANY, 'AviUtl\r\nスクリプト講座', size=(560, 560), style=wx.BORDER_NONE)
        button_39 = wx.Button(panel, wx.ID_ANY, 'AviUtl\r\nプロジェクトファイル\r\n配布動画', size=(560, 560), style=wx.BORDER_NONE)
        button_40 = wx.Button(panel, wx.ID_ANY, '静止画素材情報\r\nPHOTOSHOP VIP', size=(560, 560), style=wx.BORDER_NONE)
        button_41 = wx.Button(panel, wx.ID_ANY, 'AE tips集\r\nAEP Project', size=(560, 560), style=wx.BORDER_NONE)
        button_42 = wx.Button(panel, wx.ID_ANY, 'OADAS\r\n作曲入門講座', size=(560, 560), style=wx.BORDER_NONE)


        # 追加分
        button_43 = wx.Button(panel, wx.ID_ANY, 'MMDモデル配布あり\r\n(ニコニ立体)', size=(560, 560), style=wx.BORDER_NONE)
        button_44 = wx.Button(panel, wx.ID_ANY, 'MMDアクセサリ\r\n配布あり\r\n(ニコニ立体)', size=(560, 560), style=wx.BORDER_NONE)
        button_45 = wx.Button(panel, wx.ID_ANY, 'MMDステージ\r\n配布あり\r\n(ニコニ立体)', size=(560, 560), style=wx.BORDER_NONE)
        button_46 = wx.Button(panel, wx.ID_ANY, 'MMD衣装配布あり\r\n(ニコニ立体)', size=(560, 560), style=wx.BORDER_NONE)
        button_47 = wx.Button(panel, wx.ID_ANY, 'MMDモーション\r\n'
                                                '配布あり\r\n(ニコニコ動画)', size=(560, 560), style=wx.BORDER_NONE)
        button_48 = wx.Button(panel, wx.ID_ANY, 'MMDポーズ配布あり\r\n(ニコニコ動画)', size=(560, 560), style=wx.BORDER_NONE)
        button_49 = wx.Button(panel, wx.ID_ANY, 'MMDポーズ配布あり\r\n(ニコニコ静画)', size=(560, 560), style=wx.BORDER_NONE)
        button_50 = wx.Button(panel, wx.ID_ANY, 'AviUtlスクリプト講座\r\n(ニコニコ動画)', size=(560, 560), style=wx.BORDER_NONE)
        button_51 = wx.Button(panel, wx.ID_ANY, 'MMD\r\nUGSFモデルまとめ', size=(560, 560), style=wx.BORDER_NONE)
        button_52 = wx.Button(panel, wx.ID_ANY, '開発者に寄付する', size=(560, 560), style=wx.BORDER_NONE)
        button_53 = wx.Button(panel, wx.ID_ANY, 'ChatGPT', size=(560, 560), style=wx.BORDER_NONE)




        text = wx.StaticText(panel, -1, message)

        # fontスタイル
        font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ")
        title = wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ")

        button_11.SetFont(font)
        button_12.SetFont(font)
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
        button_38.SetFont(font)
        button_39.SetFont(font)
        button_40.SetFont(font)
        button_41.SetFont(font)
        button_42.SetFont(font)

        button_43.SetFont(font)
        button_44.SetFont(font)
        button_45.SetFont(font)
        button_46.SetFont(font)
        button_47.SetFont(font)
        button_48.SetFont(font)
        button_49.SetFont(font)
        button_50.SetFont(font)
        button_51.SetFont(font)
        button_52.SetFont(font)
        button_53.SetFont(font)

        text.SetFont(title)

        # ボタンカラー
        button_11.SetBackgroundColour(button_color)
        button_12.SetBackgroundColour(button_color)
        button_14.SetBackgroundColour(button_color)
        button_15.SetBackgroundColour(button_color)
        button_16.SetBackgroundColour(button_color)
        button_17.SetBackgroundColour(button_color)
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
        button_38.SetBackgroundColour(button_color)
        button_39.SetBackgroundColour(button_color)
        button_40.SetBackgroundColour(button_color)
        button_41.SetBackgroundColour(button_color)
        button_42.SetBackgroundColour(button_color)
        button_43.SetBackgroundColour(button_color)
        button_44.SetBackgroundColour(button_color)
        button_45.SetBackgroundColour(button_color)
        button_46.SetBackgroundColour(button_color)
        button_47.SetBackgroundColour(button_color)
        button_48.SetBackgroundColour(button_color)
        button_49.SetBackgroundColour(button_color)
        button_50.SetBackgroundColour(button_color)
        button_51.SetBackgroundColour(button_color)
        button_52.SetBackgroundColour(button_color)
        button_53.SetBackgroundColour(button_color)

        # ボタン文字色
        button_11.SetForegroundColour(font_color)
        button_12.SetForegroundColour(font_color)
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
        button_38.SetForegroundColour(font_color)
        button_39.SetForegroundColour(font_color)
        button_40.SetForegroundColour(font_color)
        button_41.SetForegroundColour(font_color)
        button_42.SetForegroundColour(font_color)
        button_43.SetForegroundColour(font_color)
        button_44.SetForegroundColour(font_color)
        button_45.SetForegroundColour(font_color)
        button_46.SetForegroundColour(font_color)
        button_47.SetForegroundColour(font_color)
        button_48.SetForegroundColour(font_color)
        button_49.SetForegroundColour(font_color)
        button_50.SetForegroundColour(font_color)
        button_51.SetForegroundColour(font_color)
        button_52.SetForegroundColour(font_color)
        button_53.SetForegroundColour(font_color)


        text.SetForegroundColour(font_color)

        # ボタンクリック時のバインド
        button_11.Bind(wx.EVT_LEFT_DOWN, click_button_11)
        button_12.Bind(wx.EVT_LEFT_DOWN, click_button_12)
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
        button_38.Bind(wx.EVT_LEFT_DOWN, click_button_38)
        button_39.Bind(wx.EVT_LEFT_DOWN, click_button_39)
        button_40.Bind(wx.EVT_LEFT_DOWN, click_button_40)
        button_41.Bind(wx.EVT_LEFT_DOWN, click_button_41)
        button_42.Bind(wx.EVT_LEFT_DOWN, click_button_42)
        button_43.Bind(wx.EVT_LEFT_DOWN, click_button_43)
        button_44.Bind(wx.EVT_LEFT_DOWN, click_button_44)
        button_45.Bind(wx.EVT_LEFT_DOWN, click_button_45)
        button_46.Bind(wx.EVT_LEFT_DOWN, click_button_46)
        button_47.Bind(wx.EVT_LEFT_DOWN, click_button_47)
        button_48.Bind(wx.EVT_LEFT_DOWN, click_button_48)
        button_49.Bind(wx.EVT_LEFT_DOWN, click_button_49)
        button_50.Bind(wx.EVT_LEFT_DOWN, click_button_50)
        button_51.Bind(wx.EVT_LEFT_DOWN, click_button_51)
        button_52.Bind(wx.EVT_LEFT_DOWN, click_button_52)
        button_53.Bind(wx.EVT_LEFT_DOWN, click_button_53)




        # パネルレイアウト
        layout = wx.GridSizer(rows=7, cols=7, gap=(10, 10))

        # パーツ配置
        layout.Add(button_18, flag=wx.EXPAND)
        layout.Add(button_17, flag=wx.EXPAND)
        layout.Add(button_16, flag=wx.EXPAND)
        layout.Add(button_15, flag=wx.EXPAND)
        layout.Add(button_14, flag=wx.EXPAND)
        layout.Add(button_12, flag=wx.EXPAND)
        layout.Add(button_11, flag=wx.EXPAND)
        layout.Add(button_22, flag=wx.EXPAND)
        layout.Add(button_19, flag=wx.EXPAND)
        layout.Add(button_20, flag=wx.EXPAND)
        layout.Add(button_21, flag=wx.EXPAND)

        layout.Add(button_43, flag=wx.EXPAND)

        layout.Add(button_23, flag=wx.EXPAND)
        layout.Add(button_27, flag=wx.EXPAND)
        layout.Add(button_28, flag=wx.EXPAND)

        layout.Add(button_44, flag=wx.EXPAND)

        layout.Add(button_29, flag=wx.EXPAND)
        layout.Add(button_30, flag=wx.EXPAND)

        layout.Add(button_45, flag=wx.EXPAND)


        layout.Add(button_31, flag=wx.EXPAND)
        layout.Add(button_32, flag=wx.EXPAND)

        layout.Add(button_46, flag=wx.EXPAND)

        layout.Add(button_47, flag=wx.EXPAND)
        layout.Add(button_48, flag=wx.EXPAND)
        layout.Add(button_49, flag=wx.EXPAND)
        layout.Add(button_50, flag=wx.EXPAND)
        layout.Add(button_51, flag=wx.EXPAND)

        layout.Add(button_33, flag=wx.EXPAND)
        layout.Add(button_34, flag=wx.EXPAND)
        layout.Add(button_35, flag=wx.EXPAND)
        layout.Add(button_36, flag=wx.EXPAND)
        layout.Add(button_24, flag=wx.EXPAND)
        layout.Add(button_25, flag=wx.EXPAND)
        layout.Add(button_26, flag=wx.EXPAND)
        layout.Add(button_38, flag=wx.EXPAND)
        layout.Add(button_39, flag=wx.EXPAND)
        layout.Add(button_40, flag=wx.EXPAND)
        layout.Add(button_41, flag=wx.EXPAND)
        layout.Add(button_42, flag=wx.EXPAND)

        layout.Add(button_53, flag=wx.EXPAND)
        layout.Add(button_52, flag=wx.EXPAND)
        layout.Add(text, flag=wx.EXPAND)


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
