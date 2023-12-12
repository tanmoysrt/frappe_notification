import requests

class FrappeNotification:
    CENTRAL_SERVER_ENDPOINT = "http://notification.relay:8000"
    PROJECT_NAME = ""
    SITE_NAME = ""
    API_KEY = ""
    API_SECRET = ""

    def __init__(self) -> None:
        raise NotImplementedError
    
    @staticmethod
    def setSiteName(site_name: str) -> None:
        FrappeNotification.SITE_NAME = site_name

    @staticmethod
    def setProjectName(project_name: str) -> None:
        FrappeNotification.PROJECT_NAME = project_name
    
    @staticmethod
    def setCredential(api_key: str, api_secret: str) -> None:
        FrappeNotification.API_KEY = api_key
        FrappeNotification.API_SECRET = api_secret

    # Add Token (User)
    @staticmethod
    def addToken(user_id: str, token: str) -> bool:
        res = FrappeNotification._sendPostRequest("/api/method/notification_relay.api.token.add",  {
            "user_id": user_id,
            "fcm_token": token
        })
        if res[0]:
            return res[1]["success"]
        else:
            raise Exception(res[1])

    # Remove Token (User)
    @staticmethod
    def removeToken(user_id: str, token: str) -> bool:
        res = FrappeNotification._sendPostRequest("/api/method/notification_relay.api.token.remove",  {
            "user_id": user_id,
            "fcm_token": token
        })
        if res[0]:
            return res[1]["success"]
        else:
            raise Exception(res[1])

    # Add Topic
    def addTopic(topic_name: str) -> bool:
        res = FrappeNotification._sendPostRequest("/api/method/notification_relay.api.topic.add",  {
            "topic_name": topic_name
        })
        if res[0]:
            return res[1]["success"]
        else:
            raise Exception(res[1]["message"])

    # Remove Topic
    @staticmethod
    def removeTopic(topic_name: str) -> bool:
        res = FrappeNotification._sendPostRequest("/api/method/notification_relay.api.topic.remove",  {
            "topic_name": topic_name
        })
        if res[0]:
            return res[1]["success"]
        else:
            raise Exception(res[1])

    # Subscribe Topic (User)
    @staticmethod
    def subscribeTopic(user_id: str, topic_name: str) -> bool:
        res = FrappeNotification._sendPostRequest("/api/method/notification_relay.api.topic.subscribe",  {
            "user_id": user_id,
            "topic_name": topic_name
        })
        if res[0]:
            return res[1]["success"]
        else:
            raise Exception(res[1])

    # Unsubscribe Topic (User)
    @staticmethod
    def unsubscribeTopic(user_id: str, topic_name: str) -> bool:
        res = FrappeNotification._sendPostRequest("/api/method/notification_relay.api.topic.unsubscribe",  {
            "user_id": user_id,
            "topic_name": topic_name
        })
        if res[0]:
            return res[1]["success"]
        else:
            raise Exception(res[1])

    # Send notification (User)
    @staticmethod
    def sendNotificationToUser(user_id: str, title: str, content: str) -> bool:
        res = FrappeNotification._sendPostRequest("/api/method/notification_relay.api.send_notification.user",  {
            "user_id": user_id,
            "title": title,
            "content": content
        })
        if res[0]:
            return res[1]["success"]
        else:
            raise Exception(res[1])

    # Send notification (Topic)
    @staticmethod
    def sendNotificationToTopic(topic_name: str, title: str, content: str) -> bool:
        res = FrappeNotification._sendPostRequest("/api/method/notification_relay.api.send_notification.topic",  {
            "topic_name": topic_name,
            "title": title,
            "content": content
        })
        if res[0]:
            return res[1]["success"]
        else:
            raise Exception(res[1])


    @staticmethod
    def _sendPostRequest(route: str, params:dict) -> (bool, dict):
        try:
            headers = {
                "Authorization": f"token {FrappeNotification.API_KEY}:{FrappeNotification.API_SECRET}"
            }
            body = FrappeNotification._injectStaticInfo(params)
            response = requests.post(FrappeNotification._createRoute(route), params=params, json=body, headers=headers)
            if response.status_code == 200:
                responseJson = response.json()
                return True, responseJson["message"]
            else:
                text = response.text
                return False, {"message": "request failed", "status_code": response.status_code, "error": text}
        except Exception as e:
            return False, {"message": str(e)}
        
    @staticmethod
    def _createRoute(route: str) -> str:
        return FrappeNotification.CENTRAL_SERVER_ENDPOINT + FrappeNotification._formatRoute(route)
        
    @staticmethod
    def _formatRoute(route: str) -> str:
        if not route.startswith("/"):
            route = "/" + route
        if route.endswith("/"):
            route = route[:-1]
        return route

    @staticmethod
    def _injectStaticInfo(query: dict) -> dict:
        query["project_name"] = FrappeNotification.PROJECT_NAME
        query["site_name"] = FrappeNotification.SITE_NAME
        return query