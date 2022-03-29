
class User():

    def __init__(self, user_type, user_id, device_id, password, subscription_type=""):
        self.user_type = user_type
        self.user_id = user_id
        self.device_id = device_id
        self.password = password
        self.subscription_type = subscription_type