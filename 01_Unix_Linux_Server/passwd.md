# linux(RHEL7, Ubuntu 20~) password config

``` bash
sudo vim /etc/login.defs
```
``` bash
PASS_MAX_DAYS 90 
PASS_MIN_DAYS 1
PASS_WARN_AGE 5

LOGIN_TIMEOUT 60
LOGIN_RETRIES 5

ENCRYPT_METHOD sha512
```

``` bash
sudo apt install libpam-pwquality
```

## other setting

> /etc/pam.d/common-password
``` bash
sudo apt-get install libpam-pwquality
```

``` bash
password        requisite                       pam_pwquality.so retry=4 minlen=9 difok=4 lcredit=-2 ucredit=-2 dcredit=-1 ocredit=-1 reject_username enforce_for_root
password        [success=1 default=ignore]      pam_unix.so obscure use_authtok try_first_pass yescrypt remember=10 sha512
```

| Recommanded Value | function                      | description				| 
| ----------------- |-------------------------------| ------------------------- |
| lcredit=-1        | min lower lens                | min lower lens 1			|
| ucredit=-1        | min upper lens                | min upper lens 1			|
| dcredut=-1        | min digit lens                | min digit lens 1			|
| ocredut=-1        | min Special char lens         | min Special char lens 1	|
| minlen=8          | min passwd lens               | min passwd lens 1			|
| difok=10          | compare witch existing passwd | default value 10			|  

# what is yescrpy?

It is a recently invented cryptographic scheme to prevent gpu operation.  
Since the gpu opration is twice as slow as before, it can defend against attacks such as bruteforce

# /etc/passwd

use cut filter, and see policy 

> other login policy check filter
``` bash
cat /etc/passwd | grep -v "/nologin"
```

> password not save to /etc/shadow location check 
``` bash
cat /etc/passwd | cut -d: -f2 | grep -v x
```
