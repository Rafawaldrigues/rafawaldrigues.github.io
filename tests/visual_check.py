import argparse
import json
from pathlib import Path

from playwright.sync_api import sync_playwright


parser = argparse.ArgumentParser()
parser.add_argument("--url", default="http://127.0.0.1:4173")
parser.add_argument("--output", required=True)
parser.add_argument("--width", type=int, required=True)
parser.add_argument("--height", type=int, required=True)
parser.add_argument("--full-page", action="store_true")
args = parser.parse_args()

output = Path(args.output)
output.parent.mkdir(parents=True, exist_ok=True)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page(
        viewport={"width": args.width, "height": args.height},
        device_scale_factor=1,
        reduced_motion="reduce",
    )
    console_errors = []
    page.on("console", lambda message: console_errors.append(message.text) if message.type == "error" else None)
    page.goto(args.url, wait_until="networkidle")
    page.evaluate("document.documentElement.classList.add('capture-ready')")
    page.screenshot(path=str(output), full_page=args.full_page)
    diagnostics = page.evaluate(
        """
        () => ({
          title: document.title,
          scrollWidth: document.documentElement.scrollWidth,
          clientWidth: document.documentElement.clientWidth,
          scrollHeight: document.documentElement.scrollHeight,
          images: [...document.images].map((image) => ({
            src: image.getAttribute('src'),
            complete: image.complete,
            naturalWidth: image.naturalWidth,
            naturalHeight: image.naturalHeight
          })),
          links: [...document.querySelectorAll('a')].map((link) => ({
            text: link.textContent.trim(),
            href: link.href
          }))
        })
        """
    )
    diagnostics["consoleErrors"] = console_errors
    print(json.dumps(diagnostics, indent=2))
    browser.close()
