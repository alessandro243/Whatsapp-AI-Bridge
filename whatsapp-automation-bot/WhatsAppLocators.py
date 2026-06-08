class WhatsAppLocators:
    def __init__(self, page):
        self.page = page
        self.searchBarText = "Pesquisar ou começar uma nova conversa"
        self.search_input = self.searchSearchBar()

    def searchSearchBar(self):
        return self.page.get_by_placeholder(self.searchBarText)

    def searchElementByState(self, state):
        state_ = state
        self.search_input.wait_for(state=state_, timeout=45000)

    def searchContact(self, contact_name):
        self.search_input.fill(contact_name)