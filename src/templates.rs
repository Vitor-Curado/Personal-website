/* ------------------------
   Templates
-------------------------*/

use crate::models::{ Food, Log, Project };
use askama::Template;

#[derive(Template)]
#[template(path = "index.html")]
pub struct IndexTemplate<'a> {
    pub logs: &'a [Log],
    pub projects: &'a [Project],
}

#[derive(Template)]
#[template(path = "food.html")]
pub struct FoodTemplate {
    pub foods: Vec<Food>
}

#[derive(Template)]
#[template(path = "food_detail.html")]
pub struct FoodDetailTemplate<'a> {
    pub food: &'a Food,
}

#[derive(Template)]
#[template(path = "boardgames.html")]
pub struct BoardgamesTemplate;

#[derive(Template)]
#[template(path = "resume.html")]
pub struct ResumeTemplate;

#[derive(Template)]
#[template(path = "apps.html")]
pub struct AppsTemplate;
