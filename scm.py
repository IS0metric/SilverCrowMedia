from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def home():
    """Home page"""
    return render_template('home.html')


@app.route('/contact')
def contact():
    """Contact page: displays's contact links"""
    return render_template('contact.html')


@app.route('/podcasts')
def podcasts():
    """Podcasts page: details and links for each podcast"""
    return render_template('podcasts.html')


@app.route('/streams')
def streams():
    """Streams page: details and links for streams"""
    return render_template('streams.html')


@app.route('/about')
def about():
    """About page: wee bios for each member"""
    return render_template('about.html')


if __name__ == "__main__":
    print("RUNNING APP")
    app.run(debug=True)
