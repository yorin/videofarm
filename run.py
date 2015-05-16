#!/usr/bin/python
#script to call scrapy from root in python
"""
http://stackoverflow.com/questions/13437402/how-to-run-scrapy-from-within-a-python-script
"""
os.system('cd /home/werby/videofarm/videofarm/')
os.system('PATH=$PATH:/usr/local/bin')
os.system('export PATH')
os.system('scrapy crawl youtube -a query=6KZ1kvIUFrU')
os.system('cd -')
exit
