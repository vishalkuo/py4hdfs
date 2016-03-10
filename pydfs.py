#!/usr/bin/env python
import requests
import ConfigParser
import sys
import os

def main():
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
    path = sys.argv[1]
    payload={'op': 'LISTSTATUS'}
    request_url = 'http://{0}:{1}/webhdfs/v1{2}'.format(host, port, path)
    r = requests.get(request_url, params=payload)
    result = r.json()
    status_list = result['FileStatuses']
    for status in status_list['FileStatus']:
    	# print(status['owner'] + '\t' + status['type'] + '\t' + status['pathSuffix'])
    	print(status['pathSuffix'])



if __name__ == '__main__':
    main()