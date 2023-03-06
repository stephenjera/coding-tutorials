from flask import Flask, render_template, abort
from model import db

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", names=db)


@app.route("/names/<int:index>")
def names(index):
    try:
        name = db[index]
        return render_template(
            "names.html", name=name, index=index, max_index=len(db) - 1
        )
    except IndexError:
        abort(404)


if __name__ == "__main__":
    # Run app in debug mode
    app.run(debug=True)
