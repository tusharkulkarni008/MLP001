from flask import Flask

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
<<<<<<< HEAD
    return "hello world"


if __name__=="__main__":
    app.run()
=======
   
if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 7239b91c8b5efb83c5b7a0e96edefeb90d98cdd3
