import os
import sys
"""
Django settings for HR project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crontab',
    'django_user_agents',
    'django_cleanup.apps.CleanupConfig',

    'corsheaders',
    'rest_framework',
    "rest_framework.authtoken",

    "apps.org",
    "apps.core",
    "apps.suborg",
    "apps.schedule",
    "apps.role",
    "apps.worker",
    "apps.work_calendar",
    "apps.feedback",
    "apps.survey",
    "apps.shagnal",
    "apps.sahilga",
    "apps.notif",
    "apps.faq",
    "apps.work_ad",
    "apps.report",
    "apps.device",
    "apps.kpi",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',

    # custom middleware
    'main.middleware.color.color_print',
    "main.middleware.successFn.success_fn",
    "main.middleware.errorHandler.ErrorHandlerMiddleware",
    "main.middleware.check_org.check_org",
    "main.middleware.set_perms.set_perms",
    "main.middleware.requestLog.RequestLogMiddleware",
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'main.context_processors.context_config',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processors.context_page_bookmarks',
            ],
            'libraries':{
                'mytags': 'templatetags',
            }
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dn&tTPV=DSy@&ty;c,Lia&]5x8{:41'
AUTHENTICATION_BACKENDS = ['main.utils.backend.PhoneAndEmailBackend']

STUDENT_LOGIN_API = 'http://student.utilitysolution.mn/api/user/login/'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'muis',
        'USER': 'muisuser',
        'PASSWORD': 'muis@123',
        'HOST':  'localhost',
        'PORT': '5432',
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

ENCRYPT_KEY = b'5sy_4mJN2q4GMu3OMhLrt2WWH5eP0AK6JAYssRn-pXA='
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'main.middleware.errorRFHandler.custom_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

# doc https://pypi.org/project/django-crontab/
# шинээр crontab үүсгэх нь ./manage.py crontab add
CRONJOBS = [
    ('1 1 * * *', 'apps.schedule.crontabs.successRequestAndVacation'),                     # Өглөөний 1 цаг 1 минутанд амралтын өдрийг бодох
    ('*/30 * * * *', 'apps.schedule.crontabs.absentismTimeRegister'),                      # 30 мин болгон тасыг бодно
    ('1 1 * * *', 'apps.account.views.happyBrithdaySendMail'),                          # Өглөөний 1 цаг 1 минутанд нягтлангуудлуу төрсөн өдөр болж байгаа хүмүүсийн мэдээллийг явуулна
    ('0 * * * *', 'apps.schedule.crontabs.changeXyStartNextJobAndVacationDate'),            # 1 цаг болгон XY ажилчны ажлын, амралтын эхлэх цагийг шинэчлэх
    ('0 * * * *', 'apps.work_ad.views.anyEndedWorkAdsense'),                            # 1 цаг болгон ажлын байрны төлөв шинэчлэх
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Ulaanbaatar'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'core.User'
SESSION_COOKIE_AGE = 7 * 24 * 60
SESSION_SAVE_EVERY_REQUEST = True

MESSAGE_TAGS = {
    messages.DEBUG: 'info',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "DELETE",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "access-control-allow-origin",
    "X-Frame-Options",
    'X-CSRFTOKEN',
    "set-cookie"
]

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:3001',
    'http://127.0.0.1:3001',
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3001',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:3001',
]

# QUERY DEBUG хийхэд хэрэгтэй LOGGING=1 ./manage.py runserver
# гэж асаавал server дээр ажиллаж query -г буцаана
if os.environ.get("LOGGING") == "1":
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'console': {
                'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s',
                'datefmt': "%H:%M:%S"
            },
            'sql': {
                'format': (
                        ''
                        # '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d \n'
                        # '%(duration).3f %(sql)s\n'
                        # '%(sql)s\n'
                        # 'args=%(params)s\n'
                    ),
                'datefmt': "%H:%M:%S"
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'console',
            },
            'sql': {
                'class': 'logging.StreamHandler',
                'class': 'logging.FileHandler',
                'filename': './debug.log',
                'formatter': 'sql',
            },
        },
        'loggers': {
            'django.db.backends': {
                'handlers': ['sql'],
                'level': 'DEBUG',
                'propagate': False,
            },
            '': {
                'handlers': ['console'],
                'level': 'INFO',
            },
        },
    }

X_FRAME_OPTIONS = 'SAMEORIGIN'

DATA_UPLOAD_MAX_MEMORY_SIZE = 262144800
FILE_UPLOAD_MAX_MEMORY_SIZE = 262144800
