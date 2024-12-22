from flask import Flask, redirect, url_for
import secrets

from .routes import tools


def create_app():
    app = Flask(__name__)
    
    # config 파일 로드
    app.config.from_pyfile('config.py')     # 'config.py' 파일을 읽어온다
    
    # 세션을 위한 Secret Key 설정
    app.secret_key = secrets.token_hex(32)
    
    # 블루프린트 등록
    from .routes import login, utils
    app.register_blueprint(login.bp)
    app.register_blueprint(utils.bp)
    app.register_blueprint(tools.bp)
    
    # 시작 시, log in 페이지로 리디렉션
    @app.route('/')
    def start():
        return redirect(url_for('login.login'))
    
    return app