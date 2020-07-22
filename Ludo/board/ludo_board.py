from tkinter import *
from board import houses as hs

"""Class Board to draw the board of Ludo"""
class Board():
    def __init__(self, view, ludo_width,ludo_height):
        self.view=view
        self.ludo_width = ludo_width
        self.ludo_height = ludo_height
        
    def board(self):
        coordinate={}
        grid_width = self.ludo_width/15
        grid_height = (self.ludo_height)/16
        view=self.view
        #Left frame Ludo board
        row_number = 0
        #rows and columns on Ludo board
        rows=15
        cols=15
        #Draw Simple Grid
        for row in range(rows):
            column_number = 0
            row_number = row_number + 1
            for col in range(cols):
                column_number = column_number + 1
                rect = view.create_rectangle(col * grid_width,row * 
                                             grid_height,(col + 1) * grid_width,(row + 1) * 
                                             grid_height,fill="white")
                #Sets row, column
                view.itemconfig(rect, tags=(str(row_number), str(column_number)))
                coordinate[(row,col)]=rect
        green_house_data={"row_start":0 , "col_start":0, "row_end":5, "col_end":5,"color":"green",
                          "view":view,"coordinate":coordinate,"home_row":6,
                          "home_col":1,"victory_path_row":7,"victory_path_col":1}
        green_house=hs.Houses(green_house_data)
        green_house.HousePaint()
        yellow_house_data={"row_start":0 , "col_start":9, "row_end":5, "col_end":14,"color":"yellow","view":view,
                           "coordinate":coordinate,"home_row":1,"home_col":8,"victory_path_row":1,"victory_path_col":7}
        yellow_house=hs.Houses(yellow_house_data)
        yellow_house.HousePaint()
        blue_house_data={"row_start":9 , "col_start":9, "row_end":14, "col_end":14,"color":"blue","view":view,
                         "coordinate":coordinate,"home_row":8,"home_col":13,"victory_path_row":7,"victory_path_col":13}
        blue_house=hs.Houses(blue_house_data)
        blue_house.HousePaint()
        red_house_data={"row_start":9 , "col_start":0, "row_end":14, "col_end":5,"color":"red","view":view,
                        "coordinate":coordinate,"home_row":13,"home_col":6,"victory_path_row":13,"victory_path_col":7}
        red_house=hs.Houses(red_house_data)
        red_house.HousePaint()        
        empty_boxes={"green_empty": (6,6), "yellow_empty": (6,8),"blue_empty": (8,8),"red_empty": (8,6)}
        house_data={"green":green_house_data,"yellow":yellow_house_data,"blue":blue_house_data,
                   "red":red_house_data}
        color="gray"
        view.itemconfig(coordinate[6,6], fill=color)
        view.itemconfig(coordinate[6,8], fill=color)
        view.itemconfig(coordinate[8,8], fill=color)
        view.itemconfig(coordinate[8,6], fill=color)   
        path_route=self.define_path(empty_boxes)
        return coordinate,empty_boxes,house_data,path_route
    
    def define_path(self,empty_boxes):
        direction="right"
        green_empty=empty_boxes["green_empty"]
        yellow_empty=empty_boxes["yellow_empty"]
        blue_empty=empty_boxes["blue_empty"]
        red_empty=empty_boxes["red_empty"]
        path_route=[]
        row=6
        col=1
        count=0
        for i in range(52):        #total boxes in path of ludo
            path_route.append([row,col])
            count=count+1
            #direction,row,col=self.get_direction(row,col,empty_boxes,direction)
            if direction=="right":
                if col+1==15 or col+1==9:
                    #move down
                    direction="down"
                    row=row+1
                elif row==green_empty[0] and col+1==green_empty[1]:
                    direction="up"
                    row-=1
                    col+=1
                else:
                    col=col+1
            elif direction=="down":
                if row+1==15 or row+1==9:
                    #move left
                    direction="left"
                    col=col-1
                elif row+1==yellow_empty[0] and col==yellow_empty[1]:
                    direction="right"
                    row=row+1
                    col=col+1
                else:
                    row=row+1
            elif direction=="left":
                if col-1==5 or col-1==-1:
                    #move down
                    direction="up"
                    row=row-1
                elif row==blue_empty[0] and col-1==blue_empty[1]:
                    direction="down"
                    row=row+1
                    col=col-1
                else:
                    col=col-1
            elif direction=="up":
                if row-1==5 or row-1==-1:
                    #move down
                    direction="right"
                    col=col+1
                elif row-1==red_empty[0] and col==red_empty[1]:
                    direction="left"
                    row=row-1
                    col=col-1
                else:
                    row=row-1
            
        return path_route
    
    