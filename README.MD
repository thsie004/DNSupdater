# A script to update server IP on Google Domain

Requires an external shell script to operate in the following manner:

```bash
username=[your_username]
password=[your_password]
currentIP=$(sh getIP.sh)

python DNSupdate.py $username $password $currentIP
```

Replace square brackets with personal information, and adjust directory path for getIP.sh accordingly.
