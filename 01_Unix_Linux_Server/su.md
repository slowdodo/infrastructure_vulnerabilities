# 

> /etc/pam.d/su
``` bash
auth       required   pam_wheel.so debug group=wheel
auth       required   pam_wheel.so debug use_uid
```
