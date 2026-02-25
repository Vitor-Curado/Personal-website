use crate::templates::{ IndexTemplate, FoodTemplate, FoodDetailTemplate, BoardgamesTemplate, ResumeTemplate, AppsTemplate };
use axum::{ response::{ Html, IntoResponse }, extract::Path };
use askama::Template;
use std::fs;
use pulldown_cmark::{Parser, html};
use crate::data::mock_food_data;

fn load_readme() -> String {
    fs::read_to_string("/home/bucko/Documents/Buckos proprietary software/Personal-website/readme.md")
        .unwrap_or_else(|_| "# README not found".to_string())
}

fn markdown_to_html(md: &str) -> String {
    let parser = Parser::new(md);
    let mut output = String::new();
    html::push_html(&mut output, parser);
    output
}

pub async fn home() -> impl IntoResponse {
    let readme_md = load_readme();
    let readme_html = markdown_to_html(&readme_md);

    Html(
        IndexTemplate {
            title: "Home",
            favicon: "home-icon.png",
            readme_html,
        }
        .render()
        .unwrap(),
    )
}

pub async fn food() -> impl IntoResponse {
    let template = FoodTemplate {
        title: "Food",
        favicon: "food-icon.png",
        foods: mock_food_data(),
    };

    Html(template.render().unwrap())
}

pub async fn food_detail(Path(slug): Path<String>) -> impl IntoResponse {
    let foods = mock_food_data();

    let food = foods
        .iter()
        .find(|f| f.slug == slug)
        .unwrap();

    let template = FoodDetailTemplate {
        title: food.title.to_string(),
        favicon: "food",
        food,
    };

    Html(template.render().unwrap())
}

pub async fn resume() -> impl IntoResponse {
    Html(
        ResumeTemplate {
            title: "Resume",
            favicon: "resume-icon.png"
        }
        .render()
        .unwrap(),
    )
}

pub async fn apps() -> impl IntoResponse {
    Html(
        AppsTemplate {
            title: "Software",
            favicon: "software-icon.png"
        }
        .render()
        .unwrap(),
    )
}

pub async fn boardgames() -> impl IntoResponse {
    Html(
        BoardgamesTemplate {
            title: "Board Games",
            favicon: "boardgames-icon.png"
        }
        .render()
        .unwrap(),
    )
}