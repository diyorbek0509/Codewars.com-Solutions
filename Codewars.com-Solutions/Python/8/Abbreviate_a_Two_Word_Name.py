def abbrev_name(name: str):
    a, b = name.split()
    return f"{a[0].upper()}.{b[0].upper()}"