def format_response(text: str) -> str:
    """Cleans AI response for better display."""
    return text.strip().replace("\n", "\n\n")
