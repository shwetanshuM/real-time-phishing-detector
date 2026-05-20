from urllib.parse import urlparse


def extract_features(url):

    features = []
    parsed = urlparse(url)
    domain = parsed.netloc
    has_ip = any(char.isdigit() for char in domain)
    features.append(1 if has_ip else -1)
    features.append(1 if len(url) > 75 else -1)
    shorteners = [
        'bit.ly',
        'tinyurl',
        'goo.gl',
        't.co',
        'ow.ly',
        'is.gd'
    ]
    is_shortened = any(
        short in url
        for short in shorteners
    )
    features.append(1 if is_shortened else -1)
    features.append(1 if '@' in url else -1)
    features.append(1 if '-' in domain else -1)
    subdomains = domain.count('.')
    if subdomains <= 1:
        features.append(-1)
    elif subdomains == 2:
        features.append(0)
    else:
        features.append(1)
    features.append(1 if parsed.scheme == 'https' else -1)

    return features