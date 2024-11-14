# gpt 사용, 프롬포트 : Django에서 csv 파일을 DB에 저장하는 법
# response
# import pandas as pd
# from myapp.models import User, Model  # 적절한 앱 이름 사용
#
# # CSV 파일을 읽어오기
# df = pd.read_csv('path/to/your/csvfile.csv', encoding='euc-kr')
#
# # CSV 데이터를 모델에 저장
# for index, row in df.iterrows():
#     user_instance = User.objects.get(id=row['user_id'])  # 사용자 정보가 필요한 경우
#     Models.objects.create(
#         user_id=user_instance,
#         name=row['name']
#     )

# gpt 사용, 프롬포트 : (.venv) PS C:\Users\User\PycharmProjects\OpenSWProgramProject> python csv_to_db.py
# Traceback (most recent call last):
#   File "C:\Users\User\PycharmProjects\OpenSWProgramProject\csv_to_db.py", line 19, in <module>
#     from apps.models import Accommodation
#   File "C:\Users\User\PycharmProjects\OpenSWProgramProject\apps\models.py", line 1, in <module>
#     from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
#   File "C:\Users\User\PycharmProjects\OpenSWProgramProject\.venv\Lib\site-packages\django\contrib\auth\base_user.py", line 40, in <module>
#     class AbstractBaseUser(models.Model):
#   File "C:\Users\User\PycharmProjects\OpenSWProgramProject\.venv\Lib\site-packages\django\db\models\base.py", line 129, in __new__
#     app_config = apps.get_containing_app_config(module)
#                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\User\PycharmProjects\OpenSWProgramProject\.venv\Lib\site-packages\django\apps\registry.py", line 260, in get_containing_app_config
#     self.check_apps_ready()
#   File "C:\Users\User\PycharmProjects\OpenSWProgramProject\.venv\Lib\site-packages\django\apps\registry.py", line 137, in check_apps_ready
#     settings.INSTALLED_APPS
#   File "C:\Users\User\PycharmProjects\OpenSWProgramProject\.venv\Lib\site-packages\django\conf\__init__.py", line 81, in __getattr__
#     self._setup(name)
#   File "C:\Users\User\PycharmProjects\OpenSWProgramProject\.venv\Lib\site-packages\django\conf\__init__.py", line 61, in _setup
#     raise ImproperlyConfigured(
# django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
# 이 오류 무슨 내용이야?
# response
# 해결 방법:
# Django 설정 모듈 환경 변수 설정: os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')를 사용하여 Django 설정 모듈을 지정했는지 확인하세요.
#
# Django 환경 초기화 순서 확인: django.setup()을 호출하여 Django 환경을 초기화해야 합니다.
# 다음은 csv_to_db.py 파일에 Django 환경을 설정하는 코드입니다.
# import sys
# import os
#
# # 프로젝트 루트 경로를 sys.path에 추가
# project_root = os.path.dirname(os.path.abspath(__file__))  # 스크립트의 상위 경로 확인
# sys.path.append(project_root)
#
# # Django 설정 모듈 환경 변수 설정
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # 'config'는 프로젝트 설정 폴더 이름
#
# # Django 환경 초기화
# import django
# django.setup()



import sys, os, django
import pandas as pd
from apps.models import Accommodation

# 프로젝트 루트 경로를 sys.path에 추가
project_root = os.path.dirname(os.path.abspath(__file__))  # 스크립트의 상위 경로 확인
sys.path.append(project_root)

# Django 설정 모듈 환경 변수 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # 'config'는 프로젝트 설정 폴더 이름

# Django 환경 초기화
django.setup()

df = pd.read_csv('combined_public_data.csv', encoding='utf-8') # 공공데이터 포털에서 얻은 파일 읽어서 DB에 저장

for index, row in df.iterrows():
    Accommodation.objects.create(
        name=row['업체명'],
        address=row['주소'],
        number=row['전화번호'],
        no_of_rooms=row['객실수'],
        urls=row['홈페이지']
    )