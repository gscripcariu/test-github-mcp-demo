#!/usr/bin/env python3
"""
GitHub MCP Test Application
A simple demo application for testing GitHub integration.
"""

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to GitHub MCP testing."

def main():
    """Main entry point."""
    print(greet("World"))
    print("GitHub MCP integration is working!")

if __name__ == "__main__":
    main()
