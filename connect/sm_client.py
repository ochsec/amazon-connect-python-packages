import os
import boto3
from dotenv import load_dotenv

class SMClient:
    
    def __init__(self) -> None:
        self.session = boto3.Session()
        load_dotenv()
        self.__connect_rds_secret = os.getenv("CONNECT_RDS_SECRET")
        self.__client = self.session.client("secretsmanager")

    def get_rds_password(self):
        response = self.__client.get_secret_value(SecretId=self.__connect_rds_secret)
        return response["SecretString"]
