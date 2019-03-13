# coding: UTF-8

# NoblesServant1.0
# develop by Apologems all rights reserved

import wx
import os
import webbrowser
import sys



sys.stdout = open(os.devnull, "w")


# URL LIST
url_1 ="https://jp.techcrunch.com"
url_2 ="http://gigazine.net"
url_3 ="https://www.4gamer.net"
url_4 ="https://www.inside-games.jp"
url_5 ="http://www.sukumizu.jp"
url_6 ="http://imasnews765.com"
url_7 ="http://photoshopvip.net"
url_8 ="http://ae-users.com/jp"
url_9 ="https://www.pixiv.net"
url_10 ="https://mail.google.com/mail"
url_11 ="https://tweetdeck.twitter.com/#"
url_12 ="http://www.nicovideo.jp"
url_13 ="https://www.trivago.jp"
url_14 ="https://twipla.jp"
url_15 ="http://digigame-expo.org/"
url_16 ="http://google.com"
url_A ="https://unity3d.com/jp"
url_B ="https://www.assetstore.unity3d.com/jp/?stay"
url_C ="https://icon.jp"
# 2019/03/02追加分
url_D ="https://bowlroll.net/" # bowlroll
url_E ="http://seiga.nicovideo.jp/tag/MMD%E3%83%A2%E3%83%87%E3%83%AB%E9%85%8D%E5%B8%83%E3%81%82%E3%82%8A?sort=image_created" # 静画配布
url_F = "https://www.nicovideo.jp/tag/MMD%E3%83%A2%E3%83%87%E3%83%AB%E9%85%8D%E5%B8%83%E3%81%82%E3%82%8A?sort=f&order=d" #動画配布
url_G = "https://www6.atwiki.jp/vpvpwiki/" # VPVP
url_H = "https://ch.nicovideo.jp/BeamManP" # ビームマンPの家
url_I = "https://artjuku.com/3d-cg-free-model/" # フリー3Dモデルまとめ
url_J = "https://dova-s.jp/" # フリー音楽配布サイト
url_K = "https://soundeffect-lab.info/" # 効果音ラボ
url_L = "https://commons.nicovideo.jp/materials/" # ニコニ・コモンズ素材ライブラリ
url_M = "https://www.acecombat.jp/" # エースコンバット公式
url_N = "https://ugsf-series.com/" # UGSFシリーズ公式

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

def click_button_A(event):
    webbrowser.open(url_A)

def click_button_B(event):
    webbrowser.open(url_B)

def click_button_C(event):
    webbrowser.open(url_C)
# 2019/03/02追加分
def click_button_D(event):
    webbrowser.open(url_D)

def click_button_E(event):
    webbrowser.open(url_E)

def click_button_F(event):
    webbrowser.open(url_F)

def click_button_G(event):
    webbrowser.open(url_G)

def click_button_H(event):
    webbrowser.open(url_H)

def click_button_I(event):
    webbrowser.open(url_I)

def click_button_J(event):
    webbrowser.open(url_J)

def click_button_K(event):
    webbrowser.open(url_K)

def click_button_L(event):
    webbrowser.open(url_L)

def click_button_M(event):
    webbrowser.open(url_M)

def click_button_N(event):
    webbrowser.open(url_N)

# 基礎処理
class Main(wx.Frame):
    def __init__(self, parent, id, title):
        # TITLE
        title = "Nobles Servant2"
        message="\n\r\n\rNobles\n\rServant2"

        # パネル設定
        wx.Frame.__init__(self, parent, id, title, size=(890, 760), pos=(500, 50))
        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour('#2b2b2b')

        # ボタン設定
        button_1 = wx.Button(panel, wx.ID_ANY, 'TechCrunch\n\rJapan', size=(90, 90))
        button_2 = wx.Button(panel, wx.ID_ANY, 'GIGAZINE', size=(90, 90))
        button_3 = wx.Button(panel, wx.ID_ANY, '4GAMER.net', size=(90, 90))
        button_4 = wx.Button(panel, wx.ID_ANY, 'INSIDE', size=(90, 90))
        button_5 = wx.Button(panel, wx.ID_ANY, '駿河電力\n\rスク水.jp', size=(90, 90))
        button_6 = wx.Button(panel, wx.ID_ANY, 'imas news 765', size=(90, 90))
        button_7 = wx.Button(panel, wx.ID_ANY, 'PhotoShopVip', size=(90, 90))
        button_8 = wx.Button(panel, wx.ID_ANY, 'AEP Project', size=(90, 90))
        button_9 = wx.Button(panel, wx.ID_ANY, 'PIXIV', size=(90, 90))
        button_10 = wx.Button(panel, wx.ID_ANY, 'GMAIL', size=(90, 90))
        button_11 = wx.Button(panel, wx.ID_ANY, 'TweetDeck', size=(90, 90))
        button_12 = wx.Button(panel, wx.ID_ANY, 'NicoNico', size=(90, 90))
        button_13 = wx.Button(panel, wx.ID_ANY, 'trivago\n\rホテル予約', size=(90, 90))
        button_14 = wx.Button(panel, wx.ID_ANY, 'twipla\n\rツイプラ', size=(90, 90))
        button_15 = wx.Button(panel, wx.ID_ANY, 'デジゲー博', size=(90, 90))
        #button_16 = wx.Button(panel, wx.ID_ANY, 'Google', size=(90, 90))
        button_A = wx.Button(panel, wx.ID_ANY, 'Unity 3D', size=(90, 90))
        button_B = wx.Button(panel, wx.ID_ANY, 'Unity\n\rAsset', size=(90, 90))
        button_C = wx.Button(panel, wx.ID_ANY, 'ICON\n\rDTMポータル', size=(90, 90))
        # 2019/03/12 追加
        button_D = wx.Button(panel, wx.ID_ANY, 'bowlroll', size=(90, 90))
        button_E = wx.Button(panel, wx.ID_ANY, 'MMDモデル配布\n\r(静画)', size=(90, 90))
        button_F = wx.Button(panel, wx.ID_ANY, 'MMDモデル配布\n\r(動画)', size=(90, 90))
        button_G = wx.Button(panel, wx.ID_ANY, 'VPVP Wiki', size=(90, 90))
        button_H = wx.Button(panel, wx.ID_ANY, 'ビームマンPの\n\rブロマガ', size=(90, 90))
        button_I = wx.Button(panel, wx.ID_ANY, 'フリー3Dモデル\n\rまとめ', size=(90, 90))
        button_J = wx.Button(panel, wx.ID_ANY, 'フリーBGM\n\rDOVA SYNDROME', size=(90, 90))
        button_K = wx.Button(panel, wx.ID_ANY, '効果音ラボ', size=(90, 90))
        button_L = wx.Button(panel, wx.ID_ANY, 'ニコニ・コモンズ\n\r素材ライブラリ', size=(90, 90))
        button_M = wx.Button(panel, wx.ID_ANY, 'エースコンバット\n\r公式', size=(90, 90))
        button_N = wx.Button(panel, wx.ID_ANY, 'UGSFシリーズ\n\r公式', size=(90, 90))

        # fontカラー
        font = wx.Font(11.5, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,  False, "メイリオ")
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
        #button_16.SetFont(font)
        button_A.SetFont(font)
        button_B.SetFont(font)
        button_C.SetFont(font)
    #2019/03/12 追加
        button_D.SetFont(font)
        button_E.SetFont(font)
        button_F.SetFont(font)
        button_G.SetFont(font)
        button_H.SetFont(font)
        button_I.SetFont(font)
        button_J.SetFont(font)
        button_K.SetFont(font)
        button_L.SetFont(font)
        button_M.SetFont(font)
        button_N.SetFont(font)

        # ボタンカラー
        button_1.SetBackgroundColour('#3c3f41')
        button_2.SetBackgroundColour('#3c3f41')
        button_3.SetBackgroundColour('#3c3f41')
        button_4.SetBackgroundColour('#3c3f41')
        button_5.SetBackgroundColour('#3c3f41')
        button_6.SetBackgroundColour('#3c3f41')
        button_7.SetBackgroundColour('#3c3f41')
        button_8.SetBackgroundColour('#3c3f41')
        button_9.SetBackgroundColour('#3c3f41')
        button_10.SetBackgroundColour('#3c3f41')
        button_11.SetBackgroundColour('#3c3f41')
        button_12.SetBackgroundColour('#3c3f41')
        button_13.SetBackgroundColour('#3c3f41')
        button_14.SetBackgroundColour('#3c3f41')
        button_15.SetBackgroundColour('#3c3f41')
        #button_16.SetBackgroundColour('#3c3f41')
        button_A.SetBackgroundColour('#3c3f41')
        button_B.SetBackgroundColour('#3c3f41')
        button_C.SetBackgroundColour('#3c3f41')
    #2019/03/02追加
        button_D.SetBackgroundColour('#3c3f41')
        button_E.SetBackgroundColour('#3c3f41')
        button_F.SetBackgroundColour('#3c3f41')
        button_G.SetBackgroundColour('#3c3f41')
        button_H.SetBackgroundColour('#3c3f41')
        button_I.SetBackgroundColour('#3c3f41')
        button_J.SetBackgroundColour('#3c3f41')
        button_K.SetBackgroundColour('#3c3f41')
        button_L.SetBackgroundColour('#3c3f41')
        button_M.SetBackgroundColour('#3c3f41')
        button_N.SetBackgroundColour('#3c3f41')

        # ボタン文字色
        button_1.SetForegroundColour('#a9b7c6')
        button_2.SetForegroundColour('#a9b7c6')
        button_3.SetForegroundColour('#a9b7c6')
        button_4.SetForegroundColour('#a9b7c6')
        button_5.SetForegroundColour('#a9b7c6')
        button_6.SetForegroundColour('#a9b7c6')
        button_7.SetForegroundColour('#a9b7c6')
        button_8.SetForegroundColour('#a9b7c6')
        button_9.SetForegroundColour('#a9b7c6')
        button_10.SetForegroundColour('#a9b7c6')
        button_11.SetForegroundColour('#a9b7c6')
        button_12.SetForegroundColour('#a9b7c6')
        button_13.SetForegroundColour('#a9b7c6')
        button_14.SetForegroundColour('#a9b7c6')
        button_15.SetForegroundColour('#a9b7c6')
        #button_16.SetForegroundColour('#a9b7c6')
        button_A.SetForegroundColour('#a9b7c6')
        button_B.SetForegroundColour('#a9b7c6')
        button_C.SetForegroundColour('#a9b7c6')
    # 2019/03/12
        button_D.SetForegroundColour('#a9b7c6')
        button_E.SetForegroundColour('#a9b7c6')
        button_F.SetForegroundColour('#a9b7c6')
        button_G.SetForegroundColour('#a9b7c6')
        button_H.SetForegroundColour('#a9b7c6')
        button_I.SetForegroundColour('#a9b7c6')
        button_J.SetForegroundColour('#a9b7c6')
        button_K.SetForegroundColour('#a9b7c6')
        button_L.SetForegroundColour('#a9b7c6')
        button_M.SetForegroundColour('#a9b7c6')
        button_N.SetForegroundColour('#a9b7c6')

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
        #button_16.Bind(wx.EVT_LEFT_DOWN, click_button_16)
        button_A.Bind(wx.EVT_LEFT_DOWN, click_button_A)
        button_B.Bind(wx.EVT_LEFT_DOWN, click_button_B)
        button_C.Bind(wx.EVT_LEFT_DOWN, click_button_C)
        # 2019/03/12追加
        button_D.Bind(wx.EVT_LEFT_DOWN, click_button_D)
        button_E.Bind(wx.EVT_LEFT_DOWN, click_button_E)
        button_F.Bind(wx.EVT_LEFT_DOWN, click_button_F)
        button_G.Bind(wx.EVT_LEFT_DOWN, click_button_G)
        button_H.Bind(wx.EVT_LEFT_DOWN, click_button_H)
        button_I.Bind(wx.EVT_LEFT_DOWN, click_button_I)
        button_J.Bind(wx.EVT_LEFT_DOWN, click_button_J)
        button_K.Bind(wx.EVT_LEFT_DOWN, click_button_K)
        button_L.Bind(wx.EVT_LEFT_DOWN, click_button_L)
        button_M.Bind(wx.EVT_LEFT_DOWN, click_button_M)
        button_N.Bind(wx.EVT_LEFT_DOWN, click_button_N)
        # アイコン呼び出し

        # パネルレイアウト
        layout = wx.GridSizer(rows=5, cols=6, gap=(1, 1))
        # メッセージ表示
        message = wx.StaticText(panel, wx.ID_ANY, message, style=wx.TE_CENTER)
        message.SetForegroundColour('#EEEEFF')
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" )
        message.SetFont(font)

        # パーツ配置
        layout.Add(message, flag=wx.GROW)
        layout.Add(button_12, flag=wx.SHAPED)
        layout.Add(button_9, flag=wx.SHAPED)
        layout.Add(button_1, flag=wx.SHAPED)
        layout.Add(button_2, flag=wx.SHAPED)
        layout.Add(button_3, flag=wx.SHAPED)
        layout.Add(button_4, flag=wx.SHAPED)
        layout.Add(button_7, flag=wx.SHAPED)
        layout.Add(button_8, flag=wx.SHAPED)
        layout.Add(button_C, flag=wx.SHAPED)
        layout.Add(button_D, flag=wx.SHAPED)
        layout.Add(button_E, flag=wx.SHAPED)
        layout.Add(button_F, flag=wx.SHAPED)
        layout.Add(button_G, flag=wx.SHAPED)
        layout.Add(button_H, flag=wx.SHAPED)
        layout.Add(button_I, flag=wx.SHAPED)
        layout.Add(button_J, flag=wx.SHAPED)
        layout.Add(button_K, flag=wx.SHAPED)
        layout.Add(button_L, flag=wx.SHAPED)
        layout.Add(button_A, flag=wx.SHAPED)
        layout.Add(button_B, flag=wx.SHAPED)
        layout.Add(button_15, flag=wx.SHAPED)
        layout.Add(button_6, flag=wx.SHAPED)
        layout.Add(button_5, flag=wx.SHAPED)
        layout.Add(button_13, flag=wx.SHAPED)
        layout.Add(button_11, flag=wx.SHAPED)
        layout.Add(button_10, flag=wx.SHAPED)
        layout.Add(button_14, flag=wx.SHAPED)
        layout.Add(button_M, flag=wx.SHAPED)
        layout.Add(button_N, flag=wx.SHAPED)
        #layout.Add(button_16, flag=wx.SHAPED)

        panel.SetSizer(layout)
        self.Show(True)

# 画面表示
def main():
    app = wx.App()
    Main(None, wx.ID_ANY, "hoge")
    app.MainLoop()
if __name__ == "__main__":
    main()