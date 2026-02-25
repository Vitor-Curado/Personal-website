mod models;
mod handlers;
mod repository;
mod templates;
mod api;

#[cfg(test)]
mod tests;

use axum::{ routing::get, Router };
use tokio::net::TcpListener;
use crate::handlers::{ home, food, food_detail, boardgames, resume, apps, health };
use tower_http::services::ServeDir;

#[tokio::main]
async fn main() {

    let app = Router::new()
        .route("/", get(home))
        .route("/food", get(food))
        .route("/food/:slug", get(food_detail))
        .route("/boardgames", get(boardgames))
        .route("/resume", get(resume))
        .route("/apps", get(apps))
        .route("/api/health", get(health))
        .nest_service("/static", ServeDir::new("static"))
        .nest_service("/media", ServeDir::new("media"));

    let listener = TcpListener::bind("127.0.0.1:3000").await.unwrap();
    println!("🚀 Listening on http://{}", listener.local_addr().unwrap());

    axum::serve(listener, app).await.unwrap();
}