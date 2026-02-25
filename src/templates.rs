use crate::models::{ Food };
use askama::Template;

#[derive(Template)]
#[template(path = "index.html", escape = "none")]
pub struct IndexTemplate {
    pub title: &'static str,
    pub favicon: &'static str,
    pub readme_html: String
}

#[derive(Template)]
#[template(path = "food.html")]
pub struct FoodTemplate {
    pub title: &'static str,
    pub favicon: &'static str,
    pub foods: Vec<Food>
}

#[derive(Template)]
#[template(path = "food_detail.html")]
pub struct FoodDetailTemplate<'a> {
    pub title: String,
    pub favicon: &'static str,
    pub food: &'a Food,
}

#[derive(Template)]
#[template(path = "boardgames.html")]
pub struct BoardgamesTemplate {
    pub title: &'static str,
    pub favicon: &'static str
}

#[derive(Template)]
#[template(path = "resume.html")]
pub struct ResumeTemplate {
    pub title: &'static str,
    pub favicon: &'static str
}

#[derive(Template)]
#[template(path = "apps.html")]
pub struct AppsTemplate {
    pub title: &'static str,
    pub favicon: &'static str
}