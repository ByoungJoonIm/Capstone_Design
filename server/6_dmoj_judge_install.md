# Dmoj judge 설치

```
$ apt install git python-dev python-pip build-essential
$ git clone https://github.com/DMOJ/judge
$ cd judge
$ pip install -r requirements.txt
$ sudo python setup.py develop
```

수많은 헤더파일 에러


- 해결

```
apt-get install libseccomp-dev
```

```
dmoj-autoconf > config.yml
```
