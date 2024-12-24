from flask import Blueprint, render_template, request, redirect, url_for, session

bp = Blueprint(
    name='tools',
    import_name=__name__,
    url_prefix='/tools'
)

@bp.route('/main')
def main():
    if 'user_id' not in session:
        return redirect(url_for('login.login'))
    return render_template('tools_main.html')

@bp.route('/logout')
def logout():
    # 세션에서 사용자 ID 제거
    session.pop('user_id', None)
    # login 페이지 url 이동
    return redirect(url_for('login.login'))

@bp.route('/action', methods=['POST'])
def handle_action():
    button_id = request.form.get('button_id')
    if button_id == 'button1':
        return redirect(url_for('tools.calculator_mobile'))
    elif button_id == 'button2':
        return redirect(url_for('tools.calculator_pc'))
    else:
        return redirect(url_for('tools.main'))  # 기본 페이지로 리다이렉트

@bp.route('/calculator-mobile')
def calculator_mobile():
    return render_template('calculator_mobile.html')

@bp.route('/calculator-pc')
def calculator_pc():
    return "calculator PC version"