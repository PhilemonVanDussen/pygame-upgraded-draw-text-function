# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game():
    pygame.init()
    pygame.font.init
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def draw_text(screen, text, font_size, font_name, color, position, italic=False, bold=False):
    if font_name:
        font = pygame.font.Font(font_name, font_size)
    else:
        font = pygame.font.Font(None, font_size)
    
    font.set_bold(bold)
    font.set_italic(italic)

    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (position))


def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initalize the clock here

    font_name = "c:\Font\EmblemaOne-Regular.ttf"
    font_name2 = "c:\Font\PlaywriteHU-VariableFont_wght.ttf"
    font_name3 = "c:\Font\BigShouldersInline-VariableFont_opsz,wght.ttf"
    font_color = config.PINK
    font_color2 = config.ORANGE
    font_color3 = config.PURPLE

    text_pos = [200, 100]
    text_pos2 = [50, 230]
    text_pos3 = [250, 400]

    
    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
        draw_text(screen, 'PJ VanDssen!', 50, font_name, font_color, text_pos, bold=True)
        draw_text(screen, 'Web and App Devolpment PM!!', 40, font_name2, font_color2, text_pos2, italic=True )
        draw_text(screen, 'Career Tech!', 100, font_name3, font_color3, text_pos3, bold=True, italic=True)
        
        

        pygame.display.flip()

        # Limit the frame rate to the specified frames per second
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



