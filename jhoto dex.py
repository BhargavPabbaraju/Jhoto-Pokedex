import pygame as pg

colors={
'primary':[(219,97,56),(146,64,42)],
'secondary':[(84,80,77)],
'gray':[(214,214,214)],
'pencil':[(245,193,80),(115,93,57)],
'red':[(232,48,48),(248,152,160)],
'green':[(85,142,54)],
'white':[(248,248,248),(168,168,168),(88,88,88)],

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
    

    def draw_pencils(self):
        x=self.x - 16
        gap = self.size[0]*SIZE+16
        tl= 12
        bl = 12
        tr = 0
        br = 0
        for i in range(2):
            if i==1:
                tl= 0
                bl = 0
                tr = 12
                br = 12
            #whole pencil
            pg.draw.rect(self.window,colors['pencil'][0],[x+gap*i,self.y - SIZE * 5,16,SIZE*6],border_top_left_radius=tl,border_bottom_left_radius=bl,border_top_right_radius=tr,border_bottom_right_radius=br)
            pg.draw.rect(self.window,(0,0,0),[x+gap*i,self.y - SIZE * 5,16,SIZE*6],width=2,border_top_left_radius=tl,border_bottom_left_radius=bl,border_top_right_radius=tr,border_bottom_right_radius=br)
            #groove 1
            pg.draw.rect(self.window,colors['pencil'][1],[x+gap*i,self.y-SIZE*5+32,16,10],border_top_left_radius=tl,border_bottom_left_radius=bl,border_top_right_radius=tr,border_bottom_right_radius=br)
            pg.draw.rect(self.window,(0,0,0),[x+gap*i,self.y-SIZE*5+32,16,10],width=2,border_top_left_radius=tl,border_bottom_left_radius=bl,border_top_right_radius=tr,border_bottom_right_radius=br)
            
            #groove 2
            pg.draw.rect(self.window,colors['pencil'][1],[x+gap*i,self.y-SIZE*3,16,10],border_top_left_radius=tl,border_bottom_left_radius=bl,border_top_right_radius=tr,border_bottom_right_radius=br)
            pg.draw.rect(self.window,(0,0,0),[x+gap*i,self.y-SIZE*3,16,10],width=2,border_top_left_radius=tl,border_bottom_left_radius=bl,border_top_right_radius=tr,border_bottom_right_radius=br)
            #groove 3
            pg.draw.rect(self.window,colors['pencil'][1],[x+gap*i,self.y-SIZE*3-32,16,10],border_top_left_radius=tl,border_bottom_left_radius=bl,border_top_right_radius=tr,border_bottom_right_radius=br)
            pg.draw.rect(self.window,(0,0,0),[x+gap*i,self.y-SIZE*3-32,16,10],width=2,border_top_left_radius=tl,border_bottom_left_radius=bl,border_top_right_radius=tr,border_bottom_right_radius=br)

    def draw(self):
        self.draw_box()

        self.draw_circles()


class TopInner:
    def __init__(self,window,x,y,size):
        self.window = window
        self.x = x
        self.y = y
        self.size = size
    

    def draw_topbar(self):
        #red bar
        pg.draw.rect(self.window,colors['red'][0],[self.x,self.y,self.size[0]*SIZE,32],border_top_left_radius=16,border_top_right_radius=16)
        pg.draw.rect(self.window,(0,0,0),[self.x,self.y,self.size[0]*SIZE,32],width=2,border_top_left_radius=16,border_top_right_radius=16)

        #triangl
        points=[(self.x+16-4,self.y+8),(self.x+16*2+4,self.y+8),(self.x+8+16,self.y+16+8)]
        pg.draw.polygon(self.window,colors['white'][0],points)
        pg.draw.polygon(self.window,colors['white'][1],points,width=2)
    

    def draw_name_bar(self):
        x=self.x+SIZE*2
        y=self.y+SIZE-16

        #red half bar
        pg.draw.rect(self.window,colors['red'][0],[x,y,3*SIZE-16,32],border_top_left_radius=4,border_top_right_radius=4)
        pg.draw.rect(self.window,colors['white'][2],[x,y,3*SIZE-16,32],width=2,border_top_left_radius=4,border_top_right_radius=4)
        
        #white half bar
        pg.draw.rect(self.window,colors['white'][0],[x,y+32,3*SIZE-16,32],border_bottom_left_radius=4,border_bottom_right_radius=4)
        pg.draw.rect(self.window,colors['white'][2],[x,y+32,3*SIZE-16,32],width=2,border_bottom_left_radius=4,border_bottom_right_radius=4)
        
        #red in between
        pg.draw.rect(self.window,colors['red'][1],[x+2,y+32-2,3*SIZE-16-4,4])
        
    def draw_pokeball(self):
        #white bg circle
        x= self.x+SIZE*2 + 16
        y= self.y+SIZE-16 + 16
        circle = draw_circle(14,colors['white'][0])
        self.window.blit(circle,circle.get_rect(center=(x,y)))
        circle = draw_circle(12,colors['white'][2])
        self.window.blit(circle,circle.get_rect(center=(x,y)))

        #red half circle
        circle = draw_circle(10,colors['red'][0],draw_bottom_left=False,draw_bottom_right=False)
        self.window.blit(circle,circle.get_rect(center=(x,y)))

        #white half circle
        circle = draw_circle(10,colors['white'][0],draw_top_left=False,draw_top_right=False)
        self.window.blit(circle,circle.get_rect(center=(x,y)))

        #grey bar in between
        pg.draw.rect(self.window,colors['white'][2],[x-10,y-1,20,2])

        circle = draw_circle(4,colors['white'][0])
        self.window.blit(circle,circle.get_rect(center=(x,y)))
        circle = draw_circle(4,colors['white'][2],width=2)
        self.window.blit(circle,circle.get_rect(center=(x,y)))
        

    def draw_grid(self):
        x = self.x + SIZE
        while x< self.x + SIZE*self.size[0]:
            pg.draw.line(self.window,colors['white'][1],(x,self.y),(x,self.y+SIZE*self.size[1]-5))
            x+=SIZE

        y = self.y + SIZE
        while y< self.y + SIZE*self.size[1]:
            pg.draw.line(self.window,colors['white'][1],(self.x+2,y),(self.x+SIZE*self.size[0]-3,y))
            y+=SIZE

    
    def draw(self):

        self.draw_grid()
        
        self.draw_topbar()

        self.draw_name_bar()

        self.draw_pokeball()

def draw():
    window.fill(-1)
    X=200
    Y=50

    color = colors['primary']
    tb = TopBox(window,X,Y,box_sizes[0],color)
    tb.draw()

    ti = TopInner(window,tb.x+SIZE//2,tb.y+SIZE//2 +2,[tb.size[0]-1,tb.size[1]-1])
    ti.draw()

    bt = BottomBox(window,X,Y+box_sizes[0][1]*2*SIZE+30-4,box_sizes[1])
    bt.draw()

    tb = TopBox(window,X,Y+box_sizes[0][1]*SIZE+32,box_sizes[0],color,top=False)
    tb.draw()

    bt.draw_pencils()  


    
    

    
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
    
