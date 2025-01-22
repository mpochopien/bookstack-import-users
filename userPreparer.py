import csv


def prepareFileToImport(fileName, config):
    data = []
    with open(fileName, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(
                {
                    "name": row[0],
                    "email": row[1],
                    "language": config["defaultLanguage"],
                    "roles": [3],
                    "send_invite": config["sendInvite"]
                }
            )
    return data