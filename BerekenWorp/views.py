import math

from django.shortcuts import render

# Create your views here.
def bereken_worp(request):
    context: dict = {}
    error: str = ""
    result: str = ""

    if request.method == "POST":

        def beginsnelheid_m_per_s() -> float | None:
            nonlocal error
            try:
                beginsnelheid_km_per_h: float = float(request.POST.get('beginsnelheid_km_per_h'))
                if beginsnelheid_km_per_h < 0:
                    raise ValueError
                return beginsnelheid_km_per_h * 1000 / 3600   # km/h -> m/s
            except ValueError:
                nonlocal error
                error += "Beginsnelheid moet een getal groter dan 0 zijn!<br>"
            except TypeError:
                error += "Veld 'Beginsnelheid (km/h)' is verplicht!<br>"

        def beginhoek_radialen() -> float | None:
            nonlocal error
            try:
                beginhoek_graden: float = float(request.POST.get('beginhoek_graden'))
                if beginhoek_graden < 0:
                    raise ValueError
                if beginhoek_graden > 90:
                    raise ValueError
                return math.radians(beginhoek_graden)   # graden -> radialen
            except ValueError:
                error += "Beginhoek met een getal tussen 0° en 90° zijn!<br>"
            except TypeError:
                error += "Veld 'Beginhoek (graden)' is verplicht!<br>"

        def bereken_worp(beginsnelheid_m_per_s: float, beginhoek_radialen: float) -> tuple:
            gravitatieconstante = 9.81
            vliegtijd: float = 2 * beginsnelheid_m_per_s * math.sin(beginhoek_radialen) / gravitatieconstante
            vliegafstand: float = beginsnelheid_m_per_s ** 2 * math.sin(2 * beginhoek_radialen) / gravitatieconstante
            return vliegtijd, vliegafstand

        def print_berekende_worp(vliegtijd: float, vliegafstand: float):
            nonlocal result
            aantal_decimalen = 2
            result += f"Het voorwerp landt na {round(vliegtijd, aantal_decimalen)} seconden.<br>"
            result += f"Het voorwerp vloog {round(vliegafstand, aantal_decimalen)} meter.<br>"

        # We gooien een voorwerp op Aarde (g=9.81) met een beginhoek (in 1) en beginsnelheid (in 2)
        # We we berekenen wanneer het voorwerp de grond raakt (uit 1) en hoe ver weg het vliegt (uit 2)
        beginsnelheid_m_per_s = beginsnelheid_m_per_s()
        beginhoek_radialen = beginhoek_radialen()
        if beginsnelheid_m_per_s and beginhoek_radialen:
            vliegtijd, vliegafstand = bereken_worp(beginsnelheid_m_per_s, beginhoek_radialen)
            print_berekende_worp(vliegtijd, vliegafstand)

        context['result'] = result
        context['error'] = error

    return render(request, 'BerekenWorp.html', context)
