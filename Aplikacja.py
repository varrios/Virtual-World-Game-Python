import pygame
import sys

class Aplikacja:
    __swiat = None
    __screen = None
    __clock = None
    __rozmiarOkna = 1400

    __logWiadomosci = []
    __buttons = []

    def __init__(self, swiat):
        self.__swiat = swiat
        pygame.init()

        self.__screen = pygame.display.set_mode([self.__rozmiarOkna, self.__rozmiarOkna - 400])
        self.__clock = pygame.time.Clock()

        self.__buttons = [
            pygame.Rect(10, self.__rozmiarOkna - 490, 100, 80),
            pygame.Rect(130, self.__rozmiarOkna - 490, 100, 80),
            pygame.Rect(250, self.__rozmiarOkna - 490, 100, 80),
            pygame.Rect(370, self.__rozmiarOkna - 490, 100, 80)
        ]


    def dodajLog(self, wiadomosc):
        self.__logWiadomosci.append(wiadomosc)

    def wyczyszLog(self):
        self.__logWiadomosci.clear()

    def run(self):
        refresh_map = False
        self.wypiszMape()
        self.wyczyszLog()
        self.dodajLog(f'Tura nr. {self.__swiat._tura} -------- Ilosc organizmow na planszy: {self.__swiat._iloscOrganizmow}')
        self.wypiszLogi()
        self.wypiszPrzyciski()
        pygame.display.flip()
        self.__clock.tick(60)
        while True:
            if refresh_map:
                self.wyczyszLog()
                self.dodajLog(f'Tura nr. {self.__swiat._tura} -------- Ilosc organizmow na planszy: {self.__swiat._iloscOrganizmow}')
                self.__swiat.wykonajTure()
                self.wypiszMape()
                self.wypiszLogi()
                self.wypiszPrzyciski()
                pygame.display.flip()
                self.__clock.tick(60)
                refresh_map = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                        refresh_map = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        for i, button_rect in enumerate(self.__buttons):
                            if button_rect.collidepoint(mouse_pos):
                                if i == 0:
                                    refresh_map = True
                                    self.dodajLog("Wcisnieto przycisk: Nastepna tura")
                                elif i == 1:
                                    self.dodajLog("Wcisnieto przycisk: Zapisz gre")
                                elif i == 2:
                                    self.dodajLog("Wcisnieto przycisk: Wczytaj gre")
                                elif i == 3:
                                    self.dodajLog("Wcisnieto przycisk: Wyjdz")

    def wypiszMape(self):
        rozmiarKomorki = 40
        self.__screen.fill((166, 160, 159))
        cell_font = pygame.font.SysFont(None, 24)

        for i in range(self.__swiat._rozmiar):
            for j in range(self.__swiat._rozmiar):
                if self.__swiat._plansza[j][i] is None:
                    kolorKomorki = (0, 0, 0)
                    letter = ''
                else:
                    kolorKomorki = self.__swiat._plansza[j][i].rysowanie()
                    letter = self.__swiat._plansza[j][i]._nazwa[0]
                pygame.draw.rect(
                    self.__screen,
                    kolorKomorki,
                    (i * rozmiarKomorki, j * rozmiarKomorki, rozmiarKomorki, rozmiarKomorki)
                )

                letter_render = cell_font.render(letter, True, (0, 0, 0))
                letter_rect = letter_render.get_rect(center=(i * rozmiarKomorki + rozmiarKomorki // 2,
                                                             j * rozmiarKomorki + rozmiarKomorki // 2))
                self.__screen.blit(letter_render, letter_rect)

    def wypiszLogi(self):
        log_rect = pygame.Rect(self.__screen.get_width() - 600, 0, 600, self.__screen.get_height())
        pygame.draw.rect(self.__screen, (166, 160, 159), log_rect)

        log_font = pygame.font.SysFont(None, 19)
        log_text_rect = log_rect.inflate(-10, -10)
        line_spacing = 15

        # Calculate the total height of all the messages
        total_height = len(self.__logWiadomosci) * (log_font.get_height() + line_spacing)

        # Calculate the maximum number of visible lines based on available space
        max_visible_lines = log_text_rect.height // (log_font.get_height() + line_spacing)

        # Calculate the starting index of the visible messages
        start_index = max(len(self.__logWiadomosci) - max_visible_lines, 0)

        for i, message in enumerate(self.__logWiadomosci[start_index:], start=start_index):
            text_render = log_font.render(message, True, (0, 0, 0))
            text_rect = text_render.get_rect()
            text_rect.topleft = (
                log_text_rect.left,
                log_text_rect.top + (i - start_index) * (text_rect.height + line_spacing)
            )
            self.__screen.blit(text_render, text_rect)

    def wypiszPrzyciski(self):
        for i, button_rect in enumerate(self.__buttons):
            pygame.draw.rect(self.__screen, (255, 255, 255), button_rect)
            button_text = f"Button {i + 1}"
            if i == 0:
                button_text = "Nastepna tura"
            if i == 1:
                button_text = "Zapisz gre"
            if i == 2:
                button_text = "Wczytaj"
            if i == 3:
                button_text = "Wyjdz"
            button_font = pygame.font.SysFont(None, 20)
            text_render = button_font.render(button_text, True, (0, 0, 0))
            text_rect = text_render.get_rect(center=button_rect.center)
            self.__screen.blit(text_render, text_rect)
