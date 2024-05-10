from tkinter import *
import random
root = Tk()

pos = [1, 2]

class Square:
    def __init__(self, type, position, canvas: Canvas):
        self.type = "P"
        self.position = [0, 0]
        self.canvas = canvas

        self.items = []
    def display(self):
        self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="white")

class Forest(Square):
    def __init__(self, position, canvas: Canvas):
        self.canvas = canvas
        self.items = []
        num_trees = 80 # DONT GO ABOVE 150, ITS BAD
        for _ in range(num_trees):
            x = random.randint(0, 599)  # Random x position in 20x20 grid
            y = random.randint(0, 599)  # Random y position in 20x20 grid
            position = [x, y]
            self.items.append(position)
    def display(self):
        self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
        for item in self.items:
            # Coordinates for the trunk (brown) and leaves (dark green)
            trunk_width = 8
            trunk_height = 12
            leaf_size = 20
            
            # Trunk at the bottom of the cell
            trunk_x1 = item[0] * 1 + (1 - trunk_width) / 2
            trunk_y1 = item[1] * 1 + 1 - trunk_height
            trunk_x2 = trunk_x1 + trunk_width
            trunk_y2 = trunk_y1 + trunk_height

            # Leaves above the trunk
            leaf_center_x = item[0] * 1 + 1 / 2
            leaf_center_y = trunk_y1 - 2  # Leaves start just above the trunk

            # Draw trunk (brown)
            self.canvas.create_rectangle(trunk_x1, trunk_y1, trunk_x2, trunk_y2, fill="saddlebrown")

            # Draw leaves (dark green) as a circle
            self.canvas.create_oval(leaf_center_x - leaf_size / 2, 
                            leaf_center_y - leaf_size / 2, 
                            leaf_center_x + leaf_size / 2, 
                            leaf_center_y + leaf_size / 2, 
                            fill="darkgreen")
            
class River(Square):
    def __init__(self, position, canvas: Canvas, grid: list, grid_xpos: int, grid_ypos: int):
        self.canvas = canvas
        self.items = []
        self.type = "dot"
        self.width = 100

        river_right = False
        river_left = False
        river_top = False
        river_bottom = False

        #determine surronding rivers
        try:
            if grid[grid_ypos][grid_xpos+1] == "R":
                river_right = True
        except:
            pass
        try:
            if not grid_xpos == 0:
                if grid[grid_ypos][grid_xpos-1] == "R":
                    river_left = True
        except:
            pass
        try:
            if grid[grid_ypos+1][grid_xpos] == "R":
                river_bottom = True
        except:
            pass
        try:
            if not grid_ypos == 0:
                if grid[grid_ypos-1][grid_xpos] == "R":
                    river_top = True
        except:
            pass

        if river_right and not river_left and not river_top and not river_bottom:
            self.type = "right"
        if river_left and not river_right and not river_top and not river_bottom:
            self.type = "left"
        if river_top and not river_right and not river_left and not river_bottom:
            self.type = "top"
        if river_bottom and not river_right and not river_left and not river_top:
            self.type = "bottom"
        if river_right and river_left and not river_top and not river_bottom:
            self.type = "horizontal"
        if river_top and river_bottom and not river_right and not river_left:
            self.type = "vertical"
        if river_right and river_bottom and not river_left and not river_top:
            self.type = "bottom_right"
        if river_right and river_top and not river_left and not river_bottom:
            self.type = "top_right"
        if river_left and river_bottom and not river_right and not river_top:
            self.type = "bottom_left"
        if river_left and river_top and not river_right and not river_bottom:
            self.type = "top_left"
        if river_right and river_left and river_top and not river_bottom:
            self.type = "top_horizontal"
        if river_right and river_left and river_bottom and not river_top:
            self.type = "bottom_horizontal"
        if river_top and river_bottom and river_right and not river_left:
            self.type = "right_vertical"
        if river_top and river_bottom and river_left and not river_right:
            self.type = "left_vertical"
        if river_top and river_bottom and river_left and river_right:
            self.type = "cross"
        
        print(self.type)

    def display(self):
        match self.type:
            case "right":
                self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2, self.canvas.winfo_reqheight()/2 - self.width, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()/2 + self.width, fill="blue", outline="blue")
                return
            case "left":
                self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2, self.canvas.winfo_reqheight()/2 - self.width, 0, self.canvas.winfo_reqheight()/2 + self.width, fill="blue", outline="blue")
                return
            case "top":
                self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2-self.width, self.canvas.winfo_reqheight()/2, self.canvas.winfo_reqwidth()/2+self.width, 0, fill="blue", outline="blue")
                return
            case "bottom":
                self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2-self.width, self.canvas.winfo_reqheight()/2, self.canvas.winfo_reqwidth()/2+self.width, self.canvas.winfo_reqheight(), fill="blue", outline="blue")
                return
            case "dot":
                self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
                self.canvas.create_oval(self.canvas.winfo_reqwidth()/2-(self.width*2), self.canvas.winfo_reqheight()/2-(self.width*2), self.canvas.winfo_reqwidth()/2+(self.width*2), self.canvas.winfo_reqheight()/2+(self.width*2), fill="blue", outline="blue")
                return
            case "horizontal":
                self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
                self.canvas.create_rectangle(0, self.canvas.winfo_reqheight()/2-(self.width), self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()/2+(self.width), fill="blue", outline="blue")
                return
            case "verticle":
                self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2-self.width, self.canvas.winfo_reqheight(), self.canvas.winfo_reqwidth()/2+self.width, 0, fill="blue", outline="blue")
                return
            case "bottom_right":
                self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2, self.canvas.winfo_reqheight()/2 - self.width, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()/2 + self.width, fill="blue", outline="blue")
                self.canvas.create_rectangle(self.canvas.winfo_width()/2-self.width, self.canvas.winfo_height(), self.canvas.winfo_width()/2+self.width, self.canvas.winfo_height()/2-self.width, fill="blue", outline="blue")
                return
            case "top_right":
                self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2, self.canvas.winfo_reqheight()/2 - self.width, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()/2 + self.width, fill="blue", outline="blue")
                self.canvas.create_rectangle(self.canvas.winfo_width()/2-self.width, 0, self.canvas.winfo_width()/2+self.width, self.canvas.winfo_height()/2+self.width, fill="blue", outline="blue")
                return
            case "cross":
                self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2-self.width, self.canvas.winfo_reqheight(), self.canvas.winfo_reqwidth()/2+self.width, 0, fill="blue", outline="blue")
                self.canvas.create_rectangle(0, self.canvas.winfo_reqheight()/2-(self.width), self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()/2+(self.width), fill="blue", outline="blue")
                print("loaded cross")
                return
            case "left_vertical":
                self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2-self.width, self.canvas.winfo_reqheight(), self.canvas.winfo_reqwidth()/2+self.width, 0, fill="blue", outline="blue")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2, self.canvas.winfo_reqheight()/2 - self.width, 0, self.canvas.winfo_reqheight()/2 + self.width, fill="blue", outline="blue")
                print("left-verticle")
                return
            case "top_horizontal":
                self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
                self.canvas.create_rectangle(0, self.canvas.winfo_reqheight()/2-(self.width), self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()/2+(self.width), fill="blue", outline="blue")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2-self.width, self.canvas.winfo_reqheight()/2, self.canvas.winfo_reqwidth()/2+self.width, 0, fill="blue", outline="blue")
                return
            case "top_left":
                self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2-self.width, self.canvas.winfo_reqheight()/2+self.width, self.canvas.winfo_reqwidth()/2+self.width, 0, fill="blue", outline="blue")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2, self.canvas.winfo_reqheight()/2 - self.width, 0, self.canvas.winfo_reqheight()/2 + self.width, fill="blue", outline="blue")
                return
            case "bottom_left":
                self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2, self.canvas.winfo_reqheight()/2 - self.width, 0, self.canvas.winfo_reqheight()/2 + self.width, fill="blue", outline="blue")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2-self.width, self.canvas.winfo_reqheight()/2-self.width, self.canvas.winfo_reqwidth()/2+self.width, self.canvas.winfo_reqheight(), fill="blue", outline="blue")
                return
            case "right_vertical":
                self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2-self.width, self.canvas.winfo_reqheight(), self.canvas.winfo_reqwidth()/2+self.width, 0, fill="blue", outline="blue")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2, self.canvas.winfo_reqheight()/2 - self.width, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()/2 + self.width, fill="blue", outline="blue")
                print("right-verticle")
                return
            case "bottom_horizontal":
                self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")
                self.canvas.create_rectangle(0, self.canvas.winfo_reqheight()/2-(self.width), self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()/2+(self.width), fill="blue", outline="blue")
                self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2-self.width, self.canvas.winfo_reqheight()/2, self.canvas.winfo_reqwidth()/2+self.width, self.canvas.winfo_reqheight(), fill="blue", outline="blue")
                return

        self.canvas.create_rectangle(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill="green")

class Mountain(Square):
    def __init__(self):
        

def createTriangle(object: Canvas):
    numTriangles = random.randint(3, 20)
    for i in range(numTriangles):
        bottom = object.winfo_reqheight() - 100
        width = random.randrange(0, int(object.winfo_reqwidth()/2), 50)
        xPos = random.randint(int(width/2), object.winfo_reqwidth()-int(width/2))
        height = random.randint(0, object.winfo_reqheight()-int(object.winfo_reqheight()/5)-100)
        object.create_polygon(xPos, bottom - height, xPos-(width/2), bottom, xPos+(width/2), bottom, fill="darkgrey")


def create_grid(object: Canvas, size: int, grid: list, pos: list):
    padding = 20

    #Background
    object.create_rectangle(object.winfo_reqwidth() - size-20, object.winfo_reqheight()-size - 20, object.winfo_reqwidth()-20, object.winfo_reqheight()-20, fill="lightgrey", outline="black", width=3)

    #Grid Lines
    line_spacing = size/3
    object.create_line(object.winfo_reqwidth() - line_spacing-20, object.winfo_reqheight()-20, object.winfo_reqwidth()-line_spacing-20, object.winfo_reqheight()-size-20)
    object.create_line(object.winfo_reqwidth() - (line_spacing * 2)-20, object.winfo_reqheight()-20, object.winfo_reqwidth()-(line_spacing*2)-20, object.winfo_reqheight()-size-20)
    object.create_line(object.winfo_reqwidth() - size-20, object.winfo_reqheight()-line_spacing-20, object.winfo_reqwidth()-20, object.winfo_reqheight()-line_spacing-20)
    object.create_line(object.winfo_reqwidth() - size-20, object.winfo_reqheight()-(line_spacing*2)-20, object.winfo_reqwidth()-20, object.winfo_reqheight()-(line_spacing*2)-20)

    #Green Box
    object.create_rectangle(object.winfo_reqwidth()-size+(line_spacing*pos[0])-(line_spacing/2), object.winfo_reqheight()-size+(line_spacing*pos[1])-(line_spacing/2), object.winfo_reqwidth()-size+(line_spacing*(pos[0]+1))-(line_spacing/2), object.winfo_reqheight()-size+(line_spacing*(pos[1]+1))-(line_spacing/2), width=3)

    #text
    object.create_text(object.winfo_reqwidth()-size+(line_spacing/2)-20, object.winfo_reqheight()-size+(line_spacing/2)-20, text=grid[0][0], font=("Arial", 20))
    object.create_text(object.winfo_reqwidth()-(line_spacing*2)+(line_spacing/2)-20, object.winfo_reqheight()-size+(line_spacing/2)-20, text=grid[0][1], font=("Arial", 20))
    object.create_text(object.winfo_reqwidth()-(line_spacing)+(line_spacing/2)-20, object.winfo_reqheight()-size+(line_spacing/2)-20, text=grid[0][2], font=("Arial", 20))

    object.create_text(object.winfo_reqwidth()-size+(line_spacing/2)-20, object.winfo_reqheight()-size+(line_spacing/2)+(line_spacing)-20, text=grid[1][0], font=("Arial", 20))
    object.create_text(object.winfo_reqwidth()-(line_spacing*2)+(line_spacing/2)-20, object.winfo_reqheight()-size+(line_spacing/2)+(line_spacing)-20, text=grid[1][1], font=("Arial", 20))
    object.create_text(object.winfo_reqwidth()-(line_spacing)+(line_spacing/2)-20, object.winfo_reqheight()-size+(line_spacing/2)+(line_spacing)-20, text=grid[1][2], font=("Arial", 20))

    object.create_text(object.winfo_reqwidth()-size+(line_spacing/2)-20+(line_spacing/2)-20, object.winfo_reqheight()-(line_spacing/2)-20, text=grid[2][0], font=("Arial", 20))
    object.create_text(object.winfo_reqwidth()-(line_spacing*2)+(line_spacing/2)-20, object.winfo_reqheight()-(line_spacing/2)-20, text=grid[2][1], font=("Arial", 20))
    object.create_text(object.winfo_reqwidth()-(line_spacing)+(line_spacing/2)-20, object.winfo_reqheight()-(line_spacing/2)-20, text=grid[2][2], font=("Arial", 20))

def create_grid_list():
    grid = []
    for i in range(3):
        sub_grid = []
        for j in range(3):
            sub_grid.append(random.choice(["M", "R", "F"]))
        grid.append(sub_grid)
    return grid

def populate_grid(things: list, screen: Canvas, grid_list: list):
    things = []

    for i in range(3):
        subThings = []
        for j in range(3):
            if grid_list[i][j] == "M":
                subThings.append(Square("M", i, screen))
            elif grid_list[i][j] == "R":
                subThings.append(River("R", screen, grid_list, j, i))
            elif grid_list[i][j] == "F":
                subThings.append(Forest("F", screen))
        things.append(subThings)
    return things

def display_objects(things: list, pos: list):
    match pos:
        case [0, 0]:
            things[0][0].display()
        case [1, 0]:
            things[0][1].display()
        case [2, 0]:
            things[0][2].display()
        case [0, 1]:
            things[1][0].display()
        case [1, 1]:
            things[1][1].display()
        case [2, 1]:
            things[1][2].display()
        case [0, 2]:
            things[2][0].display()
        case [1, 2]:
            things[2][1].display()
        case [2, 2]:
            things[2][2].display()

def right(event):
    if pos[0] < 2:
        pos[0] += 1
        display_objects(objects, pos)
        create_grid(screen, 125, grid, pos)
        print(pos)
        return
    else:
        print(pos)
        return
def left(event):
    if pos[0] > 0:
        pos[0] -= 1
        display_objects(objects, pos)
        create_grid(screen, 125, grid, pos)
        print(pos)
        return
    else:
        print(pos)
        return
def up(event):
    if pos[1] > 0:
        pos[1] -= 1
        display_objects(objects, pos)
        print(pos)
        create_grid(screen, 125, grid, pos)
        return
    else:
        print(pos)
        return
def down(event):
    if pos[1] < 2:
        pos[1] += 1
        display_objects(objects, pos)
        print(pos)
        create_grid(screen, 125, grid, pos)
        return
    else:
        print(pos)
        return

root.bind("<Right>", right)
root.bind("<Left>", left)
root.bind("<Up>", up)
root.bind("<Down>", down)
screen = Canvas(root, width=600, height=600)
root.title("Map")
grid = create_grid_list()
#grid = [["R","R","R"],["R","R","R"],["R","R","R"]]
print(grid)
objects = populate_grid(grid, screen, grid)
display_objects(objects, pos)
create_grid(screen, 125, grid, pos)
screen.pack()

mainloop()