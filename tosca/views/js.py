from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from datetime import datetime

from flask import render_template, Blueprint, Response
from flask_login import login_required


mod = Blueprint("views/js", __name__)


@mod.route("/js/main.js")
@login_required
def main():
    return Response(
        render_template(
            "js/main.js",
            title="TOSCA: Advanced FacetView User Interface",
            current_year=datetime.now().year,
        ),
        mimetype="application/javascript",
    )


@mod.route("/js/components/mainAppView.js")
@login_required
def mainAppView():
    return Response(
        render_template(
            "js/mainAppView.js",
            title="TOSCA: Advanced FacetView User Interface",
            current_year=datetime.now().year,
        ),
        mimetype="application/javascript",
    )
