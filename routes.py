from flask import Flask, render_template
from flask_flatpages import FlatPages

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'


app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

#main routes
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/articles")
def articles():
    return render_template('articles.html')
# main routes end

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path).html
    return render_template('page.html',page=page)



if __name__ == "__main__":
    app.run()
