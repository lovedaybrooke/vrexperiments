from flask import Flask
from flask import render_template, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

# attempt 1
@app.route('/local')
def local():
    return render_template('local.html')
 
# attempt 2
@app.route('/remote')
def remote():
    return render_template('remote.html')

# attempt 3
@app.route('/googles-image')
def googles_image():
    return render_template('googles-image.html')
 
# attempt 4
@app.route('/tweak')
def tweak():
    return render_template('tweak.html')
 
# attempt 5
@app.route('/aws')
def aws():
    return render_template('aws.html')

# attempt 6
@app.route('/aws-tweak')
def aws_tweak():
    return render_template('aws-tweak.html')

# attempt 7
@app.route('/aws-change-filepath')
def aws_change_filepath():
    return render_template('aws-change-filepath.html')

# @app.route('/<page>')
# def section(page=None):
#     return render_template('{0}.html'.format(page), page=page)

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404