#!/usr/bin/env python
import requests
import ConfigParser
import sys
import os
from cement.core.foundation import CementApp
from cement.utils.misc import init_defaults


def main(path):
    #If you don't want to use a config file, hardcode your host and port and comment out config lines
    fpath = os.path.join(os.path.dirname(__file__), 'config.ini')
    config = ConfigParser.ConfigParser()
    config.read(fpath)
    host = config.get('hdfs_env', 'host')
    port = config.get('hdfs_env', 'port')
    if (not host or not port):
            raise ValueError('Please add hdfs host and port to your config file')

    if len(sys.argv) <= 1:
            raise ValueError("Expected dir!")
    payload={'op': 'LISTSTATUS'}
    request_url = 'http://{0}:{1}/webhdfs/v1{2}'.format(host, port, path)
    r = requests.get(request_url, params=payload)
    result = r.json()
    status_list = result['FileStatuses']
    for status in status_list['FileStatus']:
        # print(status['owner'] + '\t' + status['type'] + '\t' + status['pathSuffix'])
        print(status['pathSuffix'])


# define our default configuration options
defaults = init_defaults('pdfs')

def my_cleanup_hook(app):
    pass

class pdfs(CementApp):
     class Meta:
        label = 'pdfs'
        config_defaults = defaults
        hooks = [
            ('pre_close', my_cleanup_hook),
        ]


with pdfs() as app:
    app.args.add_argument('-ls', '--list', action='store', metavar='STRING',
                          help='List the contents of a directory', dest='ls')
    # run the application
    app.run()

    # continue with additional application logic
    if app.pargs.ls:
        main(app.pargs.ls)


