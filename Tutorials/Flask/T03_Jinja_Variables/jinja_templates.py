from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", message="The power of Jinja variables")


if __name__ == "__main__":
    # Run app in debug mode
    app.run(debug=True)
