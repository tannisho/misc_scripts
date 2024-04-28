WD=/root/boltcl/tsusers
SD=$WD/scripts
XRDPD=$WD/xrdp_servers
XRDPDLS=`ls $XRDPD`
HDL=/tmp/hdlist.txt

eyaml decrypt -f $SD/password_map|sed '/---/d' | awk -F":" '{print $1":"$2}' > $HDL

for i in ${XRDPDLS[@]}; do

  bolt file upload $HDL $HDL --targets ${i}
  bolt script run $SD/chkdir.py --targets ${i}

done

rm -rf $HDL
