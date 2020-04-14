from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Index Page"


@app.route('/hello')
def say_hello():
    return "Hello, greetings from different endpoint"


# adding variables
@app.route('/username/<username>')
def show_user(username):
    # returns the username
    return 'Username: %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # returns the post, the post_id should be an int
    return str(post_id)


# shows a demo request route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # check user details from db
        login_user()
    elif request.method == 'GET':
        # serve login page
        serve_login_page()

# rendering templates
@app.route('/user/<name>')
def hello(name=None):
    # name=None ensures the code runs even when no name is provided
    return render_template('user_profile.html', name=name)

# accessing data request
@app.route('/user', methods=['GET', 'POST'])
def get_user():
    username = request.form['username']
    password = request.form['password']
    # login(arg, arg) is a function that tries to log in
    # and tries to log in and returns true or false
    status = login(username, password)
    return status

# demo for file uploads
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.methods == 'POST':
        static_file = request.files['the_file']
        # here you can send this static_file to a storage service
        # or save it permanently to the file system
        static_file.save('var/ww/uploads/profilephoto.png')
