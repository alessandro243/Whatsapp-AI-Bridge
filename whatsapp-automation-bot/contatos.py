
def makeContacts(page):
    contacts_ = [
    {"nome": "Alessandro", "contato": lambda : page.locator('div[data-testid="message-yourself-row"]'), "mensagem": ""},
    {"nome": "Maninho Pukow", "contato": lambda : page.locator('div[data-testid="cell-frame-container"]').filter(has_text="Maninho Pukow"), "mensagem": ""},
    {"nome": "Guerra Mundial Z", "contato": lambda : page.locator('div[data-testid="cell-frame-container"]').filter(has_text="Guerra Mundial Z"), "mensagem": ""},
    {"nome": "Maninha", "contato": lambda : page.locator('div[data-testid="cell-frame-container"]').filter(has_text="Maninha").first, "mensagem": ""},
    {"nome": "Pires", "contato": lambda : page.locator('div[data-testid="cell-frame-container"]').filter(has_text="Pires").first, "mensagem": ""}
    ]
    return contacts_