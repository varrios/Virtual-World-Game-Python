from Swiat import *
from Aplikacja import *

if __name__ == '__main__':
    swiat = Swiat()
    aplikacja = Aplikacja(swiat)
    swiat._aplikacja = aplikacja
    aplikacja.dodajLog("Logi:")
    aplikacja.run()

