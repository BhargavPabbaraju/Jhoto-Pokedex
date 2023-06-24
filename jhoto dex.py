import pygame as pg

colors={
'primary':[(219,97,56),(146,64,42)],
'secondary':[(84,80,77)],
'gray':[(214,214,214)],
'white':[(248,248,248),(163,164,164)],
'red':[(255,0,41),(157,0,27),(255,141,159)],
'green':[(85,142,54)],
'black':[(35,35,35),(0,49,43)],

}

SIZE = 64

box_sizes = [[6,6],[6,2]]

WIDTH = 800
HEIGHT = 800
pg.init()
window = pg.display.set_mode((WIDTH,HEIGHT),pg.SRCALPHA)





def draw_circle(radius,color,width=0,draw_top_right=True,draw_top_left=True,
                draw_bottom_left=True,draw_bottom_right=True):
    surf = pg.Surface((radius*2,radius*2),pg.SRCALPHA)
    pg.draw.circle(surf,color,(radius,radius),radius,width=width,draw_top_right=draw_top_right,draw_top_left=draw_top_left,
                   draw_bottom_left=draw_bottom_left,draw_bottom_right=draw_bottom_right)
    return surf




class TopBox:
    def __init__(self,window,X,Y,size,color,top=True):
        self.x = X
        self.y = Y
        self.size = size
        self.window = window
        self.color = color
        self.top = top
    
    def draw_border(self):

        if self.top:
            tl=16
            tr=16
     
        else:
            tl=0
            tr=0
        

        #primary bg
        pg.draw.rect(self.window,self.color[0],[self.x,self.y,SIZE*self.size[0],SIZE*self.size[1]],border_top_left_radius=tl,border_top_right_radius=tr)
        pg.draw.rect(self.window,(0,0,0),[self.x,self.y,SIZE*self.size[0],SIZE*self.size[1]],width=2,border_top_left_radius=tl,border_top_right_radius=tr)

        #secondary half bg
        pg.draw.rect(self.window,colors['secondary'][0],[self.x+SIZE,self.y,SIZE*(self.size[0]-2),SIZE*self.size[1]])
        pg.draw.rect(self.window,(0,0,0),[self.x+SIZE,self.y,SIZE*(self.size[0]-2),SIZE*self.size[1]],width=2)


    def draw_inner(self):
        #white display bg
        pg.draw.rect(self.window,colors['white'][0],[self.x+SIZE//2,self.y+SIZE//2,SIZE*(self.size[0]-1),SIZE*(self.size[1]-1)],border_radius=16)
        pg.draw.rect(self.window,(0,0,0),[self.x+SIZE//2,self.y+SIZE//2,SIZE*(self.size[0]-1),SIZE*(self.size[1]-1)],width=2,border_radius=16)

        if not self.top:
            return
        #green dots
        x= self.x+SIZE*2 - 16
        y= self.y+SIZE*(self.size[1]) - 16 -1
        gap = SIZE*2 + 16 + 8
        for i in range(2):
            circle = draw_circle(12,colors['green'][0])
            self.window.blit(circle,circle.get_rect(center=(x+gap*i,y)))
            circle = draw_circle(12,(0,0,0),width=2)
            self.window.blit(circle,circle.get_rect(center=(x+gap*i,y)))

    def draw_upper_circle(self):
        
        x= (2*self.x + self.size[0]*SIZE)//2
        y= self.y
        circle = draw_circle(SIZE,colors['secondary'][0])
        self.window.blit(circle,circle.get_rect(center=(x,y)))
        circle = draw_circle(SIZE,(0,0,0),width=2)
        self.window.blit(circle,circle.get_rect(center=(x,y)))

        circle = draw_circle(SIZE-16-8,colors['gray'][0])
        self.window.blit(circle,circle.get_rect(center=(x,y)))
        circle = draw_circle(SIZE-16-8,(0,0,0),width=2)
        self.window.blit(circle,circle.get_rect(center=(x,y)))
    

    def draw_rod(self):
        pg.draw.rect(self.window,colors['primary'][0],[self.x,self.y+SIZE*self.size[1],SIZE*self.size[0],32],border_radius=16)
        pg.draw.rect(self.window,(0,0,0),[self.x,self.y+SIZE*self.size[1],SIZE*self.size[0],32],width=2,border_radius=16)
        pg.draw.rect(self.window,(0,0,0),[self.x+SIZE,self.y+SIZE*self.size[1],SIZE*(self.size[0]-2),32],width=2,border_radius=16)


    def draw(self):
        if self.top:
            self.draw_upper_circle()


        self.draw_border()

        self.draw_inner()

        if self.top:
            self.draw_rod()
        
        
class BottomBox:
    def __init__(self,window,x,y,size):
        self.window = window
        self.x = x
        self.y = y
        self.size = size
    

    def draw_box(self):
        pg.draw.rect(self.window,colors['primary'][0],[self.x,self.y,SIZE*self.size[0],SIZE*self.size[1]],border_bottom_left_radius=16,border_bottom_right_radius=16)
        pg.draw.rect(self.window,(0,0,0),[self.x,self.y,SIZE*self.size[0],SIZE*self.size[1]],width=2,border_bottom_left_radius=16,border_bottom_right_radius=16)
    
    def draw_circles(self):
        x= (2*self.x + self.size[0]*SIZE)//2
        y= self.y - 16
        circle = draw_circle(SIZE,(0,0,0),width=2)
        self.window.blit(circle,circle.get_rect(center=(x,y)))

        circle = draw_circle(SIZE+32,(0,0,0),width=2)
        self.window.blit(circle,circle.get_rect(center=(x,y)))

        circle = draw_circle(SIZE+32+6,colors['primary'][1],width=6)
        self.window.blit(circle,circle.get_rect(center=(x,y)))

        circle = draw_circle(SIZE+32+6+2,(0,0,0),width=2)
        self.window.blit(circle,circle.get_rect(center=(x,y)))

    def draw(self):
        self.draw_box()

        self.draw_circles()


def draw():
    window.fill(-1)
    X=200
    Y=-200

    color = colors['primary']
    tb = TopBox(window,X,Y,box_sizes[0],color)
    tb.draw()

    bt = BottomBox(window,X,Y+box_sizes[0][1]*2*SIZE+30-4,box_sizes[1])
    bt.draw()

    tb = TopBox(window,X,Y+box_sizes[0][1]*SIZE+32,box_sizes[0],color,top=False)
    tb.draw()

    

    
def loop():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.image.save(window,'image.png')
                pg.quit()
                return


        draw()
        pg.display.flip()


loop()
    
