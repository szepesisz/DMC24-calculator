import logging

from calculator.app import main as app_main


logger = logging.getLogger(__name__)


def main():
    app_main()


if __name__ == '__main__':
    main()