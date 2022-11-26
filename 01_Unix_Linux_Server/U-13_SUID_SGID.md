# delete

``` bash
chmod -s <file name>
```

# check
find / -user root -type f \( -perm -04000 -o -perm -02000 \) -xdev 
 -exec ls –al {} \;

#/usr/bin/chgrp <group_name> <setuid_file_name>
#/usr/bin/chmod 4750 <setuid_file_name>
