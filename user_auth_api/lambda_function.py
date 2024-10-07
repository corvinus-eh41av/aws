import json
from auth import Authenticator


def lambda_handler(event, context):
    # TODO implement
    try:
        a = Authenticator
        user_token = event['headers']['auth-token']

        is_authenticated = a.is_authenticated_user(user_token)
        
        if is_authenticated:
            return {
                'statusCode': 200,
                'body': json.dumps('authorised')
            }
        return {
                'statusCode': 401,
                'body': json.dumps('not authorised')
            }
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing query parameter q'})
        }
    except ValueError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid value for q'})
        }

