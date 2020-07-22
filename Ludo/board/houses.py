
"""Houses"

"""

class Houses():
    victory_boxes_green=[]
    victory_boxes_yellow=[]
    victory_boxes_blue=[]
    victory_boxes_red=[]
        
    def __init__(self,data):
        self.row_start=data["row_start"]   # 0 to 5 for green
        self.col_start=data["col_start"]
        self.row_end=data["row_end"]
        self.col_end=data["col_end"]
        self.color=data["color"]
        self.view=data["view"]
        self.coordinate=data["coordinate"]
        self.home_row=data["home_row"]
        self.home_col=data["home_col"]
        self.victory_row=data["victory_path_row"]
        self.victory_col=data["victory_path_col"]
        
        
    def HousePaint(self):
        house_color=self.color
        row_start=self.row_start
        col_start=self.col_start
        row_end=self.row_end
        col_end=self.col_end
        view=self.view
        coordinate=self.coordinate
        home_row=self.home_row
        home_col=self.home_col
        victory_row=self.victory_row
        victory_col=self.victory_col
        default_color="white"
        #paint the house
        for row in range(row_start,row_end+1):
            for col in range(col_start,col_end+1):
                if row==row_start or row==row_end or col==col_start or col==col_end:
                    fill=house_color
                else:
                    fill=default_color            
                view.itemconfig(coordinate[row,col], fill=fill,outline=fill)    
        view.itemconfig(coordinate[home_row,home_col], fill=house_color)
        #Victory path
        row=victory_row
        col=victory_col
        if house_color=="green":
            for col in range(col,col+6):
                view.itemconfig(coordinate[row,col], fill=house_color) 
                Houses.victory_boxes_green.append([row,col])
        elif house_color=="yellow":     
            for row in range(row,row+6):
                view.itemconfig(coordinate[row,col], fill=house_color)
                Houses.victory_boxes_yellow.append([row,col])
        elif house_color=="blue":
            for col in range(col,col-6,-1):
                view.itemconfig(coordinate[row,col],fill=house_color) 
                Houses.victory_boxes_blue.append([row,col])
        else:
            for row in range(row,row-6,-1):
                view.itemconfig(coordinate[row,col], fill=house_color) 
                Houses.victory_boxes_red.append([row,col])
            
    def get_victory_path(house):
        if house=="green":
            return Houses.victory_boxes_green
        if house=="yellow":
            return Houses.victory_boxes_yellow
        if house=="blue":
            return Houses.victory_boxes_blue
        if house=="red":
            return Houses.victory_boxes_red
        return 
    
               
        