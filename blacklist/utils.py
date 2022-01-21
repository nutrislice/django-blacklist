import re

_IP_PATTERN = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')


def sanitize_ip(ip_str: str) -> str:
    if not ip_str:
        return ''
    m = _IP_PATTERN.search(ip_str)
    if m:
        return m.group(0)
    return ''
