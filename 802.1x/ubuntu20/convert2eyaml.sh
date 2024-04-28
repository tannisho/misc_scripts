#!/bin/bash
if [ -z $1 ]; then
  echo "Usage: $0 'nodename'"
  exit;
fi

if [ ! -f "out/$1.pfx" ]; then
  echo "File out/$1.pfx not found, maybe it is named differently?"
  exit;
fi

if [ -d out/$1 ]; then
  echo "The out/$1 directory appears to already exist, maybe delete it?"
  exit;
fi

mkdir out/$1
PIS=`/opt/puppetlabs/puppet/bin/eyaml decrypt -f passin_pass_eyaml`
POS=`/opt/puppetlabs/puppet/bin/eyaml decrypt -f passout_pass_eyaml`

openssl pkcs12 -in out/${1}.test.local.pfx -nocerts -out out/${1}/${1}_key_tmp -passin pass:${PIS} -passout pass:${POS}
#openssl pkcs12 -in out/${1}-2023.pfx -clcerts -nokeys -out out/${1}/${1}_crt_tmp -passin pass:${PIS} -passout pass:${POS}
openssl pkcs12 -in out/${1}.test.local.pfx -clcerts -nokeys -out out/${1}/${1}_crt_tmp -passin pass:${PIS} -passout pass:${POS}

/opt/puppetlabs/puppet/bin/eyaml encrypt -o string -f out/${1}/${1}_crt_tmp > out/${1}/${1}_crt_enc
/opt/puppetlabs/puppet/bin/eyaml encrypt -o string -f out/${1}/${1}_key_tmp > out/${1}/${1}_key_enc

echo "# check /etc/netplan/01-netcfg.yaml on node for custom" >> out/${1}/${1}.test.local.yaml 
echo "# network settings before applying this class." >> out/${1}/${1}.test.local.yaml 
echo "#classes:" >> out/${1}/${1}.test.local.yaml
echo "#  - 'profile::nac'" >> out/${1}/${1}.test.local.yaml
echo "" >> out/${1}/${1}.test.local.yaml
echo "pem_key: `cat out/${1}/${1}_crt_enc`" >> out/${1}/${1}.test.local.yaml
echo "priv_key: `cat out/${1}/${1}_key_enc`" >> out/${1}/${1}.test.local.yaml

rm -rf out/${1}/${1}_*
