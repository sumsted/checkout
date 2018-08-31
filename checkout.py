import requests

class Checkout:

    def __init__(self, username, password, host, port):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.response = None
        self.oauth2_token = None

    def get_oauth2_token(self, username, password):
        response = None

        self.oauth2_token = None

    def get_checkout(self, path, header):
        response = None
        status_code = None

        return status_code, response

    def post_checkout(self, path, header, request):
        response = None
        status_code = None

        return status_code, response
        

    
    
