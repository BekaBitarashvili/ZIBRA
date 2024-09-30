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


if __name__ == '__main__':
    app.run(debug=True)
