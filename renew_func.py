import requests
import json


def renew_func(args):
    url = f"https://my.aeza.net/api/services/{args.id}/prolong"
    headers = {'X-API-Key': args.token}
    data = {
        "method": "balance",
        "term": "hour",
        "count": args.count
    }

    r = requests.post(url, headers=headers, json=data)

    parsed = json.loads(r.content)
    print(json.dumps(parsed, indent=2))
