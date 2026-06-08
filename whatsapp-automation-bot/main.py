from WhatsAppBot import WhatsAppBot

whatsapp = WhatsAppBot()
whatsapp.searchElementByState_("visible")    
whatsapp.searchContact_("Maninha")

input("\nVeja se o nome foi digitado! Aperte ENTER para fechar o navegador...")
whatsapp.closeBrowser_()