import logging
import sys

from emailrouter.testsuite import Tester


def main():
    logging.basicConfig(level=logging.INFO)

    tester = Tester('testsuite')
    return int(not tester.test_all())


if __name__ == '__main__':
    sys.exit(main())
