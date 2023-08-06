# wanted-pre-onboarding-backend

최정윤

### 요구사항
1. python 3.10.6
2. 3306 포트에 Mysql 연결
3. pip install -r requirements.txt 를 통해 필요한 앱 설치
4. 단, django SECRET_KEY 입력 필요

### 실행 방법
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

### 엔드포인트 호출
1. 회원가입 | post /user/sign-up/
2. 로그인 | post /user/login/
3. 게시글 목록 조회 | get /article/?page={page}
4. 게시글 작성 | post /article/
5. 특정 게시글 조회 | get /article/<int:article_id>/ 
6. 특정 게시글 수정 | put /article/<int:article_id>/
7. 특정 게시글 삭제 | delete /article/<int:article_id>/

### ERD
  
  ![image](https://github.com/uniqquej/wanted-pre-onboarding-backend/assets/109218139/815c5212-b215-4676-a6f8-6ef413abec1f)
https://dillinger.io/

### 데모 영상
### 구현 방법 및 이유
1. Django REST framework 
  - serializer안에서 validate, create 등의 함수로 편리하게 데이터를 관리할 수 있음
  - orm 기능을 제공
  - pagination 기능을 제공해줌

2. simple JWT
  - 서버의 부담을 줄일 수 있음
  - token의 유효기간 등 다양한 옵션을 간편하게 관리할 수 있음

### API 명세
| 기능 | url |method |
| ------ | ------ | ------ |
| 회원가입 | /user/sign-up/ |POST|
| 로그인 | /user/login/ |POST|
| 게시글 목록 조회 | /article/ |GET|
| 게시글 작성 | /article/ |POST|
| 특정 게시글 조회 |/article/<int:article_id>/ |GET|
| 특정 게시글 수정 |/article/<int:article_id>/|PUT|
| 특정 게시글 삭제 | /article/<int:article_id>/ |DELETE|

##### 1. 회원가입
```python
# request
post /user/sign-up/
body:{
    "email": "test@test.com",
    "password":"12345678",
    "password2":"12345678"
}
#response
# status_code : 201
{
    "email":"test@test.com"
}
# status_code : 400
{
    "non_field_errors":"error message"
}
```

##### 2. 로그인
```python
# request
post /user/login/
 body:{
    "email": "test@test.com",
    "password":"12345678"
}
#response
# status_code : 200
{
    "access": "access_token",
    "refresh":"refresh_token"
}
# status_code : 400
{
    "msg":"error message"
}
```

##### 3. 게시글 목록
```python
#request
get /article/?page={page}

#response
# status_code : 200
{ "count": 2,
    "next": "http://127.0.0.1:8000/article/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": 1,
            "title": "test1",
            "content": "testing2"
        },
        {
            "id": 2,
            "author": 2,
            "title": "test2",
            "content": "testing"
        }
    ]
}
```

##### 4. 게시글 작성
```python
# request
post /aritlce/
headers:{
    "AUTHORIZATION":"Bearer {access_token}"
}
 body:{
    "title": "test title",
    "content":"test content"
}
#response
# status_code : 201
{
    "id": 3,
    "author": 2,
    "title": "test title",
    "content":"test content"
}
```
##### 5. 특정 게시글 조회
```python
# request
get /aritlce/{article_id}

#response
# status_code : 200
{
    "id": 3,
    "author": 2,
    "title": "test title",
    "content":"test content"
}

# status_code : 404
{
    "detail": "찾을 수 없습니다."
}
```

##### 6. 특정 게시글 수정
```python
# request
put /aritlce/{article_id}
headers:{
    "AUTHORIZATION":"Bearer {access_token}"
}
 body:{
    "title": "edit title",
}

#response
# status_code : 200
{
    "id": 3,
    "author": 2,
    "title": "edit title",
    "content":"test content"
}

# status_code : 401
{
    "msg": "권한이 없습니다."
}
```

##### 7. 특정 게시글 삭제
```python
# request
delete /aritlce/{article_id}
headers:{
    "AUTHORIZATION":"Bearer {access_token}"
}
#response
# status_code : 200
{
    "msg": "삭제가 완료되었습니다."
}

# status_code : 401
{
    "msg": "권한이 없습니다."
}
```