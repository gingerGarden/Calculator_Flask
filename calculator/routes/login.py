from flask import Blueprint, render_template

bp = Blueprint(
    name='login',               # 블루프린트의 "별칭"
    import_name=__name__,       # import 모듈명
    url_prefix='/login'         # 라우팅 함수의 애너테이션 접두션 URL
)

@bp.route('/')
def login():
    return 'Log in! Here!!'