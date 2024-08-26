import urllib.parse
import tldextract
LOCALHOST_PATH='C:/Users/HP/Desktop/'
DIRECTORY_NAME='Malicious-Web-Content-Detection-Using-Machine-Learning'


def extract_features(url):
    parsed_url = urllib.parse.urlparse(url)
    domain_extract = tldextract.extract(url)
    domain = domain_extract.domain
    suffix = domain_extract.suffix

    features = []

    # Append features to the list
    features.append(1 if domain.isdigit() else 0)  # UsingIP
    features.append(1 if len(url) > 75 else 0)  # LongURL
    features.append(1 if len(url) < 54 else 0)  # ShortURL
    features.append(1 if '@' in parsed_url.netloc else 0)  # Symbol@
    features.append(1 if '//' in parsed_url.path else 0)  # Redirecting//
    features.append(1 if '-' in domain else 0)  # PrefixSuffix-
    features.append(url.count('.') - 2)  # SubDomains
    features.append(1 if parsed_url.scheme == 'https' else 0)  # HTTPS
    features.append(1 if len(domain) + len(suffix) > 15 else -1)  # DomainRegLen
    features.append(1 if 'favicon.ico' in parsed_url.path else 0)  # Favicon
    features.append(1 if ':' in parsed_url.netloc else 0)  # NonStdPort
    features.append(1 if 'https' in url and '//' + domain in url else 0)  # HTTPSDomainURL
    features.append(1 if '?' in parsed_url.path else 0)  # RequestURL
    features.append(1 if '#' in parsed_url.path else 0)  # AnchorURL
    features.append(1 if '<script>' in url else 0)  # LinksInScriptTags
    features.append(1 if 'serverformhandler' in parsed_url.query.lower() else 0)  # ServerFormHandler
    features.append(1 if 'mailto:' in url else 0)  # InfoEmail
    features.append(1 if domain_extract.subdomain else 0)  # AbnormalURL
    features.append(1 if domain_extract.subdomain and domain_extract.subdomain != 'www' else 0)  # WebsiteForwarding
    features.append(1 if 'onmouseover' in url else 0)  # StatusBarCust
    features.append(1 if 'oncontextmenu' in url else 0)  # DisableRightClick
    features.append(1 if 'window.open' in url else 0)  # UsingPopupWindow
    features.append(1 if '<iframe>' in url else 0)  # IframeRedirection
    features.append(1 if '-' in parsed_url.netloc else 0)  # AgeofDomain
    features.append(1 if 'dns-record' in parsed_url.query else 0)  # DNSRecording
    features.append(1 if 'traffic' in parsed_url.query else 0)  # WebsiteTraffic
    features.append(1 if 'pagerank' in parsed_url.query else 0)  # PageRank
    features.append(1 if 'google-index' in parsed_url.query else 0)  # GoogleIndex
    features.append(1 if 'linksto' in parsed_url.query else 0)  # LinksPointingToPage
    features.append(1 if 'stats-report' in parsed_url.query else 0)  # StatsReport


    return features

