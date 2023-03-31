"""
code to download a query as CSV to connect to Tableau 
"""
import psycopg2
from flask import Flask, request, Response, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/connect", methods=["POST"])
def connect():
    try:
        # Retrieve connection parameters from the form
        hostname = request.form["hostname"]
        port = request.form["port"]
        database = request.form["database"]
        username = request.form["username"]
        password = request.form["password"]

        # Create a connection to the PostgreSQL database
        conn = psycopg2.connect(
            host=hostname, port=port, dbname=database, user=username, password=password
        )

        # Laod script 
        with open('cards.sql', 'r', encoding='utf-8') as f:
            sql_script = f.read()

        # Retrieve data from a table
        cur = conn.cursor()
        cur.execute(sql_script)
        rows = cur.fetchall()
        # Get the column headers
        headers = [description[0] for description in cur.description]

        # Format the data as a CSV string
        csv_data = ",".join(headers) + "\n"
        for row in rows:
            csv_data += ",".join(map(str, row)) + "\n"

        # Return the CSV data as a response
        return Response(
            csv_data,
            mimetype="text/csv",
            headers={"Content-Disposition": "attachment;filename=data.csv"},
        )

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)
