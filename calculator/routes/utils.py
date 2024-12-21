from flask import Blueprint

bp = Blueprint(
    name='utils',
    import_name=__name__,
    url_prefix='/utils'
)

@bp.route('/ping', methods=['GET'])
def ping():
    return "pong"