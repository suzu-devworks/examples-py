from typing import Any, Mapping

from flask import Flask, render_template


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    from .app1 import bp as app1
    from .app2 import bp as app2
    from .app3 import bp as app3
    from .app4 import bp as app4
    from .app5 import bp as app5

    app.register_blueprint(app1)
    app.register_blueprint(app2, url_prefix="/app2-alias")
    app.register_blueprint(app3, url_prefix="/app3")
    app.register_blueprint(app4, url_prefix="/app4")
    app.register_blueprint(app5, url_prefix="/app5")

    @app.route("/")
    def index() -> str:
        return render_template("index.html")

    return app
