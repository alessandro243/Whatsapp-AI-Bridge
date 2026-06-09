from WhatsAppConfig import WhatsAppConfig
from WhatsAppInterceptor import WhatsAppInterceptor

class WhatsAppBot:
    def __init__(self):
        self.text = None
        self.config = WhatsAppConfig()
        self.page = self.startBrowser_()
        self.locator = WhatsAppInterceptor(self.page)

    def makePlaceholder(self, place_holder):
        self.text = place_holder
        self.searchLabel_()

    def searchLabel_(self):
        self.locator.searchLabel(self.text)

    def startBrowser_(self):
        return self.config.startBrowser()
    
    def closeBrowser_(self):
        self.config.closeBrowser()
    
    def loopInterceptor_(self):
        self.locator.loopInterceptor()

    def searchContact_(self, contact_name):
        self.locator.searchContact(contact_name)