import argparse
from . import run, get_device_id, get_open_ports, say_hello,\
    get_claim_token, get_claim_url


def main():
    actions = {
        'whoami': (get_device_id, "Print device ID."),
        'portscan': (get_open_ports, "Print open ports."),
        'test-cert': (say_hello, "Validate device certificate."),
        'claim-token': (get_claim_token, "Print claim token."),
        'claim-url': (get_claim_url, "Print claim URL.")
    }
    help_string = "One of the following:\n\n" + "\n".join(
        ["{: <12} {: <}".format(k, v[1]) for k, v in actions.items()])
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="""
Let's Encrypt for IoT (with more bells and whistles).
When called without arguments, generates device certificate
or renews it if necessary.
""",
        prog="wott-agent")
    parser.add_argument('action',
                        nargs='?',
                        choices=actions.keys(),
                        metavar='action',
                        help=help_string)
    parser.add_argument(
        '--debug',
        required=False,
        action="store_true",
        help="Enable debug output.")
    parser.add_argument(
        '--dev',
        required=False,
        action="store_true",
        help="Developer mode: work with locally running server.")
    args = parser.parse_args()
    if not args.action:
        run(ping=True, debug=args.debug, dev=args.dev)
    else:
        run(ping=False, debug=args.debug, dev=args.dev)
        print(actions[args.action][0]())


if __name__ == '__main__':
    main()
