#encoding: utf-8

from flask import Flask
from flask import render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
	week_sp = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

	month_sp = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


	week_pt = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo")

	month_pt = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Septembro", "Outubro", "Novembro", "Dezembro")
	
	today = datetime.datetime.now()

	cur_month = today.month - 1
	cur_week = datetime.datetime.today().weekday()


	today = today.strftime("%Y-{}-%d, {}".format(month_pt[cur_month], week_pt[cur_week]))

	return render_template("index.html", today=today)

if __name__ == "__main__":
	app.run(debug=True)
