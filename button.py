import pygame



class button:
    text = "Button Text"
    color = (150,150,150)
    text_color = (0,0,0)
    x = 0
    y = 0
    w = 10
    h = 10
    hidden = False
    hover = False
    

    def __init__(self, gs, text,x,y,w,h,color,text_color):
        self.color = color
        self.text = text
        self.x = x
        self.y = y
        self.h = h 
        self.w = w
        self.text_color = text_color
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.gs = gs

    def draw(self):
        if self.hidden:
            return
        if self.hover:
            temp_color = (min(self.color[0]+50, 255),min(self.color[1]+50, 255),min(self.color[2]+50, 255))
           
            pygame.draw.rect(self.gs.surface,temp_color, self.rect)
        else:
            pygame.draw.rect(self.gs.surface, self.color, self.rect)
        
        
        text_obj = self.gs.font.render(self.text, 1, self.text_color)
        text_rect = text_obj.get_rect()
        text_rect.center = ((self.x+self.w/2), (self.y+self.h/2))
        self.gs.surface.blit(text_obj, text_rect)

