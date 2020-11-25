from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
    'from':  'Cornwall, Prince Edward Island',
    'current':  'New Brunswick, Canada',
    'relocate':  'particularly Toronto/Montreal/Vancouver. Would also consider returning to PEI'
    }
]

articles = [
    {
    'title': 'Alex Sutherland test ',
    'author': 'Suds171',
    'date_posted': 'Today, May 6th, 2020',
    'content': 'asdlf;kjsdfl;kjsadf;las'
    },
    {
    'title': 'Alex Sutherland test2 ',
    'author': 'Suds171',
    'date_posted': 'Today, May 6th, 2020',
    'content': 'asdlf;kjsdfl;kjsadf;las'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('Parralax_home.html', posts=posts, articles=articles)

if __name__ == '___main__':
    app.run(debug=True)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html' )

@app.route('/blog')
def blog():
    return render_template('blog.html', articles=articles)

@app.route('/announcements')
def announcements():
    return render_template('announcements.html')

if __name__ == '__main__':
    app.run(debug=True)
