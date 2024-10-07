import getpass

import boto3

class Authenticator:
    def is_authenticated_user(input_token):
        session = boto3.session.Session()
        client = session.client(
            service_name = 'secretsmanager',
            region_name = "us-east-1"
        )
        
        try:
            token = client.get_secret_value(
            SecretId='dev/myApp/api-token'
            )
            print(f'this is the token {token}')
            if token['SecretString'] == input_token:
                return True
            return False
        except ClientError as e:
            raise e
       
        

