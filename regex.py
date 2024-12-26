import re


def is_valid_url(url):
    pattern = r"^https?:\/\/(www\.)?[a-zA-Z0-9-]+\.[a-z]{2,6}([\/][^\s]*)?$"

    if re.match(pattern, url):
        return True
    else:
        return False

url = "https://tiki.vn/dien-thoai-may-tinh-bang/c1789?src=mega-menu"
print(is_valid_url(url))

url_invalid = "https://tiki.vn/dien thoa i-may-tinh-bang/c1789?src=mega-menu"
print(is_valid_url(url_invalid))
