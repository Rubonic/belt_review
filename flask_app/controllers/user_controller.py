from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.show import show
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

# Validation of Registration
@app.route("/register", methods=["POST"])
def register():

    if not User.validate_register(request.form):
        return redirect("/")

  
    pc_hash = bcrypt.generate_password_hash(request.form["password"])

    query_data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : pc_hash,
    }
    
   
    new_user_id = User.register_user(query_data)

    
    session['user_id'] = new_user_id

    
    return redirect("/dashboard")

# Validation of Login Route
@app.route("/login", methods=["POST"])
def login():

    if not User.validate_login(request.form):
        return redirect("/")

    logged_user = User.get_by_email(request.form)
    session['user_id'] = logged_user.id


    
    return redirect("/dashboard")

# Dashboard
@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        flash("You need to login in order to proceed!!!")
        return redirect("/")
    query_data = {
        "user_id" : session["user_id"]
    }
    user = User.get_by_id(query_data)
# Step 10: type this to view all of the items (import it at the top of the controller) then go to the show model
    all_shows = show.get_all_shows()
    return render_template("dashboard.html", user = user, all_shows = all_shows)
# step 15: typer in all_shows = all_shows in the return then go to dashboard.html
# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

