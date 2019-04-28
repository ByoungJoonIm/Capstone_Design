# 필요 라이브러리 설치

```
# 필요 라이브러리
apt install git gcc g++ make python-dev libxml2-dev libxslt1-dev zlib1g-dev gettext curl

# 파이썬 2.7
wget -q --no-check-certificate -O- https://bootstrap.pypa.io/get-pip.py | sudo python
# 파이썬 3.5
apt install python3-pip

# 가상환경
pip3 install virtualenv

# nodesource
wget -O- https://deb.nodesource.com/setup_8.x | sudo -E bash -

# nodejs
apt install nodejs

# npm permission
npm install -g sass pleeease-cli --unsafe-perm
```

---

# DB

[https://downloads.mariadb.org/mariadb/repositories/](https://downloads.mariadb.org/mariadb/repositories/)

- 10.2 version download

```
apt install libmysqlclient-dev
mysql -uroot -p
mariadb> CREATE DATABASE dmoj DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_general_ci;
mariadb> GRANT ALL PRIVILEGES ON dmoj.* to 'dmoj'@'localhost' IDENTIFIED BY '<password>';
mariadb> exit
```

# virtualenv

```
#파이썬 3.5
virtualenv -p /usr/bin/python3 dmojsite/
#파이썬 2.7
virtualenv dmojsite/

. dmojsite/bin/activate
```

# git

```
git clone https://github.com/DMOJ/site.git
cd site
git submodule init
git submodule update
```

# dependencies

```
pip3 install -r requirements.txt
pip3 install mysqlclient
```

---


# django

## local_setting

```
cd dmoj
vi local_settings.py
```

```python
#####################################
########## Django settings ##########
#####################################
# See <https://docs.djangoproject.com/en/1.11/ref/settings/>
# for more info and help. If you are stuck, you can try Googling about
# Django - many of these settings below have external documentation about them.
#
# The settings listed here are of special interest in configuring the site.

# SECURITY WARNING: keep the secret key used in production secret!
# You may use <http://www.miniwebtool.com/django-secret-key-generator/>
# to generate this key.
SECRET_KEY = 'This key is not very secure and you should change it.'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Change to False once you are done with runserver testing.

# Uncomment and set to the domain names this site is intended to serve.
# You must do this once you set DEBUG to False.
#ALLOWED_HOSTS = ['dmoj.ca']

# Optional apps that DMOJ can make use of.
INSTALLED_APPS += (
)

# Caching. You can use memcached or redis instead.
# Documentation: <https://docs.djangoproject.com/en/1.11/topics/cache/>
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    }
}

# Your database credentials. Only MySQL is supported by DMOJ.
# Documentation: <https://docs.djangoproject.com/en/1.11/ref/databases/>
DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dmoj',
        'USER': 'dmoj',
        'PASSWORD': '<password>',
        'HOST': '127.0.0.1',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'sql_mode': 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION',
        },
    }
}

# Sessions.
# Documentation: <https://docs.djangoproject.com/en/1.11/topics/http/sessions/>
#SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Internationalization.
# Documentation: <https://docs.djangoproject.com/en/1.11/topics/i18n/>
LANGUAGE_CODE = 'en-ca'
DEFAULT_USER_TIME_ZONE = 'America/Toronto'
USE_I18N = True
USE_L10N = True
USE_TZ = True

## django-compressor settings, for speeding up page load times by minifying CSS and JavaScript files.
# Documentation: https://django-compressor.readthedocs.io/en/latest/
COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
STATICFILES_FINDERS += ('compressor.finders.CompressorFinder',)


#########################################
########## Email configuration ##########
#########################################
# See <https://docs.djangoproject.com/en/1.11/topics/email/#email-backends>
# for more documentation. You should follow the information there to define
# your email settings.

# Use this if you are just testing.
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# The following block is included for your convenience, if you want
# to use Gmail.
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = '<your account>@gmail.com'
#EMAIL_HOST_PASSWORD = '<your password>'
#EMAIL_PORT = 587

# To use Mailgun, uncomment this block.
# You will need to run `pip install django-mailgun` for to get `MailgunBackend`.
#EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
#MAILGUN_ACCESS_KEY = '<your Mailgun access key>'
#MAILGUN_SERVER_NAME = '<your Mailgun domain>'

# You can also use Sendgrid, with `pip install sendgrid-django`.
#EMAIL_BACKEND = 'sgbackend.SendGridBackend'
#SENDGRID_API_KEY = '<Your SendGrid API Key>'

# The DMOJ site is able to notify administrators of errors via email,
# if configured as shown below.

# A tuple of (name, email) pairs that specifies those who will be mailed
# when the server experiences an error when DEBUG = False.
ADMINS = (
    ('Your Name', 'your.email@example.com'),
)

# The sender for the aforementioned emails.
SERVER_EMAIL = 'Don Mills Online Judge <errors@dmoj.ca>'


##################################################
########### Static files configuration. ##########
##################################################
# See <https://docs.djangoproject.com/en/1.11/howto/static-files/>.

# Change this to somewhere more permanent., especially if you are using a
# webserver to serve the static files. This is the directory where all the
# static files DMOJ uses will be collected to.
# You must configure your webserver to serve this directory as /static/ in production.
STATIC_ROOT = '/tmp/static'

# URL to access static files.
#STATIC_URL = '/static/'

# Uncomment to use hashed filenames with the cache framework.
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

############################################
########## DMOJ-specific settings ##########
############################################

## DMOJ site display settings.
SITE_NAME = 'DMOJ'
SITE_LONG_NAME = 'Don Mills Online Judge'
SITE_ADMIN_EMAIL = 'admin@example.com'
TERMS_OF_SERVICE_URL = '//dmoj.ca/tos' # Use a flatpage.

## Bridge controls.
# The judge connection address and port; where the judges will connect to the site.
# You should change this to something your judges can actually connect to
# (e.g., a port that is unused and unblocked by a firewall).
BRIDGED_JUDGE_ADDRESS = [('localhost', 9999)]

# The bridged daemon bind address and port to communicate with the site.
#BRIDGED_DJANGO_ADDRESS = [('localhost', 9998)]

## DMOJ features.
# Set to True to enable full-text searching for problems.
ENABLE_FTS = True

# Set of email providers to ban when a user registers, e.g., {'throwawaymail.com'}.
BAD_MAIL_PROVIDERS = set()

## Event server.
# Uncomment to enable live updating.
#EVENT_DAEMON_USE = True

# Uncomment this section to use websocket/daemon.js included in the site.
#EVENT_DAEMON_POST = '<ws:// URL to post to>'

# If you are using the defaults from the guide, it is this:
#EVENT_DAEMON_POST = 'ws://127.0.0.1:15101/'

# These are the publicly accessed interface configurations.
# They should match those used by the script.
#EVENT_DAEMON_GET = '<public ws:// URL for clients>'
#EVENT_DAEMON_GET_SSL = '<public wss:// URL for clients>'
#EVENT_DAEMON_POLL = '<public URL to access the HTTP long polling of event server>'
# i.e. the path to /channels/ exposed by the daemon, through whatever proxy setup you have.

# Using our standard nginx configuration, these should be.
#EVENT_DAEMON_GET = 'ws://<your domain>/event/'
#EVENT_DAEMON_GET_SSL = 'wss://<your domain>/event/' # Optional
#EVENT_DAEMON_POLL = '/channels/'

# If you would like to use the AMQP-based event server from <https://github.com/DMOJ/event-server>,
# uncomment this section instead. This is more involved, and recommended to be done
# only after you have a working event server.
#EVENT_DAEMON_AMQP = '<amqp:// URL to connect to, including username and password>'
#EVENT_DAEMON_AMQP_EXCHANGE = '<AMQP exchange to use>'

## CDN control.
# Base URL for a copy of ace editor.
# Should contain ace.js, along with mode-*.js.
ACE_URL = '//cdnjs.cloudflare.com/ajax/libs/ace/1.2.3/'
JQUERY_JS = '//cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js'
SELECT2_JS_URL = '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/js/select2.min.js'
SELECT2_CSS_URL = '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/css/select2.min.css'

# A map of Earth in Equirectangular projection, for timezone selection.
# Please try not to hotlink this poor site.
TIMEZONE_MAP = 'http://naturalearth.springercarto.com/ne3_data/8192/textures/3_no_ice_clouds_8k.jpg'

## Camo (https://github.com/atmos/camo) usage.
#CAMO_URL = "<URL to your camo install>"
#CAMO_KEY = "<The CAMO_KEY environmental variable you used>"

# Domains to exclude from being camo'd.
#CAMO_EXCLUDE = ("https://dmoj.ml", "https://dmoj.ca")

# Set to True to use https when dealing with protocol-relative URLs.
# See <http://www.paulirish.com/2010/the-protocol-relative-url/> for what they are.
#CAMO_HTTPS = False

# HTTPS level. Affects <link rel='canonical'> elements generated.
# Set to 0 to make http URLs canonical.
# Set to 1 to make the currently used protocol canonical.
# Set to 2 to make https URLs canonical.
#DMOJ_HTTPS = 0

## PDF rendering settings.
# Directory to cache the PDF.
#PROBLEM_PDF_CACHE = '/home/dmoj-uwsgi/pdfcache'

# Path to use for nginx's X-Accel-Redirect feature.
# Should be an internal location mapped to the above directory.
#PROBLEM_PDF_INTERNAL = '/pdfcache'

# Path to a PhantomJS executable.
#PHANTOMJS = '/usr/local/bin/phantomjs'

# If you can't use PhantomJS or prefer wkhtmltopdf, set the path to wkhtmltopdf executable instead.
#WKHTMLTOPDF = '/usr/local/bin/wkhtmltopdf'

# Note that PhantomJS is preferred over wkhtmltopdf and would be used when both are defined.

## ======== Logging Settings ========
# Documentation: https://docs.djangoproject.com/en/1.9/ref/settings/#logging
#                https://docs.python.org/2/library/logging.config.html#logging-config-dictschema
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    'handlers': {
        # You may use this handler as example for logging to other files..
        'bridge': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '<desired bridge log path>',
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'file',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'dmoj.throttle_mail.ThrottledEmailHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'file',
        },
    },
    'loggers': {
        # Site 500 error mails.
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Judging logs as received by bridged.
        'judge.bridge': {
            'handlers': ['bridge', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        # Catch all log to stderr.
        '': {
            'handlers': ['console'],
        },
        # Other loggers of interest. Configure at will.
        #  - judge.user: logs naughty user behaviours.
        #  - judge.problem.pdf: PDF generation log.
        #  - judge.html: HTML parsing errors when processing problem statements etc.
        #  - judge.mail.activate: logs for the reply to activate feature.
        #  - event_socket_server
    },
}

## ======== Integration Settings ========
## Python Social Auth
# Documentation: https://python-social-auth.readthedocs.io/en/latest/
# You can define these to enable authentication through the following services.
#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''
#SOCIAL_AUTH_FACEBOOK_KEY = ''
#SOCIAL_AUTH_FACEBOOK_SECRET = ''
#SOCIAL_AUTH_GITHUB_SECURE_KEY = ''
#SOCIAL_AUTH_GITHUB_SECURE_SECRET = ''
#SOCIAL_AUTH_DROPBOX_OAUTH2_KEY = ''
#SOCIAL_AUTH_DROPBOX_OAUTH2_SECRET = ''

## ======== Custom Configuration ========
# You may add whatever django configuration you would like here.
# Do try to keep it separate so you can quickly patch in new settings.
```

## compile asset

```
python3 manage.py check
./make_style.sh
python3 manage.py collectstatic
python3 manage.py compilemessages
python3 manage.py compilejsi18n
```

## db

```
python3 manage.py migrate

python3 manage.py loaddata navbar
python3 manage.py loaddata language_small
python3 manage.py loaddata demo
# 관리자
python3 manage.py createsuperuser
```

## run

```
python3 manage.py runserver 0.0.0.0:8000
```

## test

```
python3 manage.py runbridged
```

- 10초 기다려보고 `ctrl+c`

## uwsgi

```
pip3 install uwsgi
vi uwsgi.ini
```

- [복사붙여넣기](https://github.com/DMOJ/docs/blob/master/sample_files/uwsgi.ini)
```
[uwsgi]
# Socket and pid file location/permission.
uwsgi-socket = /tmp/dmoj-site.sock
chmod-socket = 666
pidfile = /tmp/dmoj-site.pid

# You should create an account dedicated to running dmoj under uwsgi.
#uid = dmoj-uwsgi
#gid = dmoj-uwsgi

# Paths.
chdir = /home/jjm/site
pythonpath = /home/jjm/site
virtualenv = /home/jjm/dmojsite

# Details regarding DMOJ application.
protocol = uwsgi
master = true
env = DJANGO_SETTINGS_MODULE=dmoj.settings
module = dmoj.wsgi:application
optimize = 2

# Scaling settings. Tune as you like.
memory-report = true
cheaper-algo = backlog
cheaper = 3
cheaper-initial = 5
cheaper-step = 1
cheaper-rss-limit-soft = 201326592
cheaper-rss-limit-hard = 234881024
workers = 7
```

- 경로수정

```
chdir = /home/capston/site
pythonpath = /home/capston/site
virtualenv = /home/capston/dmojsite/bin
```


```
uwsgi --ini uwsgi.ini
```

- `ctrl+c`

## supervisord

```
apt install supervisor
cd /etc/supervisor/conf.d/
```

```
vi site.conf
vi bridged.conf
```

- [SITE 복붙](https://github.com/DMOJ/docs/blob/master/sample_files/site.conf)

```
[program:site]
command=/home/jjm/dmojsite/bin/uwsgi --ini uwsgi.ini
directory= /home/jjm/site
stopsignal=QUIT
stdout_logfile=/tmp/site.stdout.log
stderr_logfile=/tmp/site.stderr.log
```

- [bridged 복붙](https://github.com/DMOJ/docs/blob/master/sample_files/bridged.conf)

```
[program:bridged]
command= /home/jjm/dmojsite/bin/python manage.py runbridged
directory= /home/jjm/site
stopsignal=INT
# You should create a dedicated user for the bridged to run under.
user=jjm
group=jjm
stdout_logfile=/tmp/bridge.stdout.log
stderr_logfile=/tmp/bridge.stderr.log
```

```
supervisorctl update
supervisorctl status
```
- 둘다 실행이 된다면 잘된것이다

### 흔하게 안되는 경우

```
vi site/dmoj/local_settings.py

<desire ---> -> log.txt

python manage.py check
supervisorctl restart all
```



## nginx

```
apt install nginx
```

```
cd /etc/nginx/conf.d
vi nginx.conf
```

- [복사붙여넣기](https://github.com/DMOJ/docs/blob/master/sample_files/nginx.conf)

```
server {
    listen       80;
    listen       [::]:80;

    # Change port to 443 and do the nginx ssl stuff if you want it.

    # Change server name to the HTTP hostname you are using.
    # You may also make this the default server by listening with default_server,
    # if you disable the default nginx server declared.
    server_name "";

    add_header X-UA-Compatible "IE=Edge,chrome=1";
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";

    charset utf-8;
    try_files $uri @icons;
    error_page 502 504 /502.html;

    location ~ ^/502\.html$|^/logo\.png$|^/robots\.txt$ {
        root /home/jjm/site;
    }

    location @icons {
        root /home/jjm/site/resources/icons;
        error_page 403 = @uwsgi;
        error_page 404 = @uwsgi;
    }

    location @uwsgi {
        uwsgi_read_timeout 600;
        # Change this path if you did so in uwsgi.ini
        uwsgi_pass unix:///tmp/dmoj-site.sock;
        include uwsgi_params;
    }

    location /static {
        gzip_static on;
        expires max;
        root /tmp/static;
        # Comment out root, and use the following if it doesn't end in /static.
        #alias <STATIC_ROOT>;
    }

    # Uncomment if you are using PDFs and want to serve it faster.
    # This location name should be set to PROBLEM_PDF_INTERNAL.
    #location /pdfcache {
    #    internal;
    #    root <path to pdf cache diretory, without the final /pdfcache>;
    #}

    # Uncomment these sections if you are using the event server.
    #location /event/ {
    #    proxy_pass http://127.0.0.1:<event server websocket port>/;
    #    proxy_http_version 1.1;
    #    proxy_set_header Upgrade $http_upgrade;
    #    proxy_set_header Connection "upgrade";
    #    proxy_read_timeout 86400;
    #}

    #location /channels/ {
    #    proxy_read_timeout          120;
    #    proxy_pass http://127.0.0.1:<event server http port>;
    #}
}

sudo ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/nginx.conf
sudo fuser -k 80/tcp
```

- 경로 수정 필수 ,static root 수정 : /tmp

```
nginx -t
service nginx reload
```

## event

```
(dmojsite) $ cd /home/<name>/site
(dmojsite) $ cat > websocket/config.js
module.exports = {
    get_host: '127.0.0.1',
    get_port: 15100,
    post_host: '127.0.0.1',
    post_port: 15101,
    http_host: '127.0.0.1',
    http_port: 15102,
    long_poll_timeout: 29000,
};
```

- get_port should be the same as the port for /event/ in nginx.conf 
- http_port should be the same as the port for /channels/ in nginx.conf 
- post_port should be the same as the port in EVENT_DAEMON_POST in local_settings. 
- You need to configure EVENT_DAEMON_GET and EVENT_DAEMON_POLL. You need to uncomment the relevant section in the nginx configuration.

```
(dmojsite) $ npm install qu ws simplesets
(dmojsite) $ pip install websocket-client
(dmojsite) $ vi /etc/supervisor/conf.d/wsevent.conf
```

- [복사 붙여넣기](https://github.com/DMOJ/docs/blob/master/sample_files/wsevent.conf)

```
[program:wsevent]
command=/usr/bin/node /home/jjm/site/websocket/daemon.js
environment=NODE_PATH="/home/jjm/site/node_modules"
# Should create a dedicated user.
user=jjm
group=jjm
stdout_logfile=/tmp/wsevent.stdout.log
stderr_logfile=/tmp/wsevent.stderr.log
```

```
supervisorctl update
supervisorctl restart bridged
supervisorctl restart site
service nginx restart
```

```
supervisorctl restart site *****
```

# 추가적으로 오류 해결하면서 자주 쓰이는거

- db 삭제

```
[Mysql]
sudo apt-get purge mysql-server
sudo apt-get purge mysql-common



[MariaDB]
sudo apt-get purge mariadb-server
sudo apt-get purge mariadb-common



[공용작업]
sudo rm -rf /var/log/mysql
sudo rm -rf /var/log/mysql.*
sudo rm -rf /var/lib/mysql
sudo rm -rf /etc/mysql
```

- migrate 해제

```
python manage.py migrate --fake contenttypes zero
python manage.py migrate --fake flatpages zero
python manage.py migrate --fake impersonate zero
python manage.py migrate --fake judge zero
```

[https://stackoverflow.com/questions/19658891/error-2002-hy000-cant-connect-to-local-mysql-server-through-socket-var-run](https://stackoverflow.com/questions/19658891/error-2002-hy000-cant-connect-to-local-mysql-server-through-socket-var-run)
