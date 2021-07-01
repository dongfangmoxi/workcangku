"""日程信息描述，只关注业务，不需要断言
"""
from GraduationProject.Apiauto.apis.weworks import WeWorks


class Events(WeWorks):
    def create_event(self, create_data):
        """
            创建日程
        :return: 创建日程接口的响应
        """
        req = {
            "method": "post",
            'url': f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{self.calendar_id}/events',
            'headers': {
                "Authorization": f"Bearer {self.tenant_access_token}",
                "Content-Type": "application/json; charset=utf-8"
            },
            'json': create_data
        }
        r = self.send_api(req)
        return r.json()

    def get_event(self):
        """
            查询日程
        :return:
        """
        req = {
            'method': 'get',
            'url': f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{self.calendar_id}/events',
            'headers': {
                "Authorization": f"Bearer {self.tenant_access_token}"
            }
        }
        r = self.send_api(req)
        return r.json()

    def update_event(self, event_id, update_data):
        """
            更新日程
        :return:
        """
        # event_id = 'aea633f5-bf1d-4b1c-8f9b-3af91c08421b_0',
        req = {
            'method': 'patch',
            'url': f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{self.calendar_id}/events/{event_id}',
            'headers': {
                "Authorization": f"Bearer {self.tenant_access_token}",
                "Content-Type": "application/json; charset=utf-8"
            },
            'json': update_data
        }
        r = self.send_api(req)
        return r.json()

    def delete_event(self, event_id):
        """
            删除日程
        :return:
        """
        # event_id = 'aea633f5-bf1d-4b1c-8f9b-3af91c08421b_0'
        req = {
            'method': 'delete',
            'url': f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{self.calendar_id}/events/{event_id}',
            'headers': {
                "Authorization": f"Bearer {self.tenant_access_token}"
            }
        }
        r = self.send_api(req)
        return r.json()
