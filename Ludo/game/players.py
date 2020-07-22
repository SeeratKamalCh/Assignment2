
from tkinter import *
from game import dummies as dm
from time import sleep
from tkinter import messagebox

def create_circle(x, y, r, color,outline,width,canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,fill=color, outline=outline,width=width)

class Players():
    turn_switch=0
    def __init__(self,data,state,coordinate,view):  #state=home or win
        self.row_start=data["row_start"]
        self.col_start=data["col_start"]
        self.row_end=data["row_end"]
        self.col_end=data["col_end"]
        self.state=state   #Home, Won
        self.house=data["color"]
        self.coordinate=coordinate
        self.view=view
        #self.PathLocation={}
        #Create green players
        row=int((self.row_start+self.row_end)/2)
        col=int((self.col_start+self.col_end)/2)
        #Add binding function to these rectangles
        player1=coordinate[(row,col)]
        player2=coordinate[(row,col+1)]
        player3=coordinate[(row+1,col)]
        player4=coordinate[(row+1,col+1)]
        x0,y0,x1,y1=view.coords(player1)
        circle1=create_circle(int((x0+x1)/2),int((y0+y1)/2),15, self.house, "#DDD", 4,view)
        x0,y0,x1,y1=view.coords(player2)
        circle2=create_circle(int((x0+x1)/2),int((y0+y1)/2),15, self.house, "#DDD", 4,view)
        x0,y0,x1,y1=view.coords(player3)
        circle3=create_circle(int((x0+x1)/2),int((y0+y1)/2),15, self.house, "#DDD", 4,view)
        x0,y0,x1,y1=view.coords(player4)
        circle4=create_circle(int((x0+x1)/2),int((y0+y1)/2),15, self.house, "#DDD", 4,view)
        
        current_box=self.get_dummies_current_box(self.house)
        Dummies=[]
        Dummies.append(dm.dummies(row,col,circle1,current_box))
        Dummies.append(dm.dummies(row,col+1,circle2,current_box))
        Dummies.append(dm.dummies(row+1,col,circle3,current_box))
        Dummies.append(dm.dummies(row+1,col+1,circle4,current_box))
        self.Dummies=Dummies
        
        
        
    def get_dummies_current_box(self,house):
        box=0
        if house=="green":
            box=0
        elif house=="yellow":
            box=13
        elif house=="blue":
            box=26
        elif house=="red":
            box=39
        return box
    
    def set_row_and_col(self,row,col):
        self.row=row
        self.col=col        
        
    def update_players(self,row,col,circle,increment):
        rect=self.coordinate[(row,col)]
        x0,y0,x1,y1=self.view.coords(rect)
        new_circle=create_circle(int((x0+x1)/2+increment),int((y0+y1)/2),15, self.house, "#DDD", 4,self.view)
        self.view.delete(circle)
        return new_circle
    
    def update_location(self,event,i):
        dummy=self.Dummies[i]
        increment=self.increment
        if dummy.get_state()=="home" and self.increment<6:
            self.untag_players()
            Players.turn_switch=1
            return
        elif dummy.get_state()=="home" and self.increment==6:
            increment=0
        path_route=self.path_route
        victory_boxes=self.victoryPath
        circle=dummy.get_circle()
        state=dummy.get_state()
        victorybox=dummy.get_victory_box()
        current_box=dummy.get_current_box()
        start_box=dummy.get_start_box()
        #here get the circle and update location according to new row and new col
        #get current box
        current_box=(current_box+increment)%(len(path_route))
        start_box=start_box+increment
        if start_box<51 and state!="victory": #move to regular path
            #not reached victory path yet
            #get row and col of new path
            self.Dummies[i].set_state("regular")
            current_info=path_route[current_box] #self.path_route
            overlap=self.check_overlap(current_box)
            new_circle=self.update_players(current_info[0], current_info[1],circle,overlap/0.2)
            self.Dummies[i].set_circle(new_circle)
            self.Dummies[i].set_start_box(start_box)
            self.Dummies[i].set_current_box(current_box)
        elif state=="victory" or start_box>50:
            #move along the victory path and keep count of the steps
            self.Dummies[i].set_state("victory")
            victory_box_indexes=start_box-51
            current_box=-1
            check_if_won=0
            new_circle=""
            #print(VictoryBoxes)
            if victory_box_indexes<5:
                new_circle=self.update_players(victory_boxes[victory_box_indexes][0],victory_boxes[victory_box_indexes][1], circle,0)
                self.Dummies[i].set_circle(new_circle)
                self.Dummies[i].set_victory_box(victory_box_indexes)
                self.Dummies[i].set_start_box(start_box)
                self.Dummies[i].set_current_box(current_box)
                check_if_won=self.Dummies[i].check_won(victory_box_indexes)
            elif victory_box_indexes==5:
                check_if_won=1
            if check_if_won==1:
                #print("won")
                new_circle=self.update_players(victory_boxes[5][0],victory_boxes[5][1], circle,0)
                #self.view.itemconfigure(new_circle, state='hidden'/'normal')
                #self.view.delete(circle)
                self.Dummies[i].set_victory_box(victory_box_indexes)
                self.Dummies[i].set_current_box(current_box)
                self.Dummies[i].set_circle(new_circle)
                self.Dummies[i].set_start_box(start_box)
                self.Dummies[i].set_state("won")
            #Check hasWon
        self.untag_players()
        self.has_won()
        if increment==0:
            self.Dummies[i].set_state("regular")
        self.check_killed(current_box)
        Players.turn_switch=1
        return
       
    def check_killed(self,current_box):
        Safeboxes=[-1, 0,13,26,39]
        players=["green","yellow","blue","red"]
        if current_box not in Safeboxes and current_box!=-1:
            for i in players:
                if i!=self.house:
                    player=self.playersInfo[i]
                    Dummies=player.get_dummies()
                    for j in range(len(Dummies)):
                        if Dummies[j].get_current_box()==current_box:
                            player.kill_player(j)   
        return
                            
    def check_overlap(self,current_box):
        Safeboxes=[-1, 0,13,26,39]
        players=["green","yellow","blue","red"]
        count=0
        if current_box in Safeboxes:
            for i in players:
                if i!=self.house:
                    Player=self.playersInfo[i]
                    Dummies=Player.get_dummies()
                    for j in range(len(Dummies)):
                        if Dummies[j].get_current_box()==current_box:
                            count+=1
        return count
    
    def tag_players(self,increment,path_route,victoryPath,playersInfo):
        dummies_states=self.check_states_dummies()
        boundCount=0
        boolBound=False
        # if won then dont bind
        # if victory but small then dont bind
        # if increment==6 but not won then bind
        # if regular state then  bind
        if (dummies_states==True and increment==6) or dummies_states==False:
            Players.turn_switch=0
            self.increment=increment
            self.path_route=path_route
            self.victoryPath=victoryPath
            self.playersInfo=playersInfo
            for i in range(len(self.Dummies)):
                boolBound=False
                print(self.Dummies[i].get_state())
                print(self.Dummies[i].get_start_box()+increment-51)
                if ((self.Dummies[i].get_state()=="victory" 
                    and (self.Dummies[i].get_start_box()+increment-51<=5 
                         and self.Dummies[i].get_start_box()+increment-51>=0))):
                    boolBound=True
                elif self.Dummies[i].get_state()=="regular":
                    boolBound=True
                elif self.Dummies[i].get_state()=="home" and increment==6:
                    boolBound=True
                
                if boolBound==True:
                    self.view.tag_bind(self.Dummies[i].get_circle(), "<1>",lambda event,count=i:
                            self.update_location(event,count))
                else:
                    boundCount=boundCount+1
            self.view.update()
            #print("player tagged")
        elif dummies_states==True and increment<6:
            #messagebox.showinfo("DiceValue", "Cannot move")
            sleep(0.5)
            Players.turn_switch=1
            #print("Next turn")
        if boundCount==4:
            sleep(0.5)
            Players.turn_switch=1
        return
            
    def untag_players(self):
         for i in self.Dummies:
            self.view.tag_unbind(i.get_circle(), "<1>")
            self.view.update()
         return
            
    def player_dummies(self):
        return self.Dummies
        
    def has_won(self):
        Dummies=self.Dummies
        if Dummies[0].get_state()=="won" and Dummies[1].get_state()=="won" and Dummies[2].get_state()=="won" and Dummies[3].get_state()=="won":
            self.state="won"
            return 1
        else:
            return 0
        return
        
    def check_states_dummies(self):
        count=0
        for i in self.Dummies:
            if i.get_state()=="home":
                count=count+1
        if count==4:
            return True
        return False
        
    def kill_player(self,index):
        row,col,oldCircle=self.Dummies[index].get_start_row_col()
        circle=self.update_players(row,col,oldCircle,0)
        self.Dummies[index].kill_dummy(circle)
        return
        
    def update_dummy(self):
        return
    
    def player_state(self):
        return self.state    
        
    def get_turn_switch():
        return Players.turn_switch
    
    def set_turn_switch(value):
        Players.turn_switch=value
    
    def get_dummies(self):
        return self.Dummies
    
