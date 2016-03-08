#!/usr/bin/env python
import requests
import ConfigParser

def main():
	config = ConfigParser.ConfigParser()
	config.read('config.ini')
	host = config.get('hdfs_env', 'host')
	port = config.get('hdfs_env', 'port')
	if (not host  or not port):
		raise ValueError('Please add hdfs host and port to your config file')

	



if __name__ == '__main__':
	main()