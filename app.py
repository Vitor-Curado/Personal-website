from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

logs = [
    {"title": "title 1", "message": "bla bla bla", "timestamp": "2024-06-01 10:00:00"},
    {"title": "title 2","message": "foo foo foo", "timestamp": "2024-06-01 11:00:00"}
]

# Example data (temporary “database”)
projects = [
    {"title": "Portfolio Website", "description": "A personal portfolio made with Flask."},
    {"title": "Financial stats machine", "description": "An application to aggregate all of one's financial data for analysis and insights."},
    {"title": "Video game", "description": "A video game."}
]

foods = [
    {
        "title": "Soft-boiled Eggs",
        "slug": "soft-boiled-eggs",
        "image": "media/perfectly-runny-soft-boiled-eggs.jpg",
        "main-ingredients": [
            "Eggs",
            "Water",
            "Salt"
        ],
        "pairs-well-with": [
            "Meats",
            "Cheese",
            "Butter"
        ],
        "cooking_method": "boiling",
        "main_cooking_apparatus": "stove",
        "equipment":[
            "Pot",
            "Tongs",
            "Bowl"
        ],
        "estimated_time_required_in_minutes": 10,
        "one_serving_is": "1 egg",
        "one_serving_equivalent_in_grams": 50,
        "instructions": [
            "Place eggs in an empty pot",
            "Fill pot with enough water to cover eggs by about an inch",
            "Place pot on stove and bring water to a boil",
            "Leave eggs in boiling water for 2 minutes",
            "After 2 minutes, turn off the heat and leave it for two more minutes",
            "After a total of 4 minutes, use tongs to transfer eggs to a bowl of cold water",
            "Let eggs sit in cold water for at least five minutes to cool down",
            "Gently tap the eggs on a hard surface to crack the shell, then peel",
            "Sprinkle with salt and enjoy"
        ],
        "diet": [
            "low-carb",
            "keto",
            "keto-friendly",
            "carnivore",
            "vegetarian",
            "gluten-free",
            "dairy-free",
            "nut-free"
        ],
        "health_profile": "healthy",
        "health_benefits": [
            "Contains a bit of every single micronutrient your body needs except for vitamin C",
            "Best quality protein source available",
            "Rich in choline which is important for brain health",
            "Contains lutein and zeaxanthin which are important for eye health"
        ],
        "notorious_nutrient_deficiencies": [ "Ascorbic acid (vitamin C)" ],
        "nutritional_information_per_serving": {
            "protein_in_grams": 6,
            "total_fat_in_grams": 5,
            "saturated_fat_in_grams": 1.5,
            "cholesterol_in_mg": 185,
            "carbohydrates_in_grams": 1,
            "fiber_in_grams": 0,
            "sugar_in_grams": 0
        },
        "preparation_style": "simple",
        "origin_of_recipe": "unknown",
        "recipe_type": "Everyday cooking",
        "origin_of_recipe_image_icon": "imagine an image here",
        "references_if_any": "imagine I got this from a cookbook"
    },
    { "title": "Pan-fried burgers patties", "slug": "pan-fried-burger-patties", "image": "media/pan-fried-burgers.jpg", "ingredients": ["ground beef", "salt", "animal fat (for greasing the skillet)"], "equipment": ["woodboard", "skillet", "spatula"], "steps": ["Form patties", "salt patties", "Heat skillet over medium-high heat", "Cook patties for 4 minutes on each side"], "estimated-time-required": "30 minutes", "diet": ["carnivore", "keto", "low-carb"], "tags": ["BBQ", "Meat"] },
    { "title": "Scrambled eggs", "slug": "scrambled-eggs" ,"image": "media/scrambled-eggs.jpg", "ingredients": ["eggs", "butter", "salt"], "equipment": ["bowl", "fork", "skillet", "spatula"], "steps": ["Crack eggs into bowl", "Whisk eggs", "Melt butter in skillet", "Pour eggs into skillet", "Cook while stirring until fluffy"], "estimated-time-required": "15 minutes", "diet": ["vegetarian", "low-carb", "carnivore", "keto"] },
    { "title": "Italian pork sausage", "slug": "italian-pork-sausage","image": "media/italian-pork-sausage.jpg", "ingredients": ["pork sausages"], "equipment": ["skillet", "tongs"], "steps": ["Heat skillet over medium heat", "Add sausage links", "Cook, turning occasionally, until browned and cooked through"], "estimated-time-required": "25 minutes", "diet": ["carnivore", "keto", "low-carb"] },
    { "title": "Medovik", "slug": "medovik", "image": "media/medovik.jpg", "ingredients": ["honey", "flour", "eggs", "sugar", "butter", "sour cream"], "equipment": ["mixing bowls", "whisk", "baking pans", "oven"], "steps": ["Prepare the dough", "Bake the layers", "Prepare the cream", "Assemble the cake", "Chill before serving"], "estimated-time-required": "4 hours", "diet": ["vegetarian"] },
    { "title": "Cheesecake", "slug": "cheesecake", "image": "media/cheesecake.jpg", "ingredients": ["cream cheese", "sweetener", "eggs"], "equipment": ["mixing bowl", "springform pan", "oven"], "steps": ["Prepare the crust", "Mix the filling", "Pour filling into crust", "Bake the cheesecake", "Chill before serving"], "estimated-time-required": "5 hours", "diet": ["vegetarian"] }

]

def slugify(title):
    return title.lower().strip().replace(" ", "-")

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
