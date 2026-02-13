/* ------------------------
   Handlers (routes)
-------------------------*/

use crate::data::{ LOGS, PROJECTS, mock_food_data };
use crate::templates::{ IndexTemplate, FoodTemplate, FoodDetailTemplate, BoardgamesTemplate, ResumeTemplate, AppsTemplate };
use axum::{ response::{ Html, IntoResponse }, extract::Path };

use askama::Template;


pub async fn home() -> impl IntoResponse {
    let template = IndexTemplate {
        logs: LOGS,
        projects: PROJECTS,
    };
    Html(template.render().unwrap())
}

pub async fn food() -> impl IntoResponse {
    let template = FoodTemplate {
        foods: mock_food_data(),
    };
    Html(template.render().unwrap())
}

pub async fn food_detail(Path(_slug): Path<String>) -> impl IntoResponse {
    let template = FoodDetailTemplate {
        food: &mock_food_data()[0], // For simplicity, just using the first food item. In a real app, you'd look up by slug.
    };
    Html(template.render().unwrap())
}

pub async fn boardgames() -> impl IntoResponse {
    Html(BoardgamesTemplate.render().unwrap())
}

pub async fn resume() -> impl IntoResponse {
    Html(ResumeTemplate.render().unwrap())
}

pub async fn apps() -> impl IntoResponse {
    Html(AppsTemplate.render().unwrap())
}
