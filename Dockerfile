# ---------- Planner stage ----------
FROM rust:latest AS planner
WORKDIR /app

RUN cargo install cargo-chef

COPY . .
RUN cargo chef prepare --recipe-path recipe.json

# ---------- Builder stage ----------
FROM rust:latest AS builder
WORKDIR /app

RUN cargo install cargo-chef

COPY --from=planner /app/recipe.json recipe.json
RUN cargo chef cook --release --recipe-path recipe.json

COPY . .
RUN cargo build --release

# ---------- Runtime stage ----------
FROM debian:bookworm-slim
WORKDIR /app

RUN apt-get update && apt-get install -y \
    ca-certificates \
    libssl3 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/target/release/personal-website .

COPY templates ./templates
COPY static ./static
COPY readme.md ./readme.md

EXPOSE 3000

CMD ["./personal-website"]

# -- ---------- Healthcheck ----------
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:3000/health || exit 1