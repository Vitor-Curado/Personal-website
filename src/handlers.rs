use crate::api::HealthResponse;
use crate::repository::mock_food_data;
use crate::state::AppState;
use crate::templates::{
    AssetsTemplate, BlogTemplate, ContactTemplate, FoodDetailTemplate, FoodTemplate, IndexTemplate,
    ResumeTemplate,
};

use axum::Json;
use axum::extract::State;
use axum::http::StatusCode;
use axum::{
    extract::Path,
    response::{Html, IntoResponse},
};

use askama::Template;

pub async fn home(State(app_state): State<AppState>) -> impl IntoResponse {
    match (IndexTemplate {
        title: "Home",
        favicon: "home-icon.png",
        readme_html: app_state.readme_html.clone(),
    })
    .render()
    {
        Ok(html) => Html(html).into_response(),
        Err(_) => (
            axum::http::StatusCode::INTERNAL_SERVER_ERROR,
            "Template rendering failed",
        )
            .into_response(),
    }
}

/// Renders the food page.
///
/// # Panics
/// This function will panic if the template rendering fails.
pub async fn food(State(app_state): State<AppState>) -> impl IntoResponse {
    let template = FoodTemplate {
        title: "Food",
        favicon: "food-icon.png",
        foods: app_state.food_data.clone(),
    };

    Html(template.render().unwrap())
}

/// Renders the food detail page for a given slug.
/// # Arguments
/// * `slug` - The slug of the food item to display details for.
/// # Errors
/// Returns a `StatusCode::NOT_FOUND` if no food item matches the provided slug.
/// # Panics
/// This function will panic if the template rendering fails.
pub async fn food_detail(Path(slug): Path<String>) -> Result<Html<String>, StatusCode> {
    let foods = mock_food_data();

    let food = foods
        .iter()
        .find(|f| f.slug == slug)
        .ok_or(StatusCode::NOT_FOUND)?;

    let template = FoodDetailTemplate {
        title: food.title.to_string(),
        favicon: "food",
        food,
    };

    Ok(Html(template.render().unwrap()))
}

/// Renders the resume page.
/// # Panics
/// This function will panic if the template rendering fails.
pub async fn resume() -> impl IntoResponse {
    Html(
        ResumeTemplate {
            title: "Resume",
            favicon: "resume-icon.png",
        }
        .render()
        .unwrap(),
    )
}

/// Returns a JSON response indicating the health status of the application.
/// # Panics
/// This function will panic if the template rendering fails.
pub async fn health() -> Json<HealthResponse> {
    Json(HealthResponse { status: "ok" })
}

/// Renders the blog page.
/// # Panics
/// This function will panic if the template rendering fails.
pub async fn blog() -> impl IntoResponse {
    Html(
        BlogTemplate {
            title: "Blog",
            favicon: "blog-icon.png",
        }
        .render()
        .unwrap(),
    )
}

/// Renders the contact page.
/// # Panics
/// This function will panic if the template rendering fails.
pub async fn contact() -> impl IntoResponse {
    Html(
        ContactTemplate {
            title: "Contact Me",
            favicon: "contact-icon.png",
        }
        .render()
        .unwrap(),
    )
}

/// Renders the assets page.
/// # Panics
/// This function will panic if the template rendering fails.
pub async fn assets() -> impl IntoResponse {
    Html(
        AssetsTemplate {
            title: "Assets",
            favicon: "assets-icon.png",
        }
        .render()
        .unwrap(),
    )
}
