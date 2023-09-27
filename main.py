from hotprices_au import woolies, coles
import argparse
import logging


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--quick', action='store_true', default=False)
    parser.add_argument('--debug', action='store_true', default=False)
    parser.add_argument('store', choices=['woolies', 'coles'])
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    match args.store:
        case 'woolies':
            woolies.main(args.quick)
        case 'coles':
            coles.main(args.quick)


if __name__ == '__main__':
    main()