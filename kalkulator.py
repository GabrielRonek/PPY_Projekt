import math
import operacje
import historia

class Kalkulator:
    def __init__(self):
        self.historia = historia.Historia()
        self.biezaca_wartosc = 0

    def ocen(self, wyrazenie):
        try:
            wynik = eval(wyrazenie, {
            "pierwiastek": operacje.pierwiastek, "procent": operacje.procent, "silnia": operacje.silnia,
            "sin": operacje.sin, "cos": operacje.cos, "tan": operacje.tan, "cot": operacje.cot
            })
            self.biezaca_wartosc = wynik
            self.historia.dodaj(f"{wyrazenie} = {wynik}")
            return wynik
        except Exception as e:
            return f"Nieprawidłowe dane: {e}"

    def pobierz_historie(self):
        return list(self.historia.pobierz())

def main():
    kalkulator = Kalkulator()
    print("--- Kalkulator ---")
    
    while True:
        print("\nBieżąca wartość:", kalkulator.biezaca_wartosc)
        wyrazenie = input("Wprowadź wyrażenie (lub wpisz 'exit', aby zakończyć): ")
        

        if wyrazenie.lower() in ['exit']:
            break
        elif wyrazenie.lower().startswith('wybierz '):
            try:
                index = int(wyrazenie.split()[1]) - 1
                if 0 <= index < len(kalkulator.pobierz_historie()):
                    kalkulator.biezaca_wartosc = float(kalkulator.pobierz_historie()[index].split('=')[-1].strip())
                else:
                    print("Nieprawidłowy indeks historii.")
            except ValueError:
                print("Nieprawidłowe wejście. Użyj formatu 'wybierz <index>'.")
        else:
            if wyrazenie.startswith("+") or wyrazenie.startswith("-") or wyrazenie.startswith("*") or wyrazenie.startswith("/"):
                wyrazenie = str(kalkulator.biezaca_wartosc) + wyrazenie
            wynik = kalkulator.ocen(wyrazenie)
            print("Wynik:", wynik)
            print("Historia (ostatnie 5 operacji):")
            for idx, entry in enumerate(kalkulator.pobierz_historie(), start=1):
                print(f"{idx}: {entry}")

if __name__ == "__main__":
    main()