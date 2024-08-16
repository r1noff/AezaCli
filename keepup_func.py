import time

from info_func import get_service_json, get_service_expiration_timestamp
from renew_func import renew_func


def keepup_func(args):
    beyond_timestamp = 82790  # 22h:59m:50s
    service = get_service_json(args.id, args.token)
    timestamp = get_service_expiration_timestamp(service)

    if time.time() - timestamp > beyond_timestamp:
        args.count = 1
        renew_func(args)
