import re
import os
from flask import Flask, flash, render_template, \
      redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

# Code as directed by Data Centric Development module
# Modified, added to and rewritten for project


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # Check username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)

        # Put user into a session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful! You can now share your own recipes!")
        return redirect(url_for("home", username=session["user"]))

    return render_template("sign_up.html")


# Log in Function
@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        # check to see if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for("home", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("sign_in"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("sign_in"))

    return render_template("sign_in.html")


@app.route("/sign_out")
def sign_out():
    if 'user' in session:
        session.pop("user")
        flash("You have been signed out")
        return redirect(url_for("home"))

    else:
        return redirect(url_for("home"))


# Add a Recipe Function
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        todays_date = datetime.today().strftime('%Y-%m-%d')
        recipe = {
            "category": request.form.get("category"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"],
            "date_added": todays_date
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("find_recipe"))

    categories = mongo.db.categories.find().sort("category", 1)
    return render_template("add_recipe.html", categories=categories)


# Edit Recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    # Following code to edit recipe and update database
    if request.method == "POST":
        todays_date = datetime.today().strftime('%Y-%m-%d')
        submit = {
            "category": request.form.get("category"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"],
            "date_added": todays_date
        }

        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category", 1)
    return render_template("edit_recipe.html",
                           recipe=recipe,
                           categories=categories)


# Delete Recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("find_recipe"))


# Find a Recipe page
@app.route("/find_recipe")
def find_recipe():
    recipes = mongo.db.recipes.find().sort("date_added", -1)
    return render_template("recipes.html", recipes=recipes)


# Search for a recipe
@app.route("/search", methods=["GET", "POST"])
def search():
    search = request.form["search"]
    search_results = mongo.db.recipes.find({"recipe_name": search})
    print(search_results.count())
    # for doc in search_results:
        # print(doc['recipe_name'])

    return render_template("search_results.html", search_results=search_results)


# View Recipe
@app.route("/view_recipe/<recipe_id>", methods=['GET'])
def view_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html", recipe=recipe)

    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
