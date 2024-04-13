from playwright.sync_api import sync_playwright
from flask import Flask, request
import httpx
import jwt

app = Flask(__name__)

def hsw(req: str, host: str) -> str:
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(bypass_csp=True)
            page = context.new_page()
            url = jwt.decode(req, options={"verify_signature": False})['l']
            hsw = httpx.get(f"{url}/hsw.js").text
            page.goto(f"https://{host}")
            page.add_script_tag(content="Object.defineProperty(navigator, \"webdriver\", {\"get\": () => false})")
            page.add_script_tag(content=hsw)
            response = page.evaluate(f"hsw(\"{req}\")")
            page.close()
            return str(response)
    except Exception as e:
        print(e)
        return "None"
    
@app.route('/hsw', methods=['POST'])
def get_hsw():
    data = request.json
    req = data.get('req')
    host = data.get('host')
    result = hsw(req, host)
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")