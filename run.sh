#!/bin/bash


export QUERY="$1"
cd ../videofarm/videofarm/spiders/
PATH=$PATH:/usr/local/bin
export PATH
function scraperon {
#scrapy crawl youtube -a query=6KZ1kvIUFrU
scrapy crawl youtube -a query=$QUERY -o ../spiders/cache/$QUERY.json
}
function curly {
LINKER=$(cat ../spiders/cache/$QUERY.json |grep -Po '"urlstream": "(.*?)"'|sed -e "s/\"//g"|sed -e "s/urlstream\: //g")
LINKTITLE=$(cat ../spiders/cache/$QUERY.json |grep -Po '"youtubetitle": "(.*?)"'|sed -e "s/\"//g" |sed -e "s/youtubetitle\: //g")
#echo $LINKER $LINKTITLE
curl "$LINKER" -a -k -o "../downloads/$LINKTITLE.mp4" --limit-rate 56k
#curl http://r2---sn-2aqu-hoad.googlevideo.com/videoplayback?ratebypass=yes&mime=video%2Fmp4&expire=1431708337&initcwndbps=1101250&sver=3&dur=744.663&ipbits=0&pl=20&itag=18&mm=31&ip=122.52.86.12&key=yt5&ms=au&source=youtube&upn=mkTwVJ0pWNg&mv=m&mt=1431686625&id=o-AGQqw48F-lzy8VsUTG3QmaWbhiPkpXHtupvOgjMLjV1f&fexp=9407478%2C9408142%2C9408710%2C945137%2C948124%2C952612%2C952637%2C952640%2C952642&signature=4BC91A710F1E0364F867AE3B12A7569D10EAD26F.B610544A016E56E4DA2BD47D1B466F875EB90F68&sparams=dur%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Cmime%2Cmm%2Cms%2Cmv%2Cpl%2Cratebypass%2Csource%2Cupn%2Cexpire -a -k -o test.mp4

}
  CDATEEPOCH=$(date +%s) #UTC datetime
  if [ ! -f "../spiders/cache/$QUERY.json" ] && [ ! -s "../spiders/cache/$QUERY.json" ] && [ ! -e "../spiders/cache/$QUERY.json" ]; then
   scraperon
  else
   CACHEFDATE=`stat -c %Y "../spiders/cache/$QUERY.json"`
  fi
   DIFF=$(($CACHEFDATE - $CDATEEPOCH))
   if [ "$DIFF" -le "0" ] || [ "$CACHEFDATE" -eq "0" ]; then
    echo "still a day old $DIFF $CACHEFDATE $CDATEEPOCH"
    curly
   else
    rm -rf ../spiders/cache/$QUERY.json
    scraperon
    curly
   fi
cd -
exit 0
