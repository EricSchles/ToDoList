from flask import Flask, jsonify, render_template, request, redirect, url_for
import pickle

app = Flask(__name__)

@app.route("/palantir", methods=["GET","POST"])
def palantir():
	jsonr = pickle.load( open("save.p","rb") )
	print jsonr
	return render_template("palantir_index.html",json=jsonify(jsonr).data)


@app.route("/palantir/add", methods=["GET","POST"])
def add():
	return render_template("palantir_add.html")

@app.route("/add_data",methods=["GET","POST"])
def add_data():	
	print "got here"
	new_todo = request.args.get("ToDo")
	jsonr = pickle.load( open("save.p" , "rb") )
	keys = jsonr.keys()
	keys.sort()
	new_todo_key = int(keys[-1])+1
	jsonr.update({new_todo_key:new_todo})
	pickle.dump( jsonr, open("save.p", "wb"))
	print "here"
	return render_template("palantir_index.html",json=jsonify(jsonr).data)


if __name__ == '__main__':
	app.run(debug=True)
