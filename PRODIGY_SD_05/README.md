# Web Scraping

This Python program extracts product information from a sample e-commerce website and saves the results to a CSV file.

## What it scrapes

The scraper targets `http://books.toscrape.com/`, a practice site built for web scraping exercises.

Extracted fields:

- `name`: product title
- `price`: product price
- `rating`: product star rating text
- `url`: product detail page link

## Usage

Run the scraper with:

```bash
python WebScraping.py
```

By default, it scrapes the first page and writes `products.csv`.

### Optional arguments

- `--pages N`: scrape the first `N` catalogue pages
- `--output FILE`: write results to `FILE`

Example:

```bash
python WebScraping.py --pages 3 --output scraped_books.csv
```

## Output

The script writes a CSV file with headers:

- `name`
- `price`
- `rating`
- `url`

It also prints a short summary of the scraped products.

## Notes

- This example uses the built-in Python `urllib` and `html.parser` modules.
- The target site `books.toscrape.com` is intended for learning scraping and is safe to crawl for small test batches.
