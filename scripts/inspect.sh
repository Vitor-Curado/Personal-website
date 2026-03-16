#!/bin/bash
set -e

echo "Security audit..."
cargo audit

echo "Binary size analysis..."
cargo bloat --release --crates

echo "Building documentation..."
cargo doc --no-deps

echo "Benchmarks..."
cargo bench || true