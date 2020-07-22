

#draw Ludo card
from tkinter import *
from board import ludo_board as bd
from board import score_board as sb
from game import players as pl
from board import houses as hs
from random import randrange
from tkinter import messagebox

def create_circle(x, y, r, color,outline,width,canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,fill=color, outline=outline,width=width)


class Game():
    turnSwitch=0
    deleted=0
    def __init__(self,window):
        self.window=window
        self.coordinate={}
        self.empty_boxes={}
        self.house_data={}
        self.players_info={}
        self.roll_btn=""
        self.roll_label=""
        self.current_player="green"
        self.current_player_label=""
        self.turn_sequence={"green":"yellow","yellow":"blue","blue":"red","red":"green"}
        self.state="continued"
        self.dice_output=0
        
    def load_board(self):
        #Main window
        window=self.window
        coordinate=self.coordinate
        empty_boxes=self.empty_boxes
        house_data=self.house_data
        window.title('Ludo')
        width  = int (window.winfo_screenwidth())
        height =  window.winfo_screenheight()
        height= int(height*0.85)
        heightFrame=height
        widthFrame=width/2
        window.geometry(f'{width}x{height}')
        window.pack_propagate(0)
        window.configure(background='gray') # '#103c42' 
        #Ludo board
        #Left frame Ludo board
        ludo_frame=Frame(window,borderwidth=1,relief="solid",width=widthFrame,height=heightFrame,background='gray')
        ludo_frame.pack(side=LEFT)
        board_canvas=Canvas(ludo_frame, height=heightFrame, width=widthFrame, bg='gray')
        board=bd.Board(board_canvas,widthFrame,heightFrame)
        coordinate,empty_boxes,house_data,path_route=board.board()
        board_canvas.pack()
        #Score board
        score_frame= Frame(window,borderwidth=0,relief="solid",width=widthFrame,height=heightFrame)
        score_frame.columnconfigure(0, weight=1)
        score_frame.pack(side=RIGHT)
        score_board=sb.ScoreBoard(score_frame, widthFrame, heightFrame)
        self.roll_btn,self.roll_label,self.current_player_label=score_board.score_board()
        score_frame.pack_propagate(False)
        self.roll_btn.config(command=lambda :self.start_game_check())
        self.coordinate=coordinate
        self.house_data=house_data
        self.empty_boxes=empty_boxes
        self.set_players(board_canvas)
        self.path_route=path_route
        self.score_board=score_board
        self.window.bind('<Escape>', lambda e: self.destroy_window())
        return
        
    def destroy_window(self):
        self.window.destroy()
        return
        
    def set_players(self,view):
        house_data=self.house_data
        coordinate=self.coordinate
        green_data=house_data["green"]
        green_players=pl.Players(green_data,"home",coordinate,view)
        yellow_data=house_data["yellow"]
        yellow_players=pl.Players(yellow_data,"home",coordinate,view)
        blue_data=house_data["blue"]
        blue_players=pl.Players(blue_data,"home",coordinate,view)
        red_data=house_data["red"]
        red_players=pl.Players(red_data,"home",coordinate,view)
        players_info={"green":green_players, "yellow": yellow_players, 
                    "blue": blue_players, "red": red_players}
        self.players_info=players_info
        return
        
    def roll_dice(self):
        OutputList=[]
        number=0
        number=randrange(1,7)
        OutputList.append(number)
        OutputDice=str(number)
        self.score_board.update_roll_label(OutputDice)
        #messagebox.showinfo("DiceValue", OutputDice)
        while(number==6):
            number=randrange(1,7)
            OutputDice=OutputDice+ " | "+str(number)
            OutputList.append(number)       
            #messagebox.showinfo("DiceValue", OutputDice)
            self.score_board.update_roll_label(OutputDice)
        self.dice_output=OutputList
    
    def take_turn(self,OutputList,Player):
        pl.Players.set_turn_switch(0)
        #print("take_turn")
        for i in OutputList:
            self.window.update()
            victoryBoxes=hs.Houses.get_victory_path(self.current_player)
            #print(victoryBoxes)
            #print(self.current_player)
            Player.tag_players(i,self.path_route,victoryBoxes,self.players_info)
            #self.window.after(500000000000, lambda : _show('Title', 'Prompting after 5 seconds')) 
            #self.window.update()
            while(pl.Players.turn_switch==0):
                #print(pl.Players.turnSwitch)
                pl.Players.turn_switch=0
                self.window.update()
        return
    
    def start_game(self):
        current_player=self.current_player
        Player=self.players_info[current_player]
        i=0
        while(i<200 and self.check_state()):
            self.window.update()
            #roll dice
            while(self.dice_output==0):
                self.window.update()
              
            i+=1
            self.roll_btn.config(state=DISABLED)
            self.take_turn(self.dice_output,Player)
            self.current_player=self.turn_sequence[self.current_player]
            Player=self.players_info[self.current_player]
            if Player.player_state()=="won":
                #player_won
                self.current_player=self.turn_sequence[self.current_player]
            self.current_player_label.configure(background=self.current_player)
            self.score_board.update_roll_label("")
            self.dice_output=0
            self.roll_btn.config(state=NORMAL)
            #shift to next player
        self.window.destroy()
        return
            
    def check_state(self):
        players=self.players_info
        count=0
        for k,v in players.items():
            if v.player_state()=="won":
                count=count+1
        if count==3:
            return "discontinued"
        else:
            return "continued"
        
    def start_game_check(self):
        #print("start_game")
        if self.roll_btn['text']=="Start":
            self.roll_btn.config(text="Roll")
            self.roll_btn.config(command=lambda :self.roll_dice())
            return
    
window=Tk()        
new_game=Game(window)
new_game.load_board()
new_game.start_game()