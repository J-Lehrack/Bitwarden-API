from dotenv import dotenv_values
from app.bitwarden.bitwarden import Bitwarden

config = dotenv_values(r"/.app/env")
bw_client_id = config["BW_CLIENT_ID"]
bw_client_secret = config["BW_CLIENT_SECRET"]

token = Bitwarden.get_access_token(bw_client_id, bw_client_secret)

org_members = Bitwarden.get_members(token)

format_members = Bitwarden.format_data(org_members)

print(format_members)
