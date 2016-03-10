# pydfs
Quickly list contents of directories using a webhdfs wrapper

## About
`hdfs dfs -ls /YOUR DIR/` is slow. Webhdfs is fast. Put pydfs in your bin directory and quickly list the contents of any directory in your hdfs system. Admittedly, it's not perfect (pr's always welcome). Currently, it only lists the contents of your specified directory. Things to work on:
* Listing type of file (directory, file, etc)
* List permissions on file
* List owner of file
* Support relative dirs (somehow)

## Usage
```python
python pydfs.py 'YOUR_DIRECTORY_HERE'
```
Or, install it in your bin directory and call 
```
pydfs.py 'YOUR_DIRECTORY_HERE'
```
Note: the config file is optional. It is very easy to change the original script to not use it.
