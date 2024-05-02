import boto3

class SMClient:
    
    def __init__(self) -> None:
        self.session = boto3.Session()
        self.__client = self.session.client("secretsmanager")

    def get_secret_value(self, secret_name):
        response = self.__client.get_secret_value(SecretId=secret_name)
        return response["SecretString"]
