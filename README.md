# videofarm
a scrapy based application for educational purposes only.
tested to run in Ubuntu by envoking run.sh

the following needs to be defined in run.py
- os.system('cd /home/videofarm/videofarm/')
- os.system('PATH=$PATH:/usr/local/bin')
- os.system('export PATH')
- os.system('scrapy crawl youtube -a query=6KZ1kvIUFrU')
- os.system('cd -')
