class Historia:
    def __init__(self, max_dlugosc=5):
        self.max_dlugosc = max_dlugosc
        self.historia_operacji = []

    def dodaj(self, wpis_historii):
        self.historia_operacji.append(wpis_historii)
        if len(self.historia_operacji) > self.max_dlugosc:
            self.historia_operacji.pop(0)

    def pobierz(self):
        return self.historia_operacji