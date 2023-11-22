from flask import Flask, g, request, redirect, url_for, abort
import functools
app = Flask(__name__)

def login_required(func):
    '''Make sure user is logged in before proceeding'''
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
    pass

'''Validating JSON'''
#
def validate_json(*expected_args): # 1
    def decorator_validate_json(func):
        @functools.wraps(func)
        def wrapper_validate_json(*args, **kwargs):
            json_object = request.get_json() 
            for expected_arg in expected_args: # 2
                if expected_arg not in json_object:
                    abort(400)
                return func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper_validate_json
    return decorator_validate_json

@app.route("/grade", methods=['POST'])
@validate_json("student_id")
def update_grade():
    json_data = request.get_json
    # Update database.
    return "Sucess!"
