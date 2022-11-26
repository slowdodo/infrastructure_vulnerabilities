
| service       | Function           |
| ------------- | ---------------------- |
| echo(7)       |
| discard(9)    |
| daytime(13)   |
| chargen(19)   |
| NTP(123)      |
| DNS(53)       |
| SNMP(161/162) |
| SMMP(25)      |

# deny

* vim /etc/xinet.d/echo
* vim /etc/xinet.d/discard
* vim /etc/xinet.d/daytime
* vim /etc/xinet.d/chargen

``` bash
service echo
{
	disable = yes
	id = echo-stream
	type = internal
	wait = no
	socket_type = stream
}

```
