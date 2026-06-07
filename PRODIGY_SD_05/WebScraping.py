import argparse
import csv
import os
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

BASE_URL = "http://books.toscrape.com/"


class ProductParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.products = []
        self.current = None
        self._in_article = False
        self._in_h3 = False
        self._in_price = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "article" and "product_pod" in attrs.get("class", ""):
            self._in_article = True
            self.current = {
                "name": "",
                "price": "",
                "rating": "",
                "url": "",
            }
            return

        if not self._in_article:
            return

        if tag == "h3":
            self._in_h3 = True

        if tag == "a" and self._in_h3:
            self.current["name"] = attrs.get("title", "").strip()
            self.current["url"] = urljoin(BASE_URL, attrs.get("href", "").strip())

        if tag == "p" and "price_color" in attrs.get("class", ""):
            self._in_price = True

        if tag == "p" and "star-rating" in attrs.get("class", ""):
            classes = attrs.get("class", "").split()
            rating_text = next((cls for cls in classes if cls.lower() != "star-rating"), "")
            self.current["rating"] = rating_text

    def handle_endtag(self, tag):
        if tag == "article" and self._in_article:
            if self.current is not None:
                self.products.append(self.current)
            self.current = None
            self._in_article = False

        if tag == "h3":
            self._in_h3 = False

        if tag == "p" and self._in_price:
            self._in_price = False

    def handle_data(self, data):
        if self._in_article and self._in_price and self.current is not None:
            self.current["price"] += data.strip()


def fetch_page(url):
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(request, timeout=10) as response:
            return response.read().decode("utf-8", errors="replace")
    except (HTTPError, URLError) as error:
        print(f"Failed to load page {url}: {error}")
        return ""


def scrape_page(url):
    html = fetch_page(url)
    if not html:
        return []

    parser = ProductParser()
    parser.feed(html)
    return parser.products


def scrape_pages(page_count):
    products = []
    for page in range(1, page_count + 1):
        if page == 1:
            page_url = BASE_URL
        else:
            page_url = urljoin(BASE_URL, f"catalogue/page-{page}.html")

        print(f"Scraping page {page}: {page_url}")
        products.extend(scrape_page(page_url))

    return products


def save_to_csv(products, output_path):
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, mode="w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "price", "rating", "url"])
        writer.writeheader()
        writer.writerows(products)

    print(f"Saved {len(products)} products to {output_path}")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_output = os.path.join(script_dir, "products.csv")

    parser = argparse.ArgumentParser(
        description="Scrape product data from books.toscrape.com and save it to a CSV file."
    )
    parser.add_argument(
        "--pages",
        type=int,
        default=1,
        help="Number of catalogue pages to scrape (default: 1)",
    )
    parser.add_argument(
        "--output",
        default=default_output,
        help=f"CSV output file path (default: {default_output})",
    )
    args = parser.parse_args()

    products = scrape_pages(args.pages)
    if not products:
        print("No products were extracted.")
        return

    save_to_csv(products, args.output)

    print("First 5 products:")
    for product in products[:5]:
        print(f"- {product['name']} | {product['price']} | {product['rating']}")


if __name__ == "__main__":
    main()
