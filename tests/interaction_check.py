import argparse
import json

from playwright.sync_api import sync_playwright


parser = argparse.ArgumentParser()
parser.add_argument("--url", default="http://127.0.0.1:4173")
args = parser.parse_args()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 960})
    console_errors = []
    page.on("console", lambda message: console_errors.append(message.text) if message.type == "error" else None)
    page.goto(args.url, wait_until="networkidle")

    hero_box = page.locator('.hero-frame').bounding_box()
    page.mouse.move(hero_box["x"] + hero_box["width"] * 0.72, hero_box["y"] + hero_box["height"] * 0.38)
    page.wait_for_timeout(80)
    pointer_response = page.evaluate(
        "getComputedStyle(document.querySelector('.hero-frame')).getPropertyValue('--glass-x').trim()"
    )

    page.locator('.site-nav a[href="#work"]').click()
    page.wait_for_timeout(450)
    desktop = page.evaluate(
        """
        () => ({
          hash: location.hash,
          scrollY: window.scrollY,
          current: document.querySelector('.site-nav a[aria-current]')?.getAttribute('href') || null,
          horizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
          visibleLinks: [...document.querySelectorAll('a')].filter((link) => {
            const style = getComputedStyle(link);
            const box = link.getBoundingClientRect();
            return style.visibility !== 'hidden' && style.display !== 'none' && box.width > 0 && box.height > 0;
          }).length,
          motionReady: document.documentElement.classList.contains('motion-ready'),
          pageReady: document.body.classList.contains('is-ready'),
          evidenceLive: document.querySelector('.feature-project').classList.contains('is-evidence-live')
        })
        """
    )

    page.set_viewport_size({"width": 390, "height": 844})
    page.goto(args.url, wait_until="networkidle")
    mobile = page.evaluate(
        """
        () => ({
          horizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
          navDisplay: getComputedStyle(document.querySelector('.site-nav')).display,
          githubVisible: document.querySelector('.site-header a[href*="github.com"]').getBoundingClientRect().width > 0,
          heroHeight: Math.round(document.querySelector('.hero-frame').getBoundingClientRect().height),
          bodyHeight: document.documentElement.scrollHeight
        })
        """
    )

    assert desktop["hash"] == "#work"
    assert desktop["scrollY"] > 500
    assert not desktop["horizontalOverflow"]
    assert desktop["visibleLinks"] >= 15
    assert desktop["motionReady"]
    assert desktop["pageReady"]
    assert desktop["evidenceLive"]
    assert pointer_response not in ("", "0px")
    assert not mobile["horizontalOverflow"]
    assert mobile["navDisplay"] == "none"
    assert mobile["githubVisible"]
    assert mobile["heroHeight"] == 1040
    assert not console_errors

    page.emulate_media(reduced_motion="reduce")
    page.set_viewport_size({"width": 1440, "height": 960})
    page.goto(args.url, wait_until="networkidle")
    reduced = page.evaluate(
        """
        () => ({
          plateAnimation: getComputedStyle(document.querySelector('.plate-glass')).animationName,
          connectorAnimation: getComputedStyle(document.querySelector('.connector.active')).animationName
        })
        """
    )
    assert reduced["plateAnimation"] == "none"
    assert reduced["connectorAnimation"] == "none"

    print(json.dumps({
        "desktop": desktop,
        "mobile": mobile,
        "pointerResponse": pointer_response,
        "reducedMotion": reduced,
        "consoleErrors": console_errors,
    }, indent=2))
    browser.close()
