#!/bin/bash
if [ -z $1 ]; then
  echo "Usage: $0 'nodename'"
  exit;
fi

#if [ ! -f "out/$1-2023.pfx" ]; then
#  echo "File out/$1-2023.pfx not found, maybe it is named differently?"
if [ ! -f "out/$1.aero.org.pfx" ]; then
  echo "File out/$1.aero.org.pfx not found, maybe it is named differently?"
  exit;
fi

if [ -f out/$1/$1.pem ]; then
  echo "The out/$1/$1.pem file appears to already exist, maybe delete it?"
  exit;
fi

if [ -f out/$1/$1.key ]; then
  echo "The out/$1/$1.key file appears to already exist, maybe delete it?"
  exit;
fi

mkdir -p out/$1
PIS=`/opt/puppetlabs/puppet/bin/eyaml decrypt -f passin_pass_eyaml`
POS=`/opt/puppetlabs/puppet/bin/eyaml decrypt -f passout_pass_eyaml`

#openssl pkcs12 -in out/${1}-2023.pfx -nocerts -out out/${1}/${1}.key -passin pass:${PIS} -passout pass:${POS}
#openssl pkcs12 -in out/${1}-2023.pfx -clcerts -nokeys -out out/${1}/${1}.crt -passin pass:${PIS} -passout pass:${POS}
openssl pkcs12 -in out/${1}.aero.org.pfx -nocerts -out out/${1}/${1}.key -passin pass:${PIS} -passout pass:${POS}
openssl pkcs12 -in out/${1}.aero.org.pfx -clcerts -nokeys -out out/${1}/${1}.crt -passin pass:${PIS} -passout pass:${POS}
