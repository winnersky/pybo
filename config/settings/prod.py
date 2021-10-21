from .base import *

ALLOWED_HOSTS = ['13.209.60.165']
STATIC_ROOT = BASE_DIR / 'pybo/static/'
STATICFILES_DIRS = []
DEBUG = False

# 로컬에서 장고 서버 진행시 --settings=config.settings.local
# 서버에서 장고 서버 진행시 --settings=config.settings.prod

# 변경된 프로그램 서버에 적용하기
#
# 앞으로 로컬 환경에서 파일 수정 후 서버에 적용하는 일련의 과정들은 이 책에서 생략할 것이다. 하지만 다음의 과정으로 서버에 프로그램을 적용해야 함을 잊지 말자.
#
# 먼저 로컬 환경에서 프로그램이 변경되면 다음과 같은 순서로 적용한다
#
# [로컬 환경에서 프로그램이 변경된 경우]
#
# git add *
# git commit -m "수정내용 코멘트"
# git push
# 그리고 서버 환경에서 변경된 내용을 다음과 같은 순서로 적용한다.
#
# [서버 환경에서 변경된 내용 적용]
#
# git pull
# sudo systemctl restart gunicorn.service