import time
from WhatsAppConfig import WhatsAppConfig
whatsapp = WhatsAppConfig()
whatsapp.startBrowser()

input("Enter para fechar o navegador.")

whatsapp.closeBrowser()