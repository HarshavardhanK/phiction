import boto3
import json
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def get_secret(secret_name):
    # Create a Secrets Manager client
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


if __name__ == "__main__":
    session = boto3.Session()
  
    
    region_name = session.region_name  # Adjust as needed

    secret = get_secret(secret_name, region_name)
    if secret:
        # Parse the JSON string to extract the API key
        secret_dict = json.loads(secret)
        api_key = secret_dict.get("api_key")  # Adjust the key to match your secret's structure
        print(f"Retrieved API key: {api_key}")
