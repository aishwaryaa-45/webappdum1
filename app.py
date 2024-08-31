from flask import Flask
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

# Replace with your Key Vault name
KEY_VAULT_NAME = "keyvalut123w"
SECRET_NAME = "MySecretKey"

# Create a SecretClient using DefaultAzureCredential
KV_URI = f"https://{KEY_VAULT_NAME}.vault.azure.net"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KV_URI, credential=credential)

# Fetch the secret from Azure Key Vault
secret = client.get_secret(SECRET_NAME)

@app.route('/')
def index():
    return f"Retrieved secret: {secret.value}"

if __name__ == "__main__":
    app.run(debug=True)
