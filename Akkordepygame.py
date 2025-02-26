import pygame, time

pygame.init()

win_width = 600
win_height = 400
win = pygame.display.set_mode((win_width,win_height))
clock = pygame.time.Clock()

#Noten Class
class Noten:
    def __init__(self, x:int, y:int, height:int, width:int, note:str, pos:int):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.note = note
        self.pos = pos
        self.rect = (self.x, self.y, self.width, self.height)
        self.color = (87,55,71)
        self.noten_textfont = pygame.font.SysFont("Arial", 20, True)
        self.noten_text, self.noten_text_rect = create_text(self.noten_textfont, self.note, (self.x+self.width/2), (self.y+self.height/2), (240,240,240),True)
    
    #draws recktangle with note name
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        win.blit(self.noten_text, self.noten_text_rect)
    
    def button_hit(self, mousepos_y, mousepos_x,mousebutton):
        if (mousepos_y > self.y and mousepos_y < self.y+self.height) and (
            mousepos_x > self.x and mousepos_x < self.x+self.width) and mousebutton:
            return True

class Akkord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gr_terz = 4
        self.quinte = 7
        self.akkord = ""
        self.akkord_textfont = pygame.font.SysFont("Arial", 50, True)
        self.akkord_text, self.akkord_text_rect = create_text(self.akkord_textfont, f"Akkord: ", self.x, self.y, (240,240,240), False)

    def draw(self, win):
        win.blit(self.akkord_text, self.akkord_text_rect)

    def create_akkord(self,note,notenpos):
        gr_terz_pos = notenpos+self.gr_terz
        quinte_pos = notenpos+self.quinte

        if gr_terz_pos >= list_len:
            gr_terz_pos = gr_terz_pos-list_len
            quinte_pos = quinte_pos-list_len
        elif quinte_pos >= list_len:
            quinte_pos = quinte_pos-list_len

        self.akkord = f"{note} {tonleiter[gr_terz_pos].note} {tonleiter[quinte_pos].note}"

        self.akkord_text, self.accord_text_rect = create_text(self.akkord_textfont, f"Akkord: {self.akkord}", self.x, self.y, (240,240,240), False)



#redraw loop
def redrawWindow():
    win.fill((20,44,22))
    draw_squares()
    akkord_output.draw(win)
    pygame.display.update()

#initilize List with Noten-objects
def initilize_list():
    x = 60
    y = 50
    tonleiter_note = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
    for i,j in enumerate(tonleiter_note):
        if i == 6:
            x = 60
            y = 130
        tonleiter.append(Noten(x,y,75,75,j,i))
        x += 80

#function to draw all squares
def draw_squares():
    for note in tonleiter:
        note.draw(win)

#create args for blit()
def create_text(font, text:str, x:int, y:int, color:tuple[int,int,int],centered:bool):
    render_text = font.render(text,1,color)
    if centered:
        render_text_rect = render_text.get_rect(center=(x, y))
    else:
        render_text_rect = (x, y)
    return render_text, render_text_rect


tonleiter =  []
initilize_list()
list_len = len(tonleiter)
akkord_output = Akkord(60,275)

#gameloop
run = True
while run:
    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_rightclick = pygame.mouse.get_pressed()[0]
    mouse_pos = pygame.mouse.get_pos()

    for note in tonleiter:
        if note.button_hit(mouse_pos[1],mouse_pos[0],mouse_rightclick):
            akkord_output.create_akkord(note.note, note.pos)
            print(note.note)



            time.sleep(0.08)




    redrawWindow()

pygame.quit()
