from urllib.parse import urlparse

def validate_hostname(url: str) -> bool:
    """Validates if the given URL is a valid hostname"""
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme and parsed_url.netloc)
