# 1st: We need to import Flask
from flask import Flask, render_template

# 2nd: Setting up the app
app = Flask(__name__)

# This is a route to my index ( / ) page.
@app.route('/cover')
def cover():
    return render_template('cover.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')


# This is the root file
if __name__ == "__main__":
    app.run(debug=True)