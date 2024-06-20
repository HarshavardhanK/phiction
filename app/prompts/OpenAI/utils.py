import json

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def get_secret(secret_name):
    # Create a Secrets Manager client
    session = boto3.Session()
    region_name = session.region_name

    client = boto3.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        # Retrieve the secret value
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )

        return get_secret_value_response['SecretString']
    
    except NoCredentialsError:
        print("No credentials provided to access AWS Secrets Manager")
        
    except PartialCredentialsError:
        print("Incomplete credentials provided to access AWS Secrets Manager")
        
    except Exception as e:
        print(f"Error retrieving secret: {e}")
        
    
    return None

def get_open_ai_keys():

    secret_name = "dev/phiction/openai/keys"

    secret = get_secret(secret_name)

    try:
        secret_dict = json.loads(secret)

        return {
            'OPEN_AI_ORG_ID': secret_dict.get("OPENAI_ORG_ID"),
            'OPEN_AI_PROJ_ID': secret_dict.get("OPENAI_PROJ_ID"),
            'OPENAI_API_KEY': secret_dict.get("OPENAI_API_KEY")
        }
    
    except Exception as e:
        print(f"Error parsing secret {secret} - {e}")

    return None

def test():

    session = boto3.Session()

    secret_name = "dev/phiction/openai/keys"
  
    print(get_open_ai_keys())


if __name__ == "__main__":
    test()