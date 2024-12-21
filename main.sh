# 가상환경 활성화
conda activate calculator

# Flask 환경 변수 설정
export FLASK_APP=calculator:create_app
export FLASK_DEBUG=true

# Flask 애플리케이션 실행
flask run --port=8080