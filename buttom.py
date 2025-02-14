import pygame


class Image_Buttom:
    # инициализация
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image  # по умолчанию основная картинка
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))  # получаем прямоугольник, устанавливаем верхний левый угол
        self.sound = None
        # устанавливаем звук если он есть
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)

        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)
        # данные текста
        font = pygame.font.Font("images/myttf.ttf", 40)
        text_surfase = font.render(self.text, True, (35, 45, 83))
        text_rect = text_surfase.get_rect(center=self.rect.center)
        screen.blit(text_surfase, text_rect)

# навекдена ли мышь?
    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
# проверка событьия нажатия клавиши мыши
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button = self))