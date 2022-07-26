from flask import Flask, render_template
from cbrf import ValueCourse
from datetime import date

app = Flask(__name__)
value_course = ValueCourse()

@app.route("/")
def index():
    today = str(date.today())
    values_usd = round(float(value_course.value['usd'][today]), 2)
    values_eur = round(float(value_course.value['eur'][today]), 2)
    values_cny = round(float(value_course.value['cny'][today])/10, 2)

    return render_template('value.html', values = [values_usd, values_eur, values_cny])


@app.route("/values")
def value():
    return render_template('index.html')


@app.route("/author")
def author():
    return render_template('author.html')

    
@app.route("/article")
def article():
    return render_template('article.html')


if __name__ == '__main__':
    app.run(debug=True)