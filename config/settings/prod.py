from .base import *

ALLOWED_HOSTS = ['13.209.60.165']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []

# 로컬에서 장고 서버 진행시 --settings=config.settings.local
# 서버에서 장고 서버 진행시 --settings=config.settings.prod