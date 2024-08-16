import time

import requests
import json

from datetime import datetime


def info_func(args):
    service = get_service_json(args.id, args.token)
    timestamp = get_service_expiration_timestamp(service)
    expires_at = datetime.fromtimestamp(timestamp).strftime('%d.%m.%Y, %H:%M')
    if timestamp > time.time():
        print(f'Service "{service['name']}" expires at {expires_at}')
    else:
        print(f'Service "{service['name']}" expired at {expires_at}')


def get_service_json(id, token):
    url = f'https://my.aeza.net/api/services/{id}'
    headers = {'X-API-Key': token}
    r = requests.get(url, headers=headers)
    parsed = json.loads(r.content)
    return parsed['data']['items'][0]


def get_service_expiration_timestamp(service):
    return int(service['timestamps']['expiresAt'])