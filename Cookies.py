import requests
from bs4 import BeautifulSoup
import Login

# 地址
url = "http://wx.sends.cc/school/jwc"

# 请求头（写各种格式的地方）（传输数据的格式是json）
headers = {"content-type":"application/json"}

# json中的payload传输形式，来提交参数
payload = {
    "cookie":Login.gs_session_id_value
}

params2 = {"param2":"data"}

response = requests.post(url,json=payload,headers=headers,params=params2)
 
if response.status_code == 200:
    data2 = response.json()
#   print(data2)
    print("OK")
else:
    print("Error:", response.status_code)

gs_session_id_value2 = data2['data']