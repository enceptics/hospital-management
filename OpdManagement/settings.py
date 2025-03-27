

from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR=BASE_DIR/'templates'
STATIC_DIR=BASE_DIR/'static'
MEDIA_ROOT=BASE_DIR/'media'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c!+v0y3s*q@r-7exqe&0n25il^lqj!%^(-@(a%v^03z^ncyi#e'

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
    'rest_framework',
    'testapp',
    'schedule',
    'crispy_forms',
    'mathfilters',
    'IPDapp',
    'usermanagementapp',
    'crispy_bootstrap4',
    'import_export',
    'ramapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'testapp.middleware.MiddlewareExecutionStart',
    # 'testapp.api.middleware.ApiMiddlewareExecution'
]

ROOT_URLCONF = 'OpdManagement.urls'
ENCRYPT_KEY = b'tmzHcYuvLUhxjcxZ4k_iqfCx-HUq6PCvdbXr4vOC5B4='

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'testapp.context_processors.users_and_projects',
            ],
        },
    },
]

WSGI_APPLICATION = 'OpdManagement.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',

#     }
# }

DATABASES = {
    "default": dj_database_url.parse("postgres://hospital_dlkm_user:TWXI5oWAHtL0gyOzg3zyP7yLEJFAjqoV@dpg-cvi69opu0jms738fdr10-a.oregon-postgres.render.com/hospital_dlkm")
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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True

LOGIN_REDIRECT_URL ='/user_login'
LOGOUT_REDIRECT_URL='/user_login'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
MEDIA_URL='/media/'
STATIC_URL = 'static/'
STATICFILES_DIRS=[
    STATIC_DIR,
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# This setting informs Django of the URI path from which your static files will be served to users
# Here, they well be accessible at your-domain.onrender.com/static/... or yourcustomdomain.com/static/...
STATIC_URL = '/static/'

# # This production code might break development mode, so we check whether we're in DEBUG mode
# if not DEBUG:
#     # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
#     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#     # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
#     # and renames the files with unique names for each version to support long-term caching
#     STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

RAZORPAY_API_KEY='rzp_test_8ocxy7Ig5NRf9z'
RAZORPAY_API_SECRET_KEY='N0kHcCLagthKdQXP4PDf4EfH'
#Email Configurations
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER= 'gohilaljcet@gmail.com'
EMAIL_HOST_PASSWORD= 'mtbfybqkckfuskxu'
EMAIL_USE_TLS=True
SESSION_EXPIRE_SECONDS = 86400
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 1440
SESSION_TIMEOUT_REDIRECT = '/user_login'