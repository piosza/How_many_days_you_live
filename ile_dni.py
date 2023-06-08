from datetime import date


def oblicz_liczbe_dni(od_roku, od_miesiaca, od_dnia):
    dzis = date.today()
    data_urodzenia = date(od_roku, od_miesiaca, od_dnia)
    roznica = dzis - data_urodzenia
    liczba_dni = roznica.days
    return liczba_dni


# Podaj datę urodzenia
rok = int(input("Podaj rok urodzenia: "))
miesiac = int(input("Podaj miesiąc urodzenia: "))
dzien = int(input("Podaj dzień urodzenia: "))

# Oblicz liczbę dni
liczba_dni_zycia = oblicz_liczbe_dni(rok, miesiac, dzien)
print("Żyjesz na świecie od urodzenia już", liczba_dni_zycia, "dni.")
