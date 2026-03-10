pub struct Config {
    pub port: u16,
}

impl Config {
    /// Load configuration from environment variables.
    /// This function reads the `PORT` environment variable and defaults to `3000` if not set.
    /// # Panics
    /// Panics if the `PORT` environment variable is set but cannot be parsed as a number.
    #[must_use]
    pub fn from_env() -> Self {
        let port = std::env::var("PORT")
            .unwrap_or_else(|_| "3000".to_string())
            .parse()
            .expect("PORT must be a number");

        Self { port }
    }
}
