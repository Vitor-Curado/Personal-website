use personal_website::router::app;
use tokio::net::TcpListener;

#[tokio::main]
async fn main() {
    let app = app();

    let listener = TcpListener::bind("0.0.0.0:3000").await.unwrap();
    println!("🚀 Listening on http://{}", listener.local_addr().unwrap());

    axum::serve(listener, app).await.unwrap();
}
