#if __name__ == "__main__":
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from os import getenv

class WhatsAppConfig:
    def __init__(self):
        load_dotenv()
        self.playWright = None
        self.browser = None
        self.page = None
        self.botDir = getenv("CAMINHO_SESSAO")
    
    def startBrowser(self):

        self.playWright = sync_playwright().start()
        self.browser = self.playWright.chromium.launch_persistent_context(
            user_data_dir=self.botDir,
            headless=False,
            no_viewport=True
        )
        self.page = self.browser.pages[0]
        self.page.goto("https://web.whatsapp.com")
        return self.page
    
    def closeBrowser(self):
        if self.browser:
            self.browser.close()

        if self.playWright:
            self.playWright.stop()