# ■ 取得するデータの種類
# ------------------------------------------------------------------------------------
# statsDataId="0003287301"は、政府統計「火災報告」のデータ。 
# このデータは消防庁がまとめたもので、火災の発生件数などの統計情報が含まれる。

# ■ エンドポイントと機能
# ------------------------------------------------------------------------------------
# エンドポイント: https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData 
# 機能: e-Stat APIの主要な口（エンドポイント）。
#       パラメータを指定することで、特定の統計データをJSON形式で取得する。

import requests

APP_ID = "1df068268bd0ed04616641210aaf4a6fdea0b639"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId": "0003287301", #
    "metaGetFlg": "Y", #メタ情報（データの分類や定義など）を取得する設定
    "cntGetFlg": "N", # 統計の数値データを取得するかどうかの設定
    "explanationGetFlg": "Y", # 解説情報を取得する設定
    "annotationGetFlg": "Y", # 注釈情報を取得する設定
    "sectionHeaderFlg": "1", # セクションヘッダ（統計表の項目名など）の表示フラグ
    "replaceSpChars": "0", # 特殊文字の置換設定。0は置換しない
    "lang": "J",  # 日本語を指定
}

# APIからデータ取得
response = requests.get(API_URL, params=params)
# JSONに変換
data = response.json()
# １０件のみデータ表示
print("【１０件のみデータ表示】")
values =data["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"]["VALUE"]
for i in values[:10]:
    print(f'年月：{i["@time"]}, 発生件数：{i["$"]}{i["@unit"]}')