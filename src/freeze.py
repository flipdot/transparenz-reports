#!/usr/bin/env python3

from pathlib import Path

from flask_frozen import Freezer
from app import app


def main():
    app.config['FREEZER_DESTINATION'] = '../build'
    freezer = Freezer(app)
    freezer.freeze()
    with open(Path(freezer.root) / 'CNAME', 'w') as f:
        f.write('transparenz.flipdot.org')


if __name__ == '__main__':
    main()
