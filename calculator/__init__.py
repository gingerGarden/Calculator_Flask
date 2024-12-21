from flask import Flask, redirect, url_for


def create_app():
    app = Flask(__name__)
    
    # session key
    app.secret_key = 'test_session_1234'
    
    from .routes import login, utils
    app.register_blueprint(login.bp)
    app.register_blueprint(utils.bp)
    
    @app.route('/')
    def index():
        return redirect(url_for('login.login'))
    
    return app