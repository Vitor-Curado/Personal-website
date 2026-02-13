mod models;
mod routes;
mod data;
mod templates;

use axum::{
    routing::get,
    Router,
};

use std::net::SocketAddr;
use tower_http::services::ServeDir;

use crate::routes::{ home, food, food_detail, boardgames, resume, apps };

/* ------------------------
   Main
-------------------------*/

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/", get(home))
        .route("/food", get(food))
        .route("/food/:slug", get(food_detail))
        .route("/boardgames", get(boardgames))
        .route("/resume", get(resume))
        .route("/apps", get(apps))
        .nest_service("/static", ServeDir::new("static"))
        .nest_service("/media", ServeDir::new("media"));

    let addr = SocketAddr::from(([127, 0, 0, 1], 8000));
    println!("🚀 Server running at http://{}", addr);

    let listener = tokio::net::TcpListener::bind(addr).await.unwrap();
    axum::serve(listener, app).await.unwrap();
}