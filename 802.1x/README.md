---
script convert2eyaml.sh:
converts .pfx cert and creates a yaml file with eyaml encrypted cert and key
places file in out/'hostname' directory
execute as: ./convert2eyaml.sh 'hostname'
for fips enabled systems, execute as: bash convert2eyaml.sh 'hostname'


script convert.sh:
converts .pfx cert and places the cert and key in out/'hostname' directory
execute as: ./convert.sh 'hostname'
for fips enabled systems, execute as: bash convert.sh 'hostname'

-- 
the 'out' directory is not git managed, so it will need to be created
prior to running these scripts. 
--
the unconverted .pfx cert needs to be in the 'out' directory.
--
the scripts rely on the puppet server keys, this should be symlinked, eg:

${SCRIPT_DIR}/802.1x/cent7/keys -> /opt/.puppetlabs/keys
${SCRIPT_DIR}/802.1x/ubuntu20/keys -> /opt/.puppetlabs/keys
