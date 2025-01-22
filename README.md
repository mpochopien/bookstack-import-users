# bookstack-import-users
Script to BookStack, to quickly import user accounts from CSV

## Usage

1. Clone this repository
2. Create a CSV file with two columns: name and email
3. Configure `settings.json`
3. Run the script with the following command:

```bash
python import.py --file=users.csv
```

You can also run test with the following command:

```bash
python test.py
```

This will test configuration and list users

## Settings

- `domain`: URL of your BookStack instance
- `apiTokenId`: API Token ID - navigate to `Settings` -> `Users` and create a new token for specific user
- `apiTokenSecret`: API Token Secret
- `defaultLanguage`: Default language for new users (e.g. `en`)
- `sendInvite`: Send invite to new users (true/false)