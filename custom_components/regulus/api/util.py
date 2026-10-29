def latin_to_cp1250_converter(value: str) -> str:
    """The IR controller serves XML declared as windows-1250 without a charset header,
    so requests decodes it as ISO-8859-1. Re-decode STRING registers properly."""
    try:
        return value.encode("latin-1").decode("cp1250", errors="replace")
    except (UnicodeEncodeError, AttributeError):
        return value

def parse_ir_version(version: str) -> tuple[int, ...]:
    return tuple(int(part) for part in version.split("_"))

def is_version_lower_than(version: str, target: str) -> bool:
    return parse_ir_version(version) < parse_ir_version(target)

def is_version_higher_or_equal_than(version: str, target: str) -> bool:
    return parse_ir_version(version) >= parse_ir_version(target)

def is_version_in_list(version: str, versions: list[str]) -> bool:
    return version in versions