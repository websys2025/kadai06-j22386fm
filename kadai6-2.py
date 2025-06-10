# ■ 参照するオープンデータの名前
#------------------------------------------------------------------------------------
# 港区公衆無線LANアクセスポイント位置情報（Minato_City_Wi-Fi）
# 提供元：東京都　港区

# ■ オープンデータの概要
# ------------------------------------------------------------------------------------
# 港区が区内の施設等に設置している公衆無線LAN「Minato City Wi-Fi」の
# アクセスポイントに関する情報。
# 具体的には、設置施設の名称、住所、緯度経度、提供しているSSID（Wi-Fiのネットワーク名）
# などの情報が含まれている。

# ■ エンドポイントと機能
# ------------------------------------------------------------------------------------
# エンドポイント: https://opendata.city.minato.tokyo.jp/dataset/
# ec151316-0fbd-4646-8cfa-4039b98be199/resource/685fa9f8-f5ae-4f36-bc2e-d1bda933e5c0/download/131032_public_wireless_lan.json
# 機能: このURLにHTTP GETリクエストを送ることで、港区の公衆無線LANアクセスポイントの
#       最新の一覧データをJSON形式で取得することができる。

# ■ プログラムの使い方
# ------------------------------------------------------------------------------------
# このプログラムを実行すると、上記のAPIエンドポイントからデータを取得し、
# 内容を整形してコンソールに一覧表示。
# 特別なパラメータは不要で、実行するだけで結果が得られる。

import requests

url = "https://opendata.city.minato.tokyo.jp/dataset/ec151316-0fbd-4646-8cfa-4039b98be199/resource/685fa9f8-f5ae-4f36-bc2e-d1bda933e5c0/download/131032_public_wireless_lan.json"

response = requests.get(url)
data = response.json()

access_points_list = data.get("features", [])

print("\n--- 港区公衆無線LANアクセスポイント 名称一覧 ---")
    
# forループを使い、リストから各アクセスポイントの情報（辞書）を一つずつ取り出す
for feature in access_points_list:
    # 各アクセスポイント情報の中から、さらに "properties" というキーで中の辞書を取り出す
    properties = feature.get("properties", {})
    
    name = properties.get("名称")
    adrs = properties.get("所在地_連結表記")
    
    print(f"-  名称 ：{name}")
    print(f"- 所在地：{adrs}")
    print()