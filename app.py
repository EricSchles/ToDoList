from flask import Flask, jsonify, render_template, request, redirect, url_for
import pickle

app = Flask(__name__)

@app.route("/palantir", methods=["GET","POST"])
def palantir():
	jsonr = pickle.load( open("save.p","rb") )
	print jsonr
	return render_template("palantir_index.html",json=jsonify(jsonr).data)

@app.route("/palantir/gate",methods=["GET","POST"])
def gate():
	if request.form["pass"] == "flapjacks": #change this
		return redirect(url_for("add"))
	else:
		return "I'm sorry that's not the password"

@app.route("/palantir/add", methods=["GET","POST"])
def add():
	new_todo = request.form["ToDo"]
	if new_todo:
		jsonr = pickle.load( open("save.p" , "rb") )
		keys = jsonr.keys()
		keys.sort()
		new_todo_key = int(keys[-1])+1
		jsonr.update({new_todo_key:new_todo})
		pickle.dump( jsonr, open("save.p", "wb"))
		return render_template("palantir_index.html",json=jsonr)
	else:
		return render_template("palantir_add.html")


if __name__ == '__main__':
	app.run(debug=True)
