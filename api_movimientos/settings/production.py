import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

# BASE DE DATOS REMOTO
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'TestSolmar',
        'HOST': '190.116.178.164',
        'USER': 'usr_solmar_vb',
        'PASSWORD': '11hotelbravo',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
        }
    }
}
