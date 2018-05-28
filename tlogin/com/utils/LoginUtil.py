import uuid
class LoginUtil:
    @staticmethod
    def genGuid():
        return (uuid.uuid4().hex).replace("-", "")