# Copy these from the user model
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

# step 9.b type this according to the schema
class Car:
    db = "tv_show_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.network = data["network"]
        self.time = data["time"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

        self.person = {};
# type self.cars = [] in the user model

# step 9.b.1 type this once completed go to new car.html
    @staticmethod
    def validate_show(form_data):
        is_valid = True
        if len(form_data["color"]) < 3 or len(form_data["color"]) > 25:
            flash("Color must be between 3-25 characters!")
            is_valid = False

        if form_data["num_of_seats"] == "":
            flash("Please enter number of seats!")
            is_valid = False
        elif int(form_data["num_of_seats"]) > 15:
            flash("Number of seats cannot exceed 15!")
            is_valid = False

        return is_valid

# Step 9.d.1 - type this/once completed go to check if it works then go to user_controller
    @classmethod
    def create_car(cls, data):
        query = "INSERT INTO cars (color, num_of_seats, user_id, created_at) VALUES (%(color)s, %(num_of_seats)s, %(user_id)s, NOW());"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

# Step 11:type this/once type copy the query into the workbench in cars and save it as a json file then open it and go to it
    @classmethod
    def get_all_cars(cls):
        query ="SELECT * FROM cars LEFT JOIN users ON cars.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)

        all_cars_with_drivers = []
# step 13: type this 
        for row in results:
            car = Car(row)

            user_data = {
                "id" : row["users.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "email" : row["email"],
                "password" : row["password"],
                "created_at" : row["users.created_at"],
                "updated_at" : row["users.updated_at"]
            }
            car.driver = user.User(user_data)
            all_cars_with_drivers.append(car)
        return all_cars_with_drivers
# Step 14: scroll up and type from flask_app.models import user then go to user_controller

# Step 24: type this classmethod
# Step 25: once query and results are typed copy the query and then go to workbench into the cars section and save the file as a json and open it
    @classmethod
    def get_one_car(cls, data):
        query = "SELECT * FROM cars LEFT JOIN users ON cars.user_id = users.id WHERE cars.id = %(car_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
# Step 26: type this data once typed go to car controller
        car = cls(results[0])
        user_data = {
            "id" : results[0]["users.id"],
            "first_name" : results[0]["first_name"],
            "last_name" : results[0]["last_name"],
            "email" : results[0]["email"],
            "password" : results[0]["password"],
            "created_at" : results[0]["users.created_at"],
            "updated_at" : results[0]["users.updated_at"]
        }
        car.driver = user.User(user_data)
        return car 

# step 42:type this (check if it works) once confirmed go to dashboard html
    @classmethod
    def update_car(cls, data):
        query = "UPDATE cars SET color = %(color)s, num_of_seats = %(num_of_seats)s, updated_at = NOW() WHERE id = %(car_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return 

# step 45: type this once done check it if it works once done go to dashboard html
    @classmethod
    def delete_car(cls, data):
        query = "DELETE FROM cars WHERE id = %(car_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return 
