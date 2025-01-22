import requests
import json

from configReader import readConfig
from printMessage import printMessage


def main():
    config = readConfig()
    domain = config['domain']
    api_token_id = config['apiTokenId']
    api_token_secret = config['apiTokenSecret']

    if domain == "" or api_token_id == "" or api_token_secret == "":
        printMessage("Check configuration file!")
        return

    headers = {
        "Authorization": f"Token {api_token_id}:{api_token_secret}"
    }

    response = requests.get(
        f"{domain}/api/users",
        headers=headers
    )

    if response.status_code == 200:
        printMessage(json.dumps(response.json(), indent=2))
    else:
        printMessage(f"Failed to retrieve users: {response.status_code} - {json.dumps(response.json(), indent=2)}")

if __name__ == '__main__':
    main()
