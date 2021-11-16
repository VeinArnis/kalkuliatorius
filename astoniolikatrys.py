from flask import Flask, render_template
import calendar

app = Flask(__name__)


@app.route('/<name>keliamieji')
def metai(name):
    keliamieji = []
    metus = range(1900, 2101)
    for x in metus:
        if calendar.isleap(x):
            keliamieji.append(x)
    return render_template("labas.html", sarasas=keliamieji)


app.run(debug=True)
