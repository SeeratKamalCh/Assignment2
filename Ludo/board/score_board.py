# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 01:03:46 2020

@author: MAQS
"""
from tkinter import *

class ScoreBoard():
    def __init__(self, window, width_frame,height_frame):
        self.score_frame=window
        self.width_frame = width_frame
        self.height_frame = height_frame
    
    
    def score_board(self):
        width_frame=self.width_frame
        height_frame=self.height_frame
        score_frame=self.score_frame
        #Create score board
        NORM_FONT = ("Helvetica", 15,"bold")
        fgColor='#55AE95'
        lbColor="white"
        SMALL_FONT=("Helvetica",10,"bold")
        bgColor=fgColor
        BOX_FONT=("Helvetica",20,"bold")
        player_label_width=int(width_frame*0.01)
        player_label_height=int(height_frame*0.0001)
        # Player 1
        start_x=20
        start_y=20
        player1=Label(score_frame, width=player_label_width, height=player_label_height, text="player1",bg="white",fg="Green",font=BOX_FONT)
        player1.place(x=start_x,y=start_y)
        start_x=start_x*player_label_width+50
        player1=Text(score_frame, width = player_label_width,height=player_label_height,font=BOX_FONT)
        player1.place(x=start_x,y=start_y)
        # Player 2
        start_x=20
        start_y=start_y+player_label_height+50
        player2=Label(score_frame, width=player_label_width, height=player_label_height, text="player2",bg="white",fg="Yellow",font=BOX_FONT)
        player2.place(x=start_x,y=start_y)
        start_x=start_x*player_label_width+50
        player2=Text(score_frame, width = player_label_width,height=player_label_height,font=BOX_FONT)
        player2.place(x=start_x,y=start_y)
        # Player 3
        start_x=20
        start_y=start_y+player_label_height+50
        player3=Label(score_frame, width=player_label_width, height=player_label_height, text="player3",bg="white",fg="Blue",font=BOX_FONT)
        player3.place(x=start_x,y=start_y)
        start_x=start_x*player_label_width+50
        player3=Text(score_frame, width = player_label_width,height=player_label_height,font=BOX_FONT)
        player3.place(x=start_x,y=start_y)
        # Player 4
        start_x=20
        start_y=start_y+player_label_height+50
        player4=Label(score_frame, width=player_label_width, height=player_label_height, text="player4",bg="white",fg="Red",font=BOX_FONT)
        player4.place(x=start_x,y=start_y)
        start_x=start_x*player_label_width+50
        player4=Text(score_frame, width = player_label_width,height=player_label_height,font=BOX_FONT)
        player4.place(x=start_x,y=start_y)
        # Player turn 
        start_x=20
        start_y=start_y+player_label_height+50
        turn_player=Label(score_frame, width=player_label_width, height=player_label_height, text="Turn",bg="white",fg=fgColor,font=BOX_FONT)
        turn_player.place(x=start_x,y=start_y)
        start_x=start_x*player_label_width+50
        turn_player=Label(score_frame, width = 5,height=2)
        turn_player.place(x=start_x,y=start_y)
        turn_player.configure(state="disabled")
        turn_player.configure(background="Green")
        #Roll dice button
        start_x=20
        start_y=start_y+player_label_height+50
        roll_btn = Button(score_frame, text="Start", fg="White",bg="#55AE95",width=5,font=BOX_FONT,)  
        roll_btn.place(x=start_x,y=start_y)
        #bind roll dice btn to roll dice function
        #Dice Result
        start_x=start_x*player_label_width+50
        roll_label = Label(score_frame, height=player_label_height, fg="black",font=BOX_FONT)  
        roll_label.place(x=start_x,y=start_y)
        self.roll_label=roll_label
        return roll_btn,roll_label,turn_player
    
    def update_roll_label(self,string):
        self.roll_label['text']=string
        
                
                
                
                