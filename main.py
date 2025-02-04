from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')

@app.route('/work_with_us')
def work_with_us():
    return render_template('work_with_us.html', title='Work With Us')

if __name__ == "__main__":
    app.run(debug=True)
