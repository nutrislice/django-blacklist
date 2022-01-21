import re

_IP_PATTERN = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')


def sanitize_ip(ip_str: str) -> str:
    """
    >>> sanitize_ip(None)
    ''
    >>> sanitize_ip('')
    ''
    >>> sanitize_ip('65.2.3.4')
    '65.2.3.4'
    >>> sanitize_ip('some junk),65.26.12.345')
    '65.26.12.345'
    >>> sanitize_ip('65.26.12.345,some jumk),')
    '65.26.12.345'
    """
    if not ip_str:
        return ''
    m = _IP_PATTERN.search(ip_str)
    if m:
        return m.group(0)
    return ''
