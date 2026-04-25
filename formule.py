import math


def beginsnelheid_m_per_s() -> float:
    while True:
        try:
            beginsnelheid_km_per_h: float = float(input("Wat is de beginsnelheid in kilometer per uur? "))
            if beginsnelheid_km_per_h < 0:
                raise ValueError
            return beginsnelheid_km_per_h * 1000 / 3600   # km/h -> m/s
        except ValueError:
            print("Beginsnelheid moet een getal groter dan 0 zijn!")


def beginhoek_radialen() -> float:
    while True:
        try:
            beginhoek_graden: float = float(input("Wat is de beginhoek in graden? "))
            if beginhoek_graden < 0:
                raise ValueError
            if beginhoek_graden > 90:
                raise ValueError
            return math.radians(beginhoek_graden)   # graden -> radialen
        except ValueError:
            print("Beginhoek met een getal tussen 0° en 90° zijn!")


def bereken_worp(beginsnelheid_m_per_s: float, beginhoek_radialen: float) -> tuple:
    gravitatieconstante = 9.81
    vliegtijd: float = 2 * beginsnelheid_m_per_s * math.sin(beginhoek_radialen) / gravitatieconstante
    vliegafstand: float = beginsnelheid_m_per_s ** 2 * math.sin(2 * beginhoek_radialen) / gravitatieconstante
    return vliegtijd, vliegafstand


def print_berekende_worp(vliegtijd: float, vliegafstand: float):
    aantal_decimalen = 2
    print(f"\nHet voorwerp landt na {round(vliegtijd, aantal_decimalen)} seconden.")
    print(f"Het voorwerp vloog {round(vliegafstand, aantal_decimalen)} meter.\n")


def main():
    # We gooien een voorwerp op Aarde (g=9.81) met een beginhoek (in 1) en beginsnelheid (in 2)
    # We we berekenen wanneer het voorwerp de grond raakt (uit 1) en hoe ver weg het vliegt (uit 2)
    vliegtijd, vliegafstand = bereken_worp(beginsnelheid_m_per_s(), beginhoek_radialen())
    print_berekende_worp(vliegtijd, vliegafstand)


main()
