# Name: Dean Nguyen Quach
# Date: 10/14/2022
# © Dean Quach 2022
# Version 1.0

# Summary: This is a bowling score game that lets you input/click on the number
# of pins knocked out from 0 to 10. A strike is a total of 10 pins knocked out at once,
# and a spare is a combined total of 10 pins knocked out in two hits per frame.
# There are 10 frames with two hit frames from frame 1 to 9. The 10th frame can store up to 3 hits. If the total pins
# knocked out is a spare or a strike. You'll get one to two more chances
# depending on the number of pins knocked out. The score is calculated on how bowling traditionally works.
# When you hit a strike or 10 pins, your score is calculated with the sum of the next two hits. When it's a spare 
# or your total of two hits in one frame is totaled to 10, your current score is calculated with the total for 
# the next hit. The maximum score for bowling is 300.



from tkinter import * 
from tkinter.ttk import  * 
import tkinter

score = [] # gets the input from the user 
single = [] # obtains the value for each number of pins and appends if it's a strike or not
double = [] # appends two singles in the current frame if it's a spare or not

single_Score = [] # current score of pins hit in a frame
double_Score = [] # current score of the two hits if the total <= 10
final_Score = [] # the total socre after the last frame


class bowlingGame(Frame):

    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.UI()

    
    #    Name: buttonClick
    #    Input: press buttons 1 to 10 to represent the number of pins hit each time;
    #           press the reset button or "11" to clear the board and restart.
    #    Function: receive integer 1 to 10, append it to list score;
    #              receive integer 11, delete variables in score, single and double lists;
    #              trigger display function.
    
    def buttonClick(self, number):
        if number <= 10:
            score.append(number)
        else:
            del score[:]
            del single[:]
            del double[:]
        self.display(score) # when the button is clicked the display function will update the score on the current frame

    
    #    Name: display
    #    Input: score list
    #    Function: 1) updates and calculates the single value list in the current frame 
    #              2) updates and calculates the double value list, the second value in the current frame;
    #              3) displays the current singleScore frame with special "X" and "/" marks depending if it's a spare or a strike; 
    #              4) displays the doubleScore text list, add up score so far for each current frame;
    #              5) calculates and displays the final score.
    
    def display(self, score):
            # checks if the reset button has been clicked
            # and clears the board/restarts the game
        if len(score) == 0:
            final_Score[0].set("")
            for i in range (0, 21):
                single_Score[i].set("")
            for i in range(0, 10):
                double_Score[i].set("") 
            return
            # checks the length of the single_Score, if it's more than 21, do nothing and return
        if len(single) > 21:
            return
        # checks the last frame, if no strike or spare, do nothing and return
        if len(single) == 20:
            if single[18] + single[19] < 10:
                return

        currentInput = score[len(score)-1] 
        # updates single value list; checks if current frame is finished
        if len(single) % 2 == 0: 
            single.append(currentInput)
            if currentInput == 10:
                if len(single) != 19 and len(single) != 20 and len(single) != 21:
                    single.append(0)
        elif len(single) % 2 == 1:
            if len(single) == 19 and single[18] == 10:
                single.append(currentInput)
            else:
                if currentInput + single[len(single)-1] <= 10:
                    single.append(currentInput)

        # update double value list;
        f = len(double)*2 # f stands for the current stage of the frame
        if len(double) == 9: # special condition for final frame
            if len(single) >= 20 and single[f] + single[f+1] < 10:
                double.append(single[f] + single[f+1])
            elif len(single) > 20:
                double.append(single[f] + single[f+1] + single[f+2])
        if len(double) < 9: # checks if current frame is less than 10
            if f+1 < len(single):
                if single[f] + single[f+1] < 10: #checks if the total score in the current frame is less than 10
                    double.append(single[f] + single[f+1])
                elif single[f] + single[f+1] == 10 and single[f] != 10: # checks the total socre of the current frame is a spare and not a strike
                    if f+2 < len(single):
                        double.append(single[f] + single[f+1] + single[f+2]) # appends the current score: spare + 2 shots 
                elif single[f] + single[f+1] == 10 and single[f] == 10: # checks if the single score in the current frame is a 10 or a strike
                    if len(double) == 8: # special condition for final frame
                        if f+3 < len(single):
                            double.append(single[f] + single[f+1] + single[f+2] + single[f+3])
                    elif f+3 < len(single):
                        if single[f+2] != 10: # strike + non-strike
                            double.append(single[f] + single[f+1] + single[f+2] + single[f+3])
                        elif single[f+2] == 10: # strike + strike
                            if len(double) == 7: # special condition for final frame
                                if f+4 < len(single):
                                    double.append(single[f] + single[f+1] + single[f+2] + single[f+3] + single[f+4])
                            if f+4 < len(single):
                                if single[f+4] == 10: # strike + strike + strike
                                    if f+5 < len(single):
                                        double.append(single[f] + single[f+1] + single[f+2] + single[f+3] + single[f+4] + single[f+5])
                                elif single[f+4] != 10: # strike + strike + non-strike
                                    double.append(single[f] + single[f+1] + single[f+2] + single[f+3] + single[f+4])
        
        # displays the single_Score
        if len(single) <= 18:
            pass_in = len(single)//2
        elif len(single) > 18:
            pass_in = 9
        # only displays single_Score for first nine frames
        for i in range(0, pass_in):
            if single[i*2] == 10:
                single_Score[i*2].set("")
                single_Score[i*2+1].set("X")
            elif single[i*2] + single[i*2+1] == 10:
                single_Score[i*2].set(single[i*2])
                single_Score[i*2+1].set("/")
            else:
                single_Score[i*2].set(single[i*2])
                single_Score[i*2+1].set(single[i*2+1])
        if len(single)%2 == 1:
            single_Score[len(single)-1].set(single[len(single)-1])

        # only handles the display single_Score for the third slot in the tenth frame
        if len(single) > 18:
            if len(single) >= 19: #check if the first slot in the 10th frame is a strike or not
                if single[18] == 10: 
                    single_Score[18].set("X")
                else:
                    single_Score[18].set(single[18])
            if len(single) >= 20: # checks if the 
                if single[19] + single[18] == 10:
                    single_Score[19].set("/")
                elif single[19] == 10:
                    single_Score[19].set("X")
                else:
                    single_Score[19].set(single[19])
            if len(single) >= 21:
                if single[20] == 10:
                    single_Score[20].set("X")
                else:
                    single_Score[20].set(single[20])
       
        # display double_Score
        for i in range(0, len(double)):
            count = 0
            for j in range(0, i+1):
                count = count + double[j]
            double_Score[i].set(count)
        # displays the final_Score
        final = 0
        for i in range(0, len(double)):
            final = final + double[i];
        final_Score[0].set(final)

    # Function: UI      
    # Input: Self
    # This is the GUI Layout 
    # 1.) user inputs from 0 to 10 
    # 2.) Restart Button to make a new game/clear the board 
    # 3.) Display Label for Scores in each frame

    def UI(self):
        self.parent.title("Bowling Score Game")
        Style().configure("W.TButton", padding=(0,6,0,6),foreground="black", background='#00ff62', font='roboto')
        Style().configure("TLabel", width=6, padding=(0,6,0,6), bg ="red", foreground="red",relief = "ridge",font='roboto', anchor="center")

        # this for loop configures for row and columns
        for i in range(0, 5): # 4 rows
            self.rowconfigure(i)
        for i in range(0, 24): # 23 columns
            self.columnconfigure(i)

        # Message at the top
        intro = "This is the bowling score game. Select any number of pins knocked out from 0 to 10!"
        msg = Label(self, text=intro).grid(row=0, column=0, columnspan=23, sticky=W+E)
        
        # All of these inputs are buttons that users can click to insert their score depending on the number including the reset button
        zero = Button(self, text=str(0), width=6, command=lambda: self.buttonClick(0)).grid(row=1,column=0)
        one = Button(self, text=str(1), width=6, command=lambda: self.buttonClick(1)).grid(row=1,column=1)
        two = Button(self, text=str(2), width=6, command=lambda: self.buttonClick(2)).grid(row=1,column=2)
        three = Button(self, text=str(3), width=6, command=lambda: self.buttonClick(3)).grid(row=1,column=3)
        four = Button(self, text=str(4), width=6, command=lambda: self.buttonClick(4)).grid(row=1,column=4)
        five = Button(self, text=str(5), width=6, command=lambda: self.buttonClick(5)).grid(row=1,column=5)
        six = Button(self, text=str(6), width=6, command=lambda: self.buttonClick(6)).grid(row=1,column=6)
        seven = Button(self, text=str(7), width=6, command=lambda: self.buttonClick(7)).grid(row=1,column=7)
        eight = Button(self, text=str(8), width=6, command=lambda: self.buttonClick(8)).grid(row=1,column=8)
        nine= Button(self, text=str(9), width=6, command=lambda: self.buttonClick(9)).grid(row=1,column=9)
        ten = Button(self, text=str(10), width=6, command=lambda: self.buttonClick(10)).grid(row=1,column=10)

        #places the reset button in the center
        new_game = Button(self, text=str("Reset"), command=lambda: self.buttonClick(11)).grid(row=5,column=8,columnspan=2)

        # This displays all of the 10 frames in one window
        frame = []
        for i in range(1, 10):
            frame_word = "Frame " + str(i)
            current = Label(self, text=frame_word)
            current.grid(row=2, column=(i-1)*2, columnspan=2, sticky=W+E)
            frame.append(current)
        frame_word = "Frame " + str(10)
        current = Label(self, text=frame_word)
        current.grid(row=2, column=(10-1)*2, columnspan=3, sticky=W+E)
        frame.append(current)

        total = Label(self, text="Total")
        total.grid(row=2, column=21, columnspan=3, sticky=W+E)

        # Displays the single scores for each frame
        for i in range(0, 22):
            single_Score.append(tkinter.StringVar())

        single = []
        for i in range(0, 21):
            single.append(Label(self, textvariable=single_Score[i]).grid(row=3, column=i, sticky=W+E))

        # Displays all the scores for all 10 frames and the final score at the bottom of the frames
        for i in range(0, 10):
            double_Score.append(tkinter.StringVar())

        double = []
        for i in range(0, 9):
            double.append(Label(self, textvariable=double_Score[i]).grid(row=4, column=i*2, columnspan=2,sticky=W+E))
        double.append(Label(self, textvariable=double_Score[9]).grid(row=4, column=9*2, columnspan=3,sticky=W+E))

        final_Score.append(tkinter.StringVar())
        Label(self, textvariable=final_Score[0]).grid(row=4, column=21, columnspan=2,sticky=W+E)
        self.pack()

# Name: if __name__ == '__main__'
# Input: none
# Function: Acts as the main driver for the game

if __name__ == '__main__':
    root = Tk()
    app = bowlingGame(root)
    root.mainloop()