# import requests

from apis.base_api import BaseApi


class WeWork(BaseApi):

    def __init__(self, corp_id, corp_secret):
        self.token = self.get_access_token(corp_id, corp_secret)

    def get_access_token(self, corp_id, corp_secret):
        """
                获取 access_token
                :return:
        """
        # 定义凭证
        # corp_id = "ww876064acebf0fa3c"
        # corp_secret = "A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9YxY"

        # url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"

        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corp_id,
                "corpsecret": corp_secret
            }
        }
        # r = requests.request("GET", url)
        r = self.send_api(req)
        token = r.json()["access_token"]
        return token


# mc = WeWork()
# mc.get_access_token()
