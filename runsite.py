from flask import Flask
from flask import render_template, redirect
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def home():
    return render_template('home.html')

# attempt 1
@app.route('/local')
def local():
    return render_template('1-local.html')
 
# attempt 2
@app.route('/remote')
@cross_origin()
def remote():
    return render_template('2-remote.html')

# attempt 3
@app.route('/googles-image')
def googles_image():
    return render_template('3-googles-image.html')
 
# attempt 4
@app.route('/tweak')
def tweak():
    return render_template('4-tweak.html')
 
# attempt 5
@app.route('/aws')
def aws():
    return render_template('5-aws.html')

# attempt 6
@app.route('/aws-tweak')
def aws_tweak():
    return render_template('6-aws-tweak.html')

# attempt 7
@app.route('/aws-change-filepath')
def aws_change_filepath():
    return render_template('7-aws-change-filepath.html')

# attempt 8
@app.route('/host-elsewhere')
def host_elsewhere():
    return render_template('8-host-elsewhere.html')

# attempt 9
@app.route('/vrview-in-static')
def vrview_in_static():
    return render_template('9-vrview-in-static.html')


# @app.route('/<page>')
# def section(page=None):
#     return render_template('{0}.html'.format(page), page=page)

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404