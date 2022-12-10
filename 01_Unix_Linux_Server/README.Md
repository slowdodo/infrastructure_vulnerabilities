# Root account remote connect session limit

> /etc/ssh/sshd_config

``` bash
PermitRootLogin no
```
## port change (auto scanning and macro brute force attack deny)

It can avoid the attacks of general script kid-level and attackers and large-scale auto-scanning red team attack,  
but it has the disavantage of non standard and annoying. 
However, it should be noted that port can be replaced 

``` bash
Port 52000
```

``` bash
sudo service ssh reload && \
sudo service ssh status
```

``` bash
sudo ufw enable
```

``` bash
sudo ufw allow 52000/tcp
```

> other shell
``` bash
ssh dodo@10.10.1.8 -p 52000
```
## delete or disable

if u don't want openssh server, it is recommended to delete or disable it.

### disable

``` bash
sudo service ssh stop && \
sudo service ssh status
```

### delete

``` bash
sudo apt -y remove openssh-server
```

--------------------------------------------------------------------------------------------------------------------------------

# linux password config

> /etc/login.defs
``` bash
PASS_MAX_DAYS 90 
PASS_MIN_DAYS 1
PASS_WARN_AGE 5

LOGIN_TIMEOUT 300 # 5MIN
LOGIN_RETRIES 5

ENCRYPT_METHOD sha512
```

## pwquality

``` bash
sudo apt install libpam-pwquality
```

> /etc/pam.d/common-password
``` bash
sudo apt-get install libpam-pwquality
```
> /etc/pam.d/common-auth
``` bash
password        requisite                       pam_pwquality.so retry=3 minlen=8 minclass=3
password        [success=1 default=ignore]      pam_unix.so obscure use_authtok try_first_pass yescrypt remember=5 sha512
```

| Recommanded Value | function                      | description				| 
| ----------------- |-------------------------------| ------------------------- |
| lcredit=-1        | min lower lens                | min lower lens 1			|
| ucredit=-1        | min upper lens                | min upper lens 1			|
| dcredut=-1        | min digit lens                | min digit lens 1			|
| ocredut=-1        | min Special char lens         | min Special char lens 1	|
| minlen=8          | min passwd lens               | min passwd lens 1			|
| difok=10          | compare witch existing passwd | default value 10			|  

--------------------------------------------------------------------------------------------------------------------------------

# R-Host command
Remote access such as rlogin, rexec, and rsh is very convenient, but it becomes a   part that is prone to vulnerabilities when real services are used.  
Personally, I recommend using a secure authentication connection such as ssh, but if you really want to use it, please follow the instructions below.  

## critical 
* /etc/host.equiv: server setting file
* /etc/.rhosts.equiv: individual user setting file

``` bash
sudo chown root /etc/rhosts.qeuiv && \
sudo chmod 600 /etc/rhosts.qeuiv 
```

``` bash
ls -al $HOME/.rhosts
```


--------------------------------------------------------------------------------------------------------------------------------

# su 

> /etc/pam.d/su
``` bash
auth       required   pam_wheel.so debug group=wheel
auth       required   pam_wheel.so debug use_uid
```
