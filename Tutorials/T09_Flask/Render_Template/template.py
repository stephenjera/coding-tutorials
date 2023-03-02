from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("hello.html")


@app.route("/form")
def form():
    return render_template("form.html")


if __name__ == "__main__":
    # Run app in debug mode
    app.run(debug=True)

