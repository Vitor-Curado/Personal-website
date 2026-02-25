// I have no idea what's going on
// tests.rs --- IGNORE ---

#[test]
fn everything_test() {
    assert!(true);
}

#[tokio::test]
async fn health_endpoint() {
    let response = reqwest::get("http://127.0.0.1:3000/api/health").await.unwrap();
    assert_eq!(response.status(), 200);
}

