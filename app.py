from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    table = None
    number = None

    if request.method == "POST":
        try:
            number = int(request.form["number"])
            if number <= 0:
                table = "Please enter a positive integer."
            else:
                table = [(i, i * number) for i in range(1, 11)]
        except ValueError:
            table = "Invalid input! Please enter an integer."

    return render_template("index.html", table=table, number=number)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
