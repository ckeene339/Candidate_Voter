from tkinter import *
import csv
import os
from Candidate_Voter_gui import *



class SAVE:
    
    '''
    Function below runs all possible tests to make sure the input meets the requirements including
    original 6 digit IDs and a name has been selected.
    '''
    
    def test_data(self, voter: str, candidate: int, candidate_text, label_info: Label) -> bool:
        try:
            
            self.voter = voter
            self.candidate = candidate
            self.candidate_text = candidate_text
            
            '''
            if statement below tests to make sure a candidate was selected.
            '''
            if self.candidate > 0:
                if self.voter.strip() and self.voter.isdigit() and int(self.voter) > 0:
                    if len(self.voter) == 6:
                        '''
                        Checks to make sure voter ID is unique and 6 digits long
                        '''
                        if not self.is_voter_duplicate():
                            return True
                        else:
                            label_info.config(text='Invalid input:\nVoter ID already exists', fg='red', font=("Arial", 12))
                            return False
                    else:
                        label_info.config(text='Invalid input:\nVoter ID should be\n6 digits long', fg='red', font=("Arial", 12))
                        return False
                else:
                    label_info.config(text='Invalid input:\nPlease enter a valid\nID number', fg='red', font=("Arial", 12))
                    return False
            else:
                label_info.config(text='      Please select      \n     a candidate     ', fg='red', font=("Arial", 12))
                return False
            
        except ValueError as e:
            label_info.config(text=str(e), fg='red', font=("Arial", 12))
            return False
            
        
    '''
    Function below makes sure the voter ID is not a duplicate of one already saved
    in the csv file.
    '''
    
    def is_voter_duplicate(self) -> bool:
        try:
            if not os.path.isfile('data.csv'):
                return False
            with open('data.csv', 'r') as csv_file:
                reader = csv.reader(csv_file)
                next(reader)
                for row in reader:
                    if row[0] == self.voter:
                        return True
            return False
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    '''
    Code below saves data to csv file after checking in test_data that all information is valid.
    '''
        
    def save_data(self, voter: str, candidate: int, candidate_text, label_info: Label, radio_answer, entry_widget: Entry) -> bool:
        try:
            self.voter = voter
            self.radio_answer = radio_answer
            self.radio_answer.set(0)
            entry_widget.delete(0, END)
            self.candidate_text = candidate_text

            label_info.config(text=f'{self.candidate_text[candidate]} received a vote\n'
                                   f'from Voter #{self.voter}\n'
                                   f'_________________________\n'
                                   f'CSV file updated!', fg='black', font=("Arial", 12))

            file_exists = os.path.isfile('data.csv')

            mode = 'w' if not file_exists else 'a'

            with open('data.csv', mode, newline='') as csv_file:
                writer = csv.writer(csv_file)
                if not file_exists:
                    writer.writerow(['Voter ID', 'Candidate'])
                writer.writerow([self.voter, candidate_text[candidate]])
        except Exception as e:
            label_info.config(text=f'Error: {e}', fg='red', font=("Arial", 12))
            print(f'Error: {e}')
            return False
        else:
            return True
