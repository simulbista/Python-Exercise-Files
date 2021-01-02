from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/map/')
def map():
    return render_template("map.html")

# In this case, we are not hosting the website, rather we are running the script named 14website.py. In such cases where we run our script
# python gives the script the name as __main__, hence we run the following 2 lines of code, in actual hosting environment, the following 2 lines would not execute.
if __name__=="__main__":
    app.run(debug=True)
