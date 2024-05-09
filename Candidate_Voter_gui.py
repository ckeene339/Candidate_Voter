from tkinter import *
from Candidate_Voter_save import *

class GUI:
    def __init__(self, window: Tk) -> None:
        self.window = window
        
        self.window.configure(background='lightgray')
        
        self.label_title = Label(self.window, text="Voting Application", font=("Arial", 24))
        self.label_title.pack(pady=15)
        
        '''
        Code below sets up text box to select number of votes you want someone to recieve.
        '''
        self.frame_voterID = Frame(self.window)
        self.label_voterID = Label(self.frame_voterID, text='ID:', font=("Arial", 20))
        self.input_voterID = Entry(self.frame_voterID, width=25, font=("Arial", 15))
        self.label_voterID.pack(side='left')
        self.input_voterID.pack(padx=5, pady=5, side='top')
        self.frame_voterID.pack(anchor='w', padx=105, pady=10)
        
        
        
        '''
        Code below sets up buttons for what candidate you wish to vote for.
        '''
        self.frame_status = Frame(self.window)
        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.candidate_john = Radiobutton(self.frame_status, text='John', variable=self.radio_answer, value=1, font=("Arial", 12))
        self.candidate_brett = Radiobutton(self.frame_status, text='Brett', variable=self.radio_answer, value=2, font=("Arial", 12))
        self.candidate_kate = Radiobutton(self.frame_status, text='Kate', variable=self.radio_answer, value=3, font=("Arial", 12))
        self.candidate_john.pack(side='left')
        self.candidate_brett.pack(side='left')
        self.candidate_kate.pack(side='left')
        self.frame_status.pack()
        
        
        
        '''
        When button "VOTE" is pressed, command "submit" is called.
        '''
        self.button_save = Button(self.window, text='VOTE', command=self.submit, font=("Arial", 12))
        self.button_save.config(width=205, height=1)
        self.button_save.pack(anchor='w', padx=150, pady=10)
        self.frame_info = Frame(self.window)
        self.label_info = Label(self.frame_info, text='Enter a valid 6 digit\nVoter ID', font=("Arial", 12))
        self.label_info.pack(side='bottom')
        self.frame_info.pack(anchor='w', padx=105, pady=5)
        
        
        
        '''
        The "def submit" function calls "Project1_save" to test for any errors,
        prints a message in the window, and saves data to csv file.
        '''
    def submit(self) -> None:
        
        voter = self.input_voterID.get()
        candidate = self.radio_answer.get()
        self.candidate_text = {1: "John", 2: "Brett", 3: "Kate"}
        
        
        '''
        save.save_data is only called when save.test returns True.
        '''
        save = SAVE()
        if save.test_data(voter, candidate, self.candidate_text, self.label_info):
            save.save_data(voter, candidate, self.candidate_text, self.label_info, self.radio_answer, self.input_voterID)
        else:
            print("Test failed. Data not saved.")
            