from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

# Routes to the home page
@app.route("/")
def home_page():
    """
    Renders and displays the homepage
    
    Returns:
        str: Returns a str formatted html site to render to the website
    """
    
    return render_template('index.html')

#Just for testing
@app.route("/about_me")
def about_me():
    
   return render_template("about_me.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)