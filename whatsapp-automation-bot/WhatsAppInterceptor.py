import time
from playwright.sync_api import TimeoutError
from ContactMaker import ContactMaker

class WhatsAppInterceptor:
    def __init__(self, page):
        self.page = page
        self.search_input = None
        self.contactmaker = ContactMaker(self.page)
        self.contacts = self.contactmaker.makeContactList()

    def searchLabel(self, text):
        self.search_input = self.page.locator(text)

    def logMessages(self, nome_contato, texto, resposta):
        with open("historico_mensagens.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Contato: {nome_contato}\n")
            arquivo.write(f"Mensagem: {texto}\n")
            arquivo.write(f"Resposta: {resposta}\n")
            arquivo.write("-" * 50 + "\n")

    def loopInterceptor(self):
        #print(self.contacts[2]["contato"]().inner_text())
        while True:
            try:
                for x in self.contacts:
                    lastMessageCast = x["mensagem"]

                    contato_elemento = x["contato"]()
                    contato_elemento.scroll_into_view_if_needed()
                    contato_elemento.click()

                    lastMessage = self.page.locator('div[data-testid="msg-container"]').last
                    lastMessageText = lastMessage.inner_text().split("\n")[0]
        
                    if lastMessageText != lastMessageCast and "/gemini" in lastMessageText and lastMessageText != "/gemini":
                        resposta = "Respondendo mensagem"
                        print(f"Está visível: {lastMessageText}")
                        x["mensagem"] = lastMessageText

                        self.logMessages(x["nome"], lastMessageText, resposta)

                        barra_digitacao = self.page.locator('div[contenteditable="true"][data-tab="10"]')
                        barra_digitacao.fill(resposta)
                        barra_digitacao.press("Enter")
                        print("🚀 Respondido com sucesso!")

                    time.sleep(1)
                time.sleep(1)
                
            except TimeoutError as error:
                print(error)
                self.loopInterceptor()
