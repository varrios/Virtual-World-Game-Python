from Czlowiek import Czlowiek
from Swiat import *
from Aplikacja import *

if __name__ == '__main__':
    swiat = Swiat()
    czlowiek = Czlowiek(swiat, 0,0)
    swiat._czlowiek = czlowiek
    swiat.dodajOrganizm(czlowiek)
    aplikacja = Aplikacja(swiat)
    swiat._aplikacja = aplikacja
    aplikacja.dodajLog("Logi:")
    aplikacja.run()

