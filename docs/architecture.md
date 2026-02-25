# Architecture

## Request Flow

Browser → Axum Router → Handler → Data → Template → HTML

## Modules

- main.rs — server startup and routing
- handlers.rs — request handlers
- models.rs — domain data structures
- templates.rs — Askama HTML templates
- data.rs — mock data provider
- api.rs — JSON response types

## Rendering

Server-side rendering using Askama templates.

## Static Files

Served via tower_http::ServeDir.