#!/usr/bin/env python
'''CustomerDB-Update

Usage:
    customerdb-update [ -b | --build-number ] <bnum>
    customerdb-update [ -h | --version ]
    customerdb-update [ -v | --version ]

Options:
    -h --help           Show this screen.
    -v --version        Show version information
    -b --build-number   Input Jenkins build-number
'''

# about
__author__ = 'Andrew Kuttor'
__maintainer__ = 'Andrew Kuttor'
__email__ = 'andrew_kuttor@intuit.com'
__version__ = '1.0.0'


from docopt import DocoptExit, docopt
import customerdbsqllib as cdb  # Lib of CustomerDB SQL statments
from scrapenv import parser, source_code as sc  # Exports EnvInject vars by build number


def main():
    try:
        args = docopt(__doc__, version='CustomerDB-Update - v1.0')
        build_number = args['<bnum>']

        # Snag the goodies (env vars)
        # source = sc(build_number)
        # envars = parser(source)

        # Import the googies into DB
        # Psuedo-code cdb...insert


    except DocoptExit as e:
        print(e.message)


if __name__ == "__main__":
    main()
