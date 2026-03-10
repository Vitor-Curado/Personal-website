use crate::handlers::{assets, blog, contact, food, food_detail, health, home, resume};
use crate::state::AppState;
use axum::Router;
use axum::http::header::{HeaderName, HeaderValue};
use axum::routing::get;
use tower_http::compression::CompressionLayer;
use tower_http::services::ServeDir;
use tower_http::set_header::SetResponseHeaderLayer;
use tower_http::trace::TraceLayer;

pub fn app() -> Router {
    let static_service = ServeDir::new("static").precompressed_gzip();

    Router::new()
        .route("/", get(home))
        .route("/health", get(health))
        .route("/food", get(food))
        .route("/food/:slug", get(food_detail))
        .route("/resume", get(resume))
        .route("/blog", get(blog))
        .route("/contact", get(contact))
        .route("/assets", get(assets))
        .nest_service("/static", static_service)
        .layer(CompressionLayer::new())
        .layer(TraceLayer::new_for_http())
        .layer(SetResponseHeaderLayer::if_not_present(
            HeaderName::from_static("cache-control"),
            HeaderValue::from_static("public, max-age=86400"),
        ))
        .layer(SetResponseHeaderLayer::if_not_present(
            HeaderName::from_static("x-frame-options"),
            HeaderValue::from_static("DENY"),
        ))
        .layer(SetResponseHeaderLayer::if_not_present(
            HeaderName::from_static("x-content-type-options"),
            HeaderValue::from_static("nosniff"),
        ))
        .layer(SetResponseHeaderLayer::if_not_present(
            HeaderName::from_static("referrer-policy"),
            HeaderValue::from_static("no-referrer"),
        ))
        .with_state(AppState::new())
}
