import requests
from bs4 import BeautifulSoup

# 地址
url = "http://wx.sends.cc/7758c813f8d64c668994ac7ddd829535/"

# 请求头（写各种格式的地方）（传输数据的格式是json）
headers = {"content-type":"application/json"}

# json中的payload传输形式，来提交参数
payload = {
    "stunum":"stunum",
    "password":"password"
}

params1 = {"param1":"GS_SESSIONID"}

response = requests.post(url,json=payload,headers=headers,params=params1)

if response.status_code == 200:
    data1 = response.json()
#   print(data1)
    print("OK")
else:
    print("Error:", response.status_code)

gs_session_id_value = data1['data']['GS_SESSIONID']