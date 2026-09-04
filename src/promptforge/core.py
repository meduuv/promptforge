def template(text: str, defaults=None):
    defaults={} if defaults is None else dict(defaults)
    return text.format_map(defaults)
