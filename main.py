from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<page>")
def index(page=None):
    return render_template("temp1.html",page=page)

@app.route("/profile/<username>/<int:post_id>")
def show_post(username,post_id):
    return "Hello {} your post_id is {}".format(username,post_id)

if __name__ == "__main__":
    app.run(debug=True)
