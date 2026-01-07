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
        "image_gallery": ["media/perfectly-runny-soft-boiled-eggs.jpg"],
        "main_ingredients": [
            "Eggs",
            "Water",
            "Salt"
        ],
        "cooking_method": "boiling",
        "main_cooking_apparatus": "pot",
        "equipment":[
            "Pot",
            "Tongs",
            "Bowl"
        ],
        "estimated_time_required_in_minutes": 10,
        "one_serving_visual_reference": "1 egg",
        "one_serving_equivalent_in_grams": 50,
        "cooking_instructions": [
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
        "diet_friendly_to": [
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
        "notorious_nutrient_deficiencies": [
            "Ascorbic acid (vitamin C)"
        ],
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
    { 
        "title": "Pan-fried burgers patties", 
        "slug": "pan-fried-burger-patties", 
        "image_gallery": ["media/pan-fried-burgers.jpg"], 
        "main_ingredients": [
            "ground beef", 
            "salt", 
            "animal fat (for greasing the skillet)"
        ], 
        "cooking_method": "frying",
        "main_cooking_apparatus": "skillet",
        "equipment": [
            "woodboard", 
            "skillet", 
            "spatula"
        ], 
        "estimated_time_required_in_minutes": 30,
        "one_serving_visual_reference": "1 patty",
        "one_serving_equivalent_in_grams": 300,
        "cooking_instructions": [
            "Form patties",
            "salt patties",
            "Heat skillet over medium-high heat", 
            "Cook patties for 4 minutes on each side"
        ],  
        "diet_friendly_to": [
            "carnivore",
            "keto",
            "low-carb"
        ],
        "health_profile": "healthy",
        "health_benefits": [
            "Rich source of creatine",
            "High in bioavailable iron",
            "Rich in B vitamins, especially B12"
        ],
        "notorious_nutrient_deficiencies": [
            "vitamin C",
            "Cholesterol"
        ],
        "nutritional_information_per_serving": {
            "protein_in_grams": 22,
            "total_fat_in_grams": 20,
            "saturated_fat_in_grams": 8,
            "cholesterol_in_mg": 80,
            "carbohydrates_in_grams": 0,
            "fiber_in_grams": 0,
            "sugar_in_grams": 0
        },
        "preparation_style": "simple",
        "origin_of_recipe": "unknown",
        "recipe_type": "Everyday cooking",
        "origin_of_recipe_image_icon": "imagine an image here",
        "references_if_any": "imagine I got this from a cookbook"
    },
    { 
        "title": "Scrambled eggs",
        "slug": "scrambled-eggs",
        "image_gallery": ["media/scrambled-eggs.jpg"],
        "main_ingredients": [
            "eggs", 
            "butter",
            "salt"
        ], 
        "cooking_method": "frying",
        "main_cooking_apparatus": "skillet",
        "equipment": [
            "bowl",
            "fork",
            "skillet",
            "spatula"
        ], 
        "estimated_time_required_in_minutes": 10,
        "one_serving_visual_reference": "6 eggs",
        "one_serving_equivalent_in_grams": 300,
        "cooking_instructions": [
            "Crack eggs into bowl",
            "Whisk eggs", 
            "Melt butter in skillet", 
            "Pour eggs into skillet", 
            "Cook while stirring until fluffy"
        ],  
        "diet_friendly_to": [
            "vegetarian",
            "low-carb",
            "carnivore","keto"
        ],
        "health_profile": "healthy",
        "health_benefits": [
            "Contains a bit of every single micronutrient your body needs except for vitamin C",
            "Best quality protein source available",
            "Rich in choline which is important for brain health",
            "Contains lutein and zeaxanthin which are important for eye health"
        ],
        "notorious_nutrient_deficiencies": [
            "Ascorbic acid (vitamin C)"
        ],
        "nutritional_information_per_serving": {
            "protein_in_grams": 36,
            "total_fat_in_grams": 30,
            "saturated_fat_in_grams": 9,
            "cholesterol_in_mg": 555,
            "carbohydrates_in_grams": 2,
            "fiber_in_grams": 0,
            "sugar_in_grams": 2
        },
        "preparation_style": "simple",
        "origin_of_recipe": "unknown",
        "recipe_type": "Everyday cooking",
        "origin_of_recipe_image_icon": "🇫🇷",
        "references_if_any": "imagine I got this from a cookbook"
    },
    { 
        "title": "Italian pork sausage",
        "slug": "italian-pork-sausage",
        "image_gallery": ["media/italian-pork-sausage.jpg"],
        "main_ingredients": [
            "pork sausages"
        ], 
        "cooking_method": "frying",
        "main_cooking_apparatus": "skillet",
        "equipment": [
            "skillet",
            "tongs"
        ], 
        "estimated_time_required_in_minutes": 25,
        "one_serving_visual_reference": "2 sausage links",
        "one_serving_equivalent_in_grams": 160,
        "cooking_instructions": [
            "Heat skillet over medium heat",
            "Add sausage links",
            "Cook, turning occasionally, until browned and cooked through"
        ], 
        "diet_friendly_to": [
            "carnivore",
            "keto",
            "low-carb"
        ],
        "health_profile": "healthy",
        "health_benefits": [
            "Rich source of thiamine (vitamin B1)",
            "Rich source of cholesterol"
        ],
        "notorious_nutrient_deficiencies": [
            "vitamin C"
        ],
        "nutritional_information_per_serving": {
            "protein_in_grams": 14,
            "total_fat_in_grams": 22,
            "saturated_fat_in_grams": 8,
            "cholesterol_in_mg": 60,
            "carbohydrates_in_grams": 2,
            "fiber_in_grams": 0,
            "sugar_in_grams": 0
        },
        "preparation_style": "simple",
        "origin_of_recipe": "unknown",
        "recipe_type": "Everyday cooking",
        "origin_of_recipe_image_icon": "🇮🇹",
        "references_if_any": "imagine I got this from a cookbook"
    },
    { 
        "title": "Medovik",
        "slug": "medovik",
        "image_gallery": ["media/medovik.jpg"],
        "main_ingredients": [
            "honey",
            "flour",
            "eggs",
            "sugar",
            "butter",
            "sour cream"
        ], 
        "cooking_method": "baking",
        "main_cooking_apparatus": "oven",
        "equipment": [
            "mixing bowls",
            "whisk",
            "baking pans",
            "oven"
        ],
        "estimated_time_required_in_minutes": 260,
        "one_serving_visual_reference": "1 slice",
        "one_serving_equivalent_in_grams": 120,
        "cooking_instructions": [
            "Prepare the dough", 
            "Bake the layers",
            "Prepare the cream",
            "Assemble the cake",
            "Chill before serving"
        ], 
        "diet_friendly_to": [
            "vegetarian"
        ],
        "health_profile": "indulgent",
        "health_benefits": [
            "Good source of joyful moments, specially when shared with loved ones"
        ],
        "notorious_nutrient_deficiencies": [
            "Cholesterol",
            "vitamins",
            "minerals",
        ],
        "nutritional_information_per_serving": {
            "protein_in_grams": 3,
            "total_fat_in_grams": 15,
            "saturated_fat_in_grams": 9,
            "cholesterol_in_mg": 50,
            "carbohydrates_in_grams": 30,
            "fiber_in_grams": 1,
            "sugar_in_grams": 20
        },
        "preparation_style": "elaborate",
        "origin_of_recipe": "Russia",
        "recipe_type": "Dessert",
        "origin_of_recipe_image_icon": "🇷🇺",
        "references_if_any": "imagine I got this from a cookbook"
    },
    { 
        "title": "Cheesecake",
        "slug": "cheesecake",
        "image_gallery": ["media/cheesecake.jpg"],
        "main_ingredients": [
            "cream cheese",
            "sweetener",
            "eggs"
        ],
        "cooking_method": "baking",
        "main_cooking_apparatus": "oven",
        "equipment": [
            "mixing bowl",
            "springform pan",
            "oven"
        ],
        "estimated_time_required_in_minutes": 300,
        "one_serving_visual_reference": "1 slice",
        "one_serving_equivalent_in_grams": 150,
        "cooking_instructions": [
            "Prepare the crust",
            "Mix the filling",
            "Pour filling into crust",
            "Bake the cheesecake",
            "Chill before serving"
        ],
        "diet_friendly_to": [
            "vegetarian"
        ],
        "health_profile": "indulgent",
        "health_benefits": [
            "Good source of joy when shared with friends and family"
        ],
        "notorious_nutrient_deficiencies": [
            "vitamins",
            "minerals"
        ],
        "nutritional_information_per_serving": {
            "protein_in_grams": 6,
            "total_fat_in_grams": 25,
            "saturated_fat_in_grams": 15,
            "cholesterol_in_mg": 80,
            "carbohydrates_in_grams": 20,
            "fiber_in_grams": 0,
            "sugar_in_grams": 15
        },
        "preparation_style": "elaborate",
        "origin_of_recipe": "unknown",
        "recipe_type": "Dessert",
        "origin_of_recipe_image_icon": "imagine an image here",
        "references_if_any": "imagine I got this from a cookbook"
    }

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
