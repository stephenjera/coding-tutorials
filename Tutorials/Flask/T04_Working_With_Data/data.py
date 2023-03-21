from flask import Flask, render_template, abort, request, redirect, url_for
from model import db, save_db
import sys

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


@app.route("/add_name/", methods=["GET", "POST"])
def add_name():
    if request.method == "POST":
        # form submitted process data
        names_dict = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
        }
        db.append(names_dict)
        save_db()
        print(f"db type: {type(db[0])} \n {db}", file=sys.stdout)
        return redirect(url_for("names", index=len(db) - 1))
    
    return render_template("add_name.html")


@app.route("/delete_name/<int:index>", methods=["GET", "POST"])
def delete_name(index):
    try:
        if request.method == "POST":
            # form submitted process data
            db.pop(index)
            save_db()
            return redirect(url_for("index"))
        
        return render_template("delete_name.html", name=db[index])
    except IndexError:
        abort(404)


@app.route("/api/names/")
def api_names():
    return db


@app.route("/api/names/<int:index>")
def api_names_index(index):
    try:
        return db[index]
    except IndexError:
        abort(404)


if __name__ == "__main__":
    # Run app in debug mode
    app.run(debug=True)
