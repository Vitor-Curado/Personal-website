mod models;
mod routes;
mod data;
mod templates;

use axum::{
    routing::get,
    Router,
};

use tokio::net::UnixListener;
use std::path::Path;

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


    let socket_path = "/run/Personal-website/gunicorn.sock";

    if Path::new(socket_path).exists() {
        std::fs::remove_file(socket_path).unwrap();
    }

    println!("🚀 Starting server on socket: {}", socket_path);
    
    let listener = UnixListener::bind(socket_path).unwrap();
    axum::serve(listener, app).await.unwrap();
}