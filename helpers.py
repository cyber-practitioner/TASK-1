
def sanitise_input(s):
    import re, html
    allowed_chars = "a-zA-Z0-9\_\,\s\.\-\!\?"
    s = re.sub(r'[^{}]+'.format(allowed_chars), '', s)
    return html.escape(s)

def sanitise_number_input(n):
    import re
    allowed_chars = "0-9"
    n = re.sub(r'[^{}]+'.format(allowed_chars), '', str(n))
    try:
        return int(n)
    except ValueError:
        return 0