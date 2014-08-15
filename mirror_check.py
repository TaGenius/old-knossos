## Copyright 2014 ngld <ngld@tproxy.de>
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##     http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.

from __future__ import absolute_import, print_function
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(threadName)s:%(module)s.%(funcName)s: %(message)s')

import sys
import argparse
import json
import time
import six
from six.moves.urllib.request import urlopen, Request
from six.moves.urllib.error import URLError

from lib import util


def check(url, meth='HEAD'):
    try:
        kwargs = {
            'headers': {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'}
        }

        if six.PY3:
            kwargs['method'] = meth

        result = urlopen(Request(url, **kwargs))
        result.close()
        return True
    except URLError:
        return False
    except KeyboardInterrupt:
        raise
    except:
        logging.exception('Failed to check url "%s"!', url)
        return False


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('checksumfile', help='Repo configuration.')
    parser.add_argument('reportfile', help='The file that will contain the generated report.')

    args = parser.parse_args(args)

    logging.info('Reading repo configuration...')
    with open(args.checksumfile, 'r') as stream:
        mods = json.load(stream)

    report = {}
    for mid, mod in mods.items():
        if mid[0] == '#':
            continue

        logging.info('Checking mod "%s"...', mod['title'])

        mrep = report[mod['title']] = {}

        for urls, files in mod['files']:
            for name in files:
                if name not in mrep:
                    mrep[name] = {}

                for url in urls:
                    mrep[name][url] = check(util.pjoin(url, name))

    logging.info('Writing report...')
    report['#generated'] = time.strftime('%d.%m.%Y %H:%M GMT', time.gmtime())

    with open(args.reportfile, 'w') as stream:
        json.dump(report, stream, separators=(',', ':'))

    logging.info('Done')


if __name__ == '__main__':
    main(sys.argv[1:])
