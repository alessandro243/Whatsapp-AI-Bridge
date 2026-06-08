from WhatsAppConfig import WhatsAppConfig
from WhatsAppLocators import WhatsAppLocators

class WhatsAppBot:
    def __init__(self):
        self.config = WhatsAppConfig()
        self.page = self.startBrowser_()
        self.locator = WhatsAppLocators(self.page)

    def startBrowser_(self):
        return self.config.startBrowser()
    
    def closeBrowser_(self):
        self.config.closeBrowser()
    
    def searchElementByState_(self, state):
        self.locator.searchElementByState(state)

    def searchContact_(self, contact_name):
        self.locator.searchContact(contact_name)