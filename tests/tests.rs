use axum::body::Body;
use axum::http::{Request, StatusCode};
use tower::util::ServiceExt; // for oneshot

use personal_website::router::app;

#[tokio::test]
async fn health_endpoint_returns_ok() {
    let app = app();

    let response = app
        .oneshot(
            Request::builder()
                .uri("/health")
                .body(Body::empty())
                .unwrap(),
        )
        .await
        .unwrap();

    assert_eq!(response.status(), StatusCode::OK);
}
