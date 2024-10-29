from flask import Flask, render_template

app = Flask(__name__)


@app.route('/' , methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/categories', methods=['GET', 'POST'])
def categories():
    return render_template('categories.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

# error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)