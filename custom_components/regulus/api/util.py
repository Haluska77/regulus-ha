def latin_to_cp1250_converter(value: str) -> str:
    """The IR controller serves XML declared as windows-1250 without a charset header,
    so requests decodes it as ISO-8859-1. Re-decode STRING registers properly."""
    try:
        return value.encode("latin-1").decode("cp1250", errors="replace")
    except (UnicodeEncodeError, AttributeError):
        return value