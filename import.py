import argparse
import json

import requests

from configReader import readConfig
from printMessage import printMessage
from userPreparer import prepareFileToImport


def main():
    config = readConfig()

    parser = argparse.ArgumentParser(description='Process some parameters.')
    parser.add_argument('--file', type=str, required=True, help='The CSV file to import')
    args = parser.parse_args()

    file_to_import = args.file
    printMessage(f'File to import: {file_to_import}')

    data = prepareFileToImport(file_to_import, config)

    for user in data:
        printMessage("Adding user: " + user['name'])

        domain = config['domain']
        api_token_id = config['apiTokenId']
        api_token_secret = config['apiTokenSecret']

        if domain == "" or api_token_id == "" or api_token_secret == "":
            printMessage("Check configuration file!")
            return

        headers = {
            "Authorization": f"Token {api_token_id}:{api_token_secret}"
        }

        response = requests.post(
            f"{domain}/api/users",
            headers=headers,
            json=user
        )

        if response.status_code == 200:
            printMessage("User added!")
        else:
            printMessage(f"Failed to add user: {response.status_code} - {json.dumps(response.json(), indent=2)}")

if __name__ == '__main__':
    main()
