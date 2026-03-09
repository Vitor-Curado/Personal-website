use pulldown_cmark::{Parser, html};
use std::fs;

#[must_use]
pub fn load_readme() -> String {
    fs::read_to_string("./readme.md") // relative to working dir in container
        .unwrap_or_else(|_| "# README not found".to_string())
}

#[must_use]
pub fn markdown_to_html(md: &str) -> String {
    let parser = Parser::new(md);
    let mut output = String::new();
    html::push_html(&mut output, parser);
    output
}

// Unit tests
#[test]
fn converts_multiple_markdown_features() {
    let input = "# Title\n\n**Bold** text";
    let html = markdown_to_html(input);

    assert!(html.contains("<h1>Title</h1>"));
    assert!(html.contains("<strong>Bold</strong>"));
}
