UF=`cat /tmp/1`

for i in ${UF[@]}; do

ldapsearch -H ldap://dc01.test.local -y ~/.ldappw -x -W -D "ldapsearchuser@test.local" -b "dc=test,dc=local" "(&(objectCategory=Person)(sAMAccountName=${i}))" sAMAccountName mail -LLL

done
