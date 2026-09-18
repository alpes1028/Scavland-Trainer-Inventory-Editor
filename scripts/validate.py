# Build: 5e364b9a01ef040585b309e6f9f890ac

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
