#!/bin/bash

cd /home/werby/videofarm/videofarm/
PATH=$PATH:/usr/local/bin
export PATH
scrapy crawl youtube -a query=6KZ1kvIUFrU
cd -
exit 0
