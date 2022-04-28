from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.show import Car

# New Car Routes Step 3: Add new controller to server.py
@app.route("/car/new")
def new_car():
# Step 6: go to user_controller and copy this from dashboard then go to New_...html
    if 'user_id' not in session:
        flash("You need to login in order to proceed!!!")
        return redirect("/")
    return render_template("new_car.html") # Step 4: Creat a new html page (new_car.html)

# Step 9:
@app.route("/car/create", methods=["POST"])
def create_car():
# Step 9.A - Validate form info
    if not Car.validate_car(request.form):
        return redirect("/car/new")
# Step 9.b - Create new model and put it at the top of the controller then go to user.py, copy the top 3
# Step 9.c - Collect query data
    query_data = {
        "color" : request.form["color"],
        "num_of_seats" : request.form["num_of_seats"],
        "user_id" : session["user_id"]
    }

# Step 9.d - Query using data (insert query) after first line is typed go to car model
    new_car_id = Car.create_car(query_data)

# Step 9.e - Redirect elsewhere
    return redirect("/dashboard")

# Show One Car Route
# Step 18: type this
# Step 21: type the following ("if statement")
@app.route("/car/show/<int:car_id>")
def show_car(car_id):
    if 'user_id' not in session:
        flash("You need to login in order to proceed!!!")
        return redirect("/")

    # Step 22: (gather query data)
    query_data = {
        "car_id" : car_id
    }

    # Step 23: (query with data) once the first line is typed go to the car model
    car = Car.get_one_car(query_data) 

    # Step 27: type one_car = car(render html with data from query) then go to show html

    return render_template("show_car.html", one_car = car) # Step 19: create a new html

# Edit one car routes
    # Step 32:  type class method (only app, def, return)
@app.route("/car/edit/<int:car_id>")
def edit_car(car_id):
# step 35: type this
    if 'user_id' not in session:
        flash("You need to login in order to proceed!!!")
        return redirect("/")
    query_data = {
        "car_id" : car_id
    }
    car = Car.get_one_car(query_data)

    return render_template("edit_car.html", one_car = car) # Step 33:  create a new html (edit) then go to it
# Step 36: ,type one_car = car nexto edit_car.html then go to the edit html

# step 38: type update class (app, def, return test it out when done)
@app.route("/car/update/<int:car_id>", methods=["POST"])
def update_car(car_id):
    # step 39: (validate info, test once typed)
    if not Car.validate_car(request.form):
        return redirect(f"/car/edit/{car_id}")

    # step 40: (gather query data)
    query_data = {
        "color" : request.form["color"],
        "num_of_seats" : request.form["num_of_seats"],
        "car_id" : car_id
    }

    # step 41: (query with data, once typed go to car model)
    Car.update_car(query_data)

    
    return redirect("/dashboard")

# Delete Route 
# step 44: type this then go to car model
@app.route("/car/delete/<int:car_id>")
def delete_car(car_id):
    query_data = {
        "car_id" : car_id
    }
    Car.delete_car(query_data)
    return redirect("/dashboard")

