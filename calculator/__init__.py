from flask import Flask, redirect, url_for


def create_app():
    app = Flask(__name__)
    
    # config 파일 로드
    app.config.from_pyfile('config.py')     # 'config.py' 파일을 읽어온다
    
    from .routes import login, utils
    app.register_blueprint(login.bp)
    app.register_blueprint(utils.bp)
    
    # 시작 시, log in 페이지로 리디렉션
    @app.route('/')
    def start():
        return redirect(url_for('login.login'))
    
    return app