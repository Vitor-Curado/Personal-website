from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

logs = [
    {"title": "title 1", "message": "bla bla bla", "timestamp": "2024-06-01 10:00:00"},
    {"title": "title 2","message": "foo foo foo", "timestamp": "2024-06-01 11:00:00"}
]

# Example data (temporary “database”)
projects = [
    {"title": "Portfolio Website", "description": "A personal portfolio made with Flask."},
    {"title": "Cybersecurity Dashboard", "description": "Real-time system monitoring tool."},
]

foods = [
    { "title": "Soft-boiled eggs", "slug": "soft-boiled-eggs", "image": "media/perfectly-runny-soft-boiled-eggs.jpg", "ingredients": ["eggs", "salt"], "equipment": ["skillet", "slotted spoon", "timer"], "steps": ["Bring water to a boil", "Gently add eggs", "Cook for 6 minutes", "Remove and cool eggs", "Serve"], "estimated-time-required": "10 minutes" },
    { "title": "Pan-fried burgers patties", "slug": "pan-fried-burger-patties", "image": "media/pan-fried-burgers.jpg", "ingredients": ["ground beef", "salt", "animal fat (for greasing the skillet)"], "equipment": ["woodboard", "skillet", "spatula"], "steps": ["Form patties", "salt patties", "Heat skillet over medium-high heat", "Cook patties for 4 minutes on each side"], "estimated-time-required": "30 minutes" },
    { "title": "Scrambled eggs", "slug": "scrambled-eggs" ,"image": "media/scrambled-eggs.jpg", "ingredients": ["eggs", "butter", "salt"], "equipment": ["bowl", "fork", "skillet", "spatula"], "steps": ["Crack eggs into bowl", "Whisk eggs", "Melt butter in skillet", "Pour eggs into skillet", "Cook while stirring until fluffy"], "estimated-time-required": "15 minutes" },
    { "title": "Italian pork sausage", "slug": "italian-pork-sausage","image": "media/italian-pork-sausage.jpg", "ingredients": ["pork sausages"], "equipment": ["skillet", "tongs"], "steps": ["Heat skillet over medium heat", "Add sausage links", "Cook, turning occasionally, until browned and cooked through"], "estimated-time-required": "25 minutes" },
    { "title": "Medovik", "slug": "medovik", "image": "media/medovik.jpg", "ingredients": ["honey", "flour", "eggs", "sugar", "butter", "sour cream"], "equipment": ["mixing bowls", "whisk", "baking pans", "oven"], "steps": ["Prepare the dough", "Bake the layers", "Prepare the cream", "Assemble the cake", "Chill before serving"], "estimated-time-required": "4 hours" },
    { "title": "Cheesecake", "slug": "cheesecake", "image": "media/cheesecake.jpg", "ingredients": ["cream cheese", "sweetener", "eggs"], "equipment": ["mixing bowl", "springform pan", "oven"], "steps": ["Prepare the crust", "Mix the filling", "Pour filling into crust", "Bake the cheesecake", "Chill before serving"], "estimated-time-required": "5 hours" }
]

def slugify(title):
    return title.lower().trim().replace(" ", "-")


@app.route("/")
def home():
    return render_template("index.html", projects=projects, logs=logs)

@app.route("/add", methods=["POST"])
def add_project():
    title = request.form.get("title")
    description = request.form.get("description")
    if title and description:
        projects.append({"title": title, "description": description})
    return redirect(url_for("home"))

@app.route("/food")
def food():
    return render_template("food.html", foods=foods)

@app.route("/food/<slug>")
def food_detail(slug):
    food_item = next((food for food in foods if food["slug"] == slug), None)
    if food_item:
        return render_template("food_detail.html", food=food_item)
    else:
        return "Food item not found", 404

@app.route("/boardgames")
def boardgames():
    return render_template("boardgames.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/apps")
def apps():
    return render_template("apps.html")

if __name__ == "__main__":
    app.run(debug=True)
