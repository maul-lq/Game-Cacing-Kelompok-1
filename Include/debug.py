import pygame

pygame.init()

def debug(info, y:int=5, x:int=5, fontSize:int=20, warna: str='black'):
    font = pygame.font.Font(None, fontSize)
    display_surf = pygame.display.get_surface()
    debug_surf = font.render(str(info),True,warna)
    debug_rect = debug_surf.get_rect(topleft=(x,y))
    
    display_surf.blit(debug_surf,debug_rect)
    pass