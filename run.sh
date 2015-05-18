#!/bin/bash
export QUERY="$2"
export SPIDER="$1"
DIRPAT=$(readlink -f $(dirname ${BASH_SOURCE[0]}))
cd $DIRPAT/videofarm/spiders/
PATH=$PATH:/usr/local/bin
export PATH
function scraperon {
  scrapy crawl "$SPIDER" -a query="$QUERY" -o ../spiders/cache/"$QUERY".json
}
function curly {
 LINKER=$(cat ../spiders/cache/$QUERY.json |grep -Po '"urlstream": "(.*?)"'|sed -e "s/\"//g"|sed -e "s/urlstream\: //g")
 LINKTITLE=$(cat ../spiders/cache/$QUERY.json |grep -Po '"youtubetitle": "(.*?)"'|sed -e "s/\"//g" |sed -e "s/youtubetitle\: //g")
 if [ ! -f "../downloads/$LINKTITLE.mp4" ] && [ ! -s "../downloads/$LINKTITLE.mp4" ] && [ ! -e "../downloads/$LINKTITLE.mp4" ]; then
   curl "$LINKER" -a -k -o "../downloads/$LINKTITLE.mp4" --limit-rate 56k
 else
   echo "$LINKTITLE.mp4 has already been downloaded!"
 fi
}
 CDATEEPOCH=$(date +%s)
 if [ ! -f "../spiders/cache/$QUERY.json" ] && [ ! -s "../spiders/cache/$QUERY.json" ] && [ ! -e "../spiders/cache/$QUERY.json" ]; then
   scraperon
 else
   CACHEFDATE=`stat -c %Y "../spiders/cache/$QUERY.json"`
 fi
   DIFF=$(($CACHEFDATE - $CDATEEPOCH))
   if [ "$DIFF" -le "0" ] || [ "$CACHEFDATE" -eq "0" ]; then
     curly
   else
     rm -rf ../spiders/cache/$QUERY.json
     scraperon
     curly
   fi
cd - > /dev/null 2>&1
exit 0
