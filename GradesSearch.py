import requests
from bs4 import BeautifulSoup
import Login
import Cookies

# 地址
url = "http://wx.sends.cc/school/grade"

# 请求头（写各种格式的地方）（传输数据的格式是json）
headers = {"content-type":"application/json"}

# json中的payload传输形式，来提交参数
payload = {
    "gssession":Login.gs_session_id_value,
    "weu":Cookies.gs_session_id_value2
}

params3 = {"param3":"data"}

response = requests.post(url,json=payload,headers=headers,params=params3)
 
if response.status_code == 200:
    data2 = response.json()
    data3 = data2['data']
    keys = ['KCM','XF','ZCJ','XSZCJMC','KCXZDM_DISPLAY']
    values = []
    for item in data3:
        values.append({key: item.get(key) for key in keys})
#   print(values)
    print("OK")
else:
    print("Error:", response.status_code)