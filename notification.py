from typing import Self


class FrappeNotification(object):
    CENTRAL_SERVER_ENDPOINT = "http://notification.relay:8000"
    PROJECT_ID = ""
    API_KEY = ""
    instance = None

    def __new__(cls) -> Self:
        if not cls.instance:
            cls.instance = super().__new__(cls)

    def __init__(self) -> None:
        raise NotImplementedError
    
    @staticmethod
    def setCredential(project_id: str, api_key: str) -> None:
        FrappeNotification.PROJECT_ID = project_id
        FrappeNotification.API_KEY = api_key

    # Add Web App
    # Fetch config of Web App
    # Add Topic
    # Remove Topic
    # Exists Topic
    # List Topic
    # Add Token (User)
    # Remove Token (User)
    # Subscribe Topic (User)
    # Unsubscribe Topic (User)
    # Send notification (User)
    # Send bulk notification (User)
    # Send notification (Topic)
    # Send bulk notification (Topic)