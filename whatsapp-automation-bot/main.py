from WhatsAppBot import WhatsAppBot

whatsapp = WhatsAppBot()
whatsapp.makePlaceholder('[aria-label*="mensagem não lida"]')
whatsapp.loopInterceptor_()  
#whatsapp.searchContact_("Maninha")

input("\nVeja se o nome foi digitado! Aperte ENTER para fechar o navegador...")
whatsapp.closeBrowser_()