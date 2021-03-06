"""
Django settings for djangoweb project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3722+o1i!))zulmfoh38%2(r#z&wl4qzufvmso2n1p(xaw^wld'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.mail',  # 邮件验证模块
    'apps.log',  # 日志配置模块
    'apps.chat',  # 实时聊天模块
    'channels',
    'apps.cscom',  # 自定义命令模块
    'apps.message',  # 消息提示模块
    'apps.page',  # 数据分页模块
    'apps.ajax',  # Ajax模块
    'haystack',
    'apps.search',  # 全局搜索模块
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 注意替换自己项目的名称
WSGI_APPLICATION = 'djangoweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'djangoweb',
         'USER': 'root',
         'PASSWORD': 'root',
         'HOST': '127.0.0.1',
         'PORT': 3306,
     }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 自定义认证模型系统
AUTH_USER_MODEL = 'mail.User'

# 发送邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# SMTP服务地址，使用其他服务器需更换
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
# 发送邮件的邮箱，换成自己的
EMAIL_HOST_USER = '15754324003@163.com'
# 在邮箱中设置的客户端授权密码，换成自己的
EMAIL_HOST_PASSWORD = 'mingrikejio8o2'
# 收件人看到的发件人，<>中地址必须与上方保持一致
EMAIL_FROM = 'c0c<15754324003@163.com>'

if os.path.exists(os.path.join(BASE_DIR, 'logs')) is False:
    os.mkdir(os.path.join(BASE_DIR, 'logs'))
# logs目录绝对路径
LOGS_ROOT = os.path.join(BASE_DIR, 'logs')
# 默认情况下，LOGGING设置与Django的默认logging配置进行合并
LOGGING = {
    'version': 1,  # 唯一的dictConfig格式版本。
    'disable_existing_loggers': False,  # 重新定义部分或所有的默认loggers
    # 定义两个格式化程序
    # asctime时间、threadName线程名称、thread线程号、name 记录器(loggers)的名称、lineno异常行号、
    # module执行日志记录调用的模块名称、funcName执行日志记录调用的函数名称、levelname日志记录级别的文本名称、message日志消息
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)s prototype] [%(name)s:%(lineno)s prototype] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
        },
        'simple': {
            'format': '%(asctime)s [%(threadName)s:%(thread)s prototype] [%(name)s:%(lineno)s prototype] [%(levelname)s]- %(message)s'
        }
    },
    # 定义过滤器
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'  # 其传递记录时 DEBUG是False
        }
    },
    # 定义处理程序
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'default': {
            'level': 'DEBUG',  # 日志级别
            'class': 'logging.handlers.RotatingFileHandler',  # 输出到文件
            'filename': os.path.join(LOGS_ROOT, 'all.log'),  # 日志文件，请确保修改'filename'路径为运行Django应用的用户有权限写入的一个位置
            'maxBytes': 1024 * 1024 * 5,  # 5 MB 文件大小
            'backupCount': 60,  # 备份份数
            'formatter': 'standard',  # 使用哪种日志格式
        },
        'console': {
            'level': 'DEBUG',  # 日志级别
            'class': 'logging.StreamHandler',  # 输出到控制台
            'formatter': 'standard',  # 使用哪种日志格式
        },
        'request_handler': {
            'level': 'DEBUG',  # 日志级别
            'class': 'logging.handlers.RotatingFileHandler',  # 输出到文件
            'filename': os.path.join(LOGS_ROOT, 'django_request.log'),  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 5 MB 文件大小
            'backupCount': 60,  # 备份份数
            'formatter': 'standard',  # 使用哪种日志格式
        },
        'exception_handler': {
            'level': 'DEBUG',  # 日志级别
            'class': 'logging.handlers.RotatingFileHandler',  # 输出到文件
            'filename': os.path.join(LOGS_ROOT, 'exception.log'),  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 5 MB 文件大小
            'backupCount': 60,  # 备份份数
            'formatter': 'standard',  # 使用哪种日志格式
        },
    },
    # 配置记录器
    # Logger 为日志系统的入口。每个logger 是一个容器，可以向它写入需要处理的消息,可以配置用哪种handlers来处理日志
    'loggers': {
        'django': {
            'handlers': ['console'],  # 日志处理器，将所有消息传递给console处理程序
            'level': 'DEBUG',  # 记录器级别
            'propagate': False  # 是否向上传播，写入的日志消息将不会被django记录器处理
        },
        # log app 专用
        'log.log': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'exception': {
            'handlers': ['exception_handler'],
            'level': 'ERROR',
            'propagate': False
        },
    }
}

# djangoweb/settings.py
ASGI_APPLICATION = 'djangoweb.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# 配置HayStack
HAYSTACK_CONNECTIONS = {
    'default': {
        # 设置搜索引擎，文件是apps下的serach的whoosh_cn_backend.py
        # 如果search模块未在apps下请自行替换或者去掉apps
        'ENGINE': 'apps.search.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
        'INCLUDE_SPELLING': True,
    },
}
# 设置每页显示的数据量
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 2
# 当数据库改变时，自动更新索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'









