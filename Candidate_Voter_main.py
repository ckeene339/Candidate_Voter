'''
This is my improved code on Lab 1
Candidate Voter Main
'''


from Candidate_Voter_gui import *


def main() -> None:
    window = Tk()
    window.title('Candidate Voter')
    window.geometry('360x320')
    window.resizable(False, False)
    GUI(window)
    window.mainloop()
    

if __name__ == "__main__":
    main()