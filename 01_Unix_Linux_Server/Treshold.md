``` bash
auth required /lib/security/pam_tally.so deny=5 unlock_time=120 no_magic_root
auth required /lib/security/pam_tally.so no_magic_root reset
```
