# -*- coding: utf-8 -*-

import os

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
