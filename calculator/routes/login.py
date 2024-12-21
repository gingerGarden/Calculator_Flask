from flask import Blueprint, render_template, request, current_app, redirect, url_for

bp = Blueprint(
    name='login',               # 블루프린트의 "별칭"
    import_name=__name__,       # import 모듈명
    url_prefix='/login'         # 라우팅 함수의 애너테이션 접두션 URL
)

@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 입력된 ID와 Password
        user_id = request.form.get('id')
        password = request.form.get('password')
        
        # 허가된 사용자 정보
        authorized_users = current_app.config['AUTHORIZED_USERS']
        
        # 검증
        if user_id in authorized_users:
            if authorized_users[user_id] == password:
                mask = True
            else:
                mask = False
        else:
            mask = False
            
        # 이동
        if mask:
            return redirect(url_for('login.success'))
        else:
            return redirect(url_for('login.fail'))
        
    return render_template('login_page.html')

@bp.route('/fail')
def fail():
    return "Fail"

@bp.route('/success')
def success():
    return "Success"