import requests


appid = wxf64d39f0756b3f70
secret = da5da13fd71812c61cb08bc1e8a569b0

def get_access_token():
    access_token = requests.get(https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET)
    return access_token