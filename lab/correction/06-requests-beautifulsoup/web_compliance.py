import requests
import sys

from bs4 import BeautifulSoup

# Write a website image compliance tester. If a website contains an image which
# contains 'freedom' in the alt property, The website is NOT Rao Compliant!


def rao_compliant_image(image):
    alt_text = image.get('alt', '')
    return alt_text.lower().find('freedom') == -1


def rao_compliant_website(raw_html):
    soup = BeautifulSoup(raw_html)
    images = soup.findAll('img', '')

    for image in images:
        if not rao_compliant_image(image):
            return False

    return True


def main():
    url = sys.argv[1]
    response = requests.get(url)
    raw_html = response.text
    compliance = rao_compliant_website(raw_html)

    if compliance:
        print '*Website is Rao Compliant!*'
    else:
        print '*WARNING Website is NOT Rao Compliant!*'


if __name__ == '__main__':
    main()
