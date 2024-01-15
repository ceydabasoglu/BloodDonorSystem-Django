"""
Django settings for BloodDonorSystem project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-grtnoodz1$5y=7ochjpd**m(3$c7)ex47j8yuqn2-()*!wjc9i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'CreateQueryDonor',
    'BloodBankManagement',
    'BloodRequestManagement',
    'rest_framework',
    'django_filters',
    
    
    
    
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
import os

ROOT_URLCONF = 'BloodDonorSystem.urls'

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    
]

# settings.py
LOGIN_URL = 'branch_login'
LOGIN_REDIRECT_URL = '/create_query_donor/'  
LOGOUT_REDIRECT_URL = '/create_query_donor/branch_login/' 

WSGI_APPLICATION = 'BloodDonorSystem.wsgi.application'

#Permission ve Authentication Ayarları: Django REST Framework, kullanıcı yetkilendirme ve kimlik doğrulama işlemi.
# Pagination Ayarı. her sayfada 10 talebi görüntüleyecektir.
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.SearchFilter'],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#projemi azure sql database e bağlarken burayı kullandım. 
"""
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',  
        'NAME': 'ceydaabasogluu',
        'USER': 'ceydaabasoglu',
        'PASSWORD': 'Ceyda123',
        'HOST': 'ceydaabasogluu.database.windows.net',
        'PORT': '',  
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server',  
            'MARS_Connection': True,
        },
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



GDAL_LIBRARY_PATH = 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python392\\Lib\\site-packages\\osgeo\\gdal304.dll'
GEOS_LIBRARY_PATH = 'C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python392\\Lib\\site-packages\\osgeo\\geos_c.dll'
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# E-posta gönderimi için yapılandırma. SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 't32552136@gmail.com'  
EMAIL_HOST_PASSWORD = 'nwuhxprzgjuixiwl'  
#http://127.0.0.1:8000/bloodrequest/request_blood/
#http://127.0.0.1:8000/bloodrequest/api/bloodrequests/