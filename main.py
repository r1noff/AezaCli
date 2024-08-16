import argparse
import os

from renew_func import renew_func
from info_func import info_func
from keepup_func import keepup_func

parser = argparse.ArgumentParser(description='Command-line tool for interaction with aeza.net')

token = os.environ.get("AEZA_TOKEN")
parser.add_argument("--token", "-t", default=token, required=token is None)

service_parser = argparse.ArgumentParser(add_help=False)
service_id = os.environ.get("AEZA_SERVICE_ID")
service_parser.add_argument("--id", default=service_id, required=service_id is None)

subparsers = parser.add_subparsers()

renew_help = "Renew service for *count* hours"
renew_parser = subparsers.add_parser("renew", parents=[service_parser], help=renew_help, description=renew_help)
renew_parser.add_argument("count", type=int, default=1, nargs="?")
renew_parser.set_defaults(func=renew_func)

info_help = "Get info about service"
info_parser = subparsers.add_parser("info", parents=[service_parser], help=info_help, description=info_help)
info_parser.set_defaults(func=info_func)

keepup_help = "Renews service if it close to removal"
keepup_parser = subparsers.add_parser("keepup", parents=[service_parser], help=keepup_help, description=keepup_help)
keepup_parser.set_defaults(func=keepup_func)

args = parser.parse_args()
args.func(args)
