import requests
import json
from dotenv import dotenv_values


class Bitwarden(object):
    """
    Accesses the Bitwarden public API
    Precondition: bw_client_id and bw_client_secret are valid credentials. Go to Org > Settings > Org Info > API Key
    """
    @staticmethod
    def get_access_token(client_id: str, client_secret: str):
        """Uses bw_client_id and bw_client_secret to retrieve access token."""
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        data = f"grant_type=client_credentials&scope=api.organization&client_id={client_id}&client_secret={client_secret}"

        response = requests.post('https://identity.bitwarden.com/connect/token', headers=headers, data=data)
        return response.json()["access_token"]

    @staticmethod
    def get_members(access_token):
        """Uses access_token to retrieve Organization Members"""
        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(f'https://api.bitwarden.com/public/members', headers=headers)
        return response.json()

    @staticmethod
    def format_data(data):
        layout = json.dumps(data, sort_keys=True, indent=3)
        print(layout)


if __name__ == "__main__":
    config = dotenv_values(r"/.env")
    bw_client_id = config["BW_CLIENT_ID"]
    bw_client_secret = config["BW_CLIENT_SECRET"]

    token = Bitwarden.get_access_token(bw_client_id, bw_client_secret)

    print("Access token,", token, "secured.")
