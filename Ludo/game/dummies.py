class dummies():
    def __init__(self,row,col,circle,current_box):
        self._state="home"
        self._row=row
        self._col=col
        self._circle=circle
        self._victorybox=-1
        self._current_box=current_box
        self._start_box=0
        self._start_row=row
        self._start_col=col
        self._start_curr_box=current_box

    def set_state(self,newState):
        self._state = newState

    def set_position(self,row,col):
        self._row = row
        self._col = col

    def get_circle(self):
        return self._circle

    def get_state(self):
        return self._state

    def set_victory_box(self,box):
        self._victorybox = box
        self._current_box = -1

    def get_victory_box(self):
        return self._victorybox

    def get_current_box(self):
        return self._current_box

    def set_current_box(self,box):
        if self._victorybox==-1:
            self._current_box=box

    def get_start_box(self):
        return self._start_box

    def set_circle(self,circle):
        self._circle=circle

    def check_won(self,victorybox):
        if victorybox==5:
            return 1
        else:
            return 0
        
    def set_start_box(self,value):
        self._start_box=value

    def get_start_row_col(self):
        return self._start_row,self._start_col,self._circle

    def kill_dummy(self,circle):
        self._state="home"
        self._row=self._start_row
        self._col=self._start_col
        self._victorybox=-1
        self._circle=circle
        self._current_box=self._start_curr_box
        self._start_box=self._start_curr_box
        