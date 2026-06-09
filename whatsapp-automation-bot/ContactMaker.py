import json

class ContactMaker:
    def __init__(self, page):
        self.page = page
        self.myself = self.page.locator('div[data-testid="message-yourself-row"]')
        self.others = page.locator('div[data-testid="cell-frame-container"]').filter(has_text="Pires").first
        self.contacts = []

    def makeContactList(self):
        with open(r"whatsapp-automation-bot\\contacts_data\\contacts.json", "r", encoding="utf-8") as arquivo:
            files = json.load(arquivo)
            dict_ = None
            for file in files:
                if file["property"] == "myself":
                    dict_ = {"nome": file["nome"], "contato": lambda: self.page.locator('div[data-testid="message-yourself-row"]'), "mensagem": ""}
                    self.contacts.append(dict_)
                elif file["property"] == "other":
                    dict_ = {"nome": file["nome"], "contato": lambda nome_atual=file["nome"]: self.page.locator('div[data-testid="cell-frame-container"]').filter(has_text=nome_atual).first, "mensagem": ""}
                    self.contacts.append(dict_)
        
            return self.contacts
        