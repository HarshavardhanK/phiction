from openai import OpenAI
from prompts.OpenAI.get_secrets import get_open_ai_keys

#A class wrapper for OpenAI Client to interact with ChatGPT

class Client:
    '''
    A class to interact with OpenAI ChatGPT API

    Purpose - Defines a client to interact with OpenAI ChatGPT API. 
    The client can be used to generate text based on a given prompt.
    
    '''
    def __init__(self, model, org_id=None, proj_id=None):
        '''
        Parameters - Model, Organization ID, Project ID
        @Model - The model to use for generating text
        @Organization ID - The organization ID for the OpenAI API
        @Project ID - The project ID for the OpenAI API

        '''
        self.model = model
        self.org_id = org_id
        self.proj_id = proj_id

        self.client = self.set_client()

    def set_client(self):

        KEYS = get_open_ai_keys() #Get the keys from AWS Secrets Manager

        return OpenAI(
                    organization=KEYS['OPEN_AI_ORG_ID'],
                    project=f'{KEYS['OPEN_AI_PROJ_ID']}',
                    api_key=KEYS['OPENAI_API_KEY']
                )
    
    def _test_client(self, prompt):

        try:
            return self.client.chat.completions.create(
                        model=self.model,
                        messages=[{"role": "user", "content": f"{prompt}"}],
                        max_tokens=100,  
                        temperature=0.7
                    ).choices[0].message.content
    
        except Exception as e:
            print(f"Error generating text: {e}")

        return None
    
if __name__ == '__main__':
    client = Client('gpt-4-turbo')
    print(client.client)
    prompt = "Generate a short story about a dragon and a princess"
    print(client._test_client(prompt))