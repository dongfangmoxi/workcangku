from GraduationProject.Apiauto.apis.baseapi import BaseApi


# 获取token类
class WeWorks(BaseApi):
    def __init__(self):
        self.tenant_access_token = self.get_tenant_access_token()
        self.calendar_id = self.get_calendar_id()

    def get_tenant_access_token(self):
        """
            获取 tenant_access_token
        """
        req = {
            'method': 'post',
            'url': 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/',
            'json': {
                "app_id": "cli_a051b8714bb8500e",
                "app_secret": "UQDmRVGoMzoorMf7UsMcJfQWrUm0Xz1e"
            }
        }
        r = self.send_api(req)
        tenant_access_token = r.json()["tenant_access_token"]
        return tenant_access_token

    def get_calendar_id(self):
        """
            获取calendar_id,用于日程管理
        :return: calendar_id
        """
        req = {
            'method': 'get',
            'url': 'https://open.feishu.cn/open-apis/calendar/v4/calendars',
            'headers': {
                "Authorization": f"Bearer {self.tenant_access_token}",
                "Content-Type": "application/json; charset=utf-8"
            }
        }
        r = self.send_api(req)
        calendar_id = r.json()["data"]['calendar_list'][0]['calendar_id']
        return calendar_id
