from azure.identity import InteractiveBrowserCredential
from dotenv import load_dotenv
import os

class Graph_Auth:
    device_code_credential: InteractiveBrowserCredential
    token: str

    def __init__(self):
        load_dotenv()
        client_id = os.getenv('CLIENT_ID')
        tenant_id = os.getenv('TENANT_ID')
        graph_scopes = os.getenv('GRAPH_SCOPES')
        self.device_code_credential = InteractiveBrowserCredential(
            client_id=client_id, 
            tenant_id=tenant_id,
            timeout=5
        )
        self.token = self.device_code_credential.get_token(graph_scopes)
        
    def get_access_token(self):
        return self.token.token
    
    def close_window(self):
        self.device_code_credential.close()
        
