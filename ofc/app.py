from flask import Flask, render_template, request
import ofc_simulation

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ofc', methods=["POST"])
def results():
    n = request.form["n"]
    a = request.form["A"]
    steps = request.form["steps"]
    force = request.form["force"]
    ofc_simulation.simulation(int(n), float(a), int(steps), float(force))
    return render_template("results.html")


if __name__ == '__main__':
    app.run()
