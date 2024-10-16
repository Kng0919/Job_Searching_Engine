from flask import Flask, render_template, request

app = Flask(__name__)

#Home Page
@app.route("/", methods=['GET','POST'])
def home():
    return render_template("home.html")

#Register Page
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        #POST method - To be implemented
        pass

if __name__ == "__main__":
    app.run()