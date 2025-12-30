class Termometr:
    def __init__(self, harorat):
        self.harorat = harorat

    def tekshir(self):
        if self.harorat < 0:
            print("❄️ Juda sovuq")
        elif self.harorat > 30:
            print("🔥 Juda issiq")
        else:
            print("🌤 Normal harorat")


t = Termometr(25)
t.tekshir()
