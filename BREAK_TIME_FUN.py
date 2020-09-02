# importing tkinter module for making GUI

import tkinter

# creating first window of the game i.e. is the main home window.
main_window = tkinter.Tk()
# delcaring the title of the window - main_window
main_window.title("BREAK - TIME FUN!")
# size of main_window
main_window.geometry('600x500')

# uploading image on the interface
photo = tkinter.PhotoImage(file = "page_7.png")
background_label = tkinter.Label(main_window, image=photo)
background_label.pack()

# function for instructions page
def info():
    
    main_window.withdraw()
    # creating the window gameinfo
    gameinfo = tkinter.Tk()
    # delcaring the title of the window - gameinfo
    gameinfo.title('GAME INFO')
    # size of gameinfo
    gameinfo.geometry('600x500')
    # changing the bg color of window   
    gameinfo.config(bg = 'teal')

    infomsg = """1. You have 3 lives!

2. You can only answer once per question.

3. There are 2 SKIP options available.

4. Once you have disclosed a tile it cannot be closed again.

5. Each wrong answer results to -1 life.

6. Fourth wrong attempt leads to game over.

7. If you give a correct answer, only then next tile appears on your screen. 

8. You cannot go to the next question until you solve the current question. 

9. All the best! Get set go…."""

    # displaying the heading and instructions in label
    tkinter.Label(gameinfo, text = "GAME INFO", font = ('Cambria', 25), fg = 'white', bg = 'teal', justify = 'left').pack(padx = 8, pady = 20)    
    tkinter.Label(gameinfo, text = infomsg , font = ('Calibiri light', 13), fg = 'white', bg = 'teal', justify = 'left').pack(pady = 20)
    # PLAY GAME! button
    tkinter.Button(gameinfo, text = "BACK", command = lambda: (gameinfo.destroy(), main_window.deiconify()), font = ('Calibiri light', 13), fg = 'teal', bg = 'white', activeforeground = 'white', activebackground = 'black').place(bordermode = 'outside',height = 30, width = 150, x = 400, y = 440)
    # loop of the window
    gameinfo.mainloop()


def play():

    # creating the window playgame
    playgame = tkinter.Tk()
    # delcaring the title of the window - playgame
    playgame.title('PLAY GAME')
    # size of playgame
    playgame.geometry('600x500')
    # changing the bg color of window   
    playgame.config(bg = 'teal')


    # MATH 
    
    def math():
        # creating the window mathgame
        mathgame = tkinter.Tk()
        # delcaring the title of the window - mathgame
        mathgame.title('MATH')
        # size of mathgame
        mathgame.geometry('600x500')
        # changing the bg color of window
        mathgame.config(bg = 'lightcyan')
        
        # declaring the variable score as global
        global score
        score = 0
                
        tkinter.Label(mathgame, text = 'SCORE:', bg = 'lightcyan', fg = 'teal', font = ('Consolas', 15)).place(x = 10, y = 20)
        score_label = tkinter.Label(mathgame, text = 0, bg = 'lightcyan', fg = 'teal', font = ('Consolas', 15))
        score_label.place(x = 80, y = 20)
        
        tkinter.Label(mathgame, text = 'Gear up your brain!', bg = 'lightcyan', fg = 'teal', font = ('Consolas', 20)).pack(padx = 20, pady = 80)
        
        questions = ["How many hundred\nthousands make\na million?", "Total number of\n three digit \nnumbers?", "What is the \nbasic unit of \ngeometry?" ]
            
        # First set of questions
        
        def clicktry1():
            global answer1
            # change text on the TRY ME button after clicking on it and display the input box
            try1['text'] = questions[0]
            answer1 = tkinter.Entry(mathgame, width = 19)
            answer1.place(x = 30, y = 410)
            answer1.focus_set()
            tkinter.Button(mathgame, text = 'Done', command = check1, bg = 'lightseagreen').place(x = 35, y = 440)
            
        try1 = tkinter.Button(mathgame, text = "TRY ME", command = clicktry1, font = ('Candara', 13), fg = 'white', bg = 'lightseagreen', activebackground = 'cadetblue', activeforeground = 'white')
        try1.place(bordermode = 'outside', height = 200, width = 150, x = 35, y = 200)

        
        # Second set of questions

        def clicktry2():
            global answer2
            # change text on the TRY ME button after clicking on it and display the input box
            try2['text'] = questions[1]
            answer2 = tkinter.Entry(mathgame, width = 19)
            answer2.place(x = 220, y = 410)
            answer2.focus_set()
            tkinter.Button(mathgame, text = 'Done', command = check2, bg = 'lightseagreen').place(x = 225, y = 440)
            
        try2 = tkinter.Button(mathgame, text = "TRY ME", command = clicktry2, font = ('Candara', 13), fg = 'white', bg = 'lightseagreen', activebackground = 'cadetblue', activeforeground = 'white')
        try2.place(bordermode = 'outside', height = 200, width = 150, x = 225, y = 200)
               

        def clicktry3():
            global answer3
            # change text on the TRY ME button after clicking on it and display the input box
            try3['text'] = questions[2]
            answer3 = tkinter.Entry(mathgame, width = 19)
            answer3.place(x = 410, y = 410)
            answer3.focus_set()
            tkinter.Button(mathgame, text = 'Done', command = check3, bg = 'lightseagreen').place(x = 415, y = 440)
        
        try3 = tkinter.Button(mathgame, text = "TRY ME", command = clicktry3, font = ('Candara', 13), fg = 'white', bg = 'lightseagreen', activebackground = 'cadetblue', activeforeground = 'white')
        try3.place(bordermode = 'outside', height = 200, width = 150, x = 415, y = 200)

        # checkpoint for the first riddle

        def check1():
            global score
            s = answer1.get()
            answer1.destroy()
            
            if s.lower() == '10' or s.lower() == 'ten':
                print("correct")
                score += 5
                score_label.config(text = score)
                tkinter.Label(mathgame, text = "Correct answer!", bg = 'white', fg = 'green').place(x = 90, y = 443)
            else:
                print("wrong")
                score -= 4
                score_label.config(text = score)
                tkinter.Label(mathgame, text = "Wrong answer!", bg = 'white', fg = 'red').place(x = 90, y = 443)

        # checkpoint for the second riddle

        def check2():
            global score
            s = answer2.get()
            answer2.destroy()
            
            if s.lower() == '999':
                print("correct")
                score += 5
                score_label.config(text = score)
                tkinter.Label(mathgame, text = "Correct answer!", bg = 'white', fg = 'green').place(x = 280, y = 443)
            else:
                print("wrong")
                score -= 4
                score_label.config(text = score)                
                tkinter.Label(mathgame, text = "Wrong answer!", bg = 'white', fg = 'red').place(x = 280, y = 443)

        # checkpoint for the third riddle

        def check3():
            global score
            s = answer3.get()
            answer3.destroy()
            
            if s.lower() == 'point':
                print("correct")
                score += 5
                score_label.config(text = score)
                tkinter.Label(mathgame, text = "Correct answer!", bg = 'white', fg = 'green').place(x = 470, y = 443)
            else:
                print("wrong")
                score -= 4
                score_label.config(text = score)
                tkinter.Label(mathgame, text = "Wrong answer!", bg = 'white', fg = 'red').place(x = 470, y = 443)
                

        # destroying the previous window
        playgame.destroy()
        # loop of the window
        mathgame.mainloop()

    
    # RIDDLE 
    
    def riddle():
        # creating the window riddlegame
        riddlegame = tkinter.Tk()
        # delcaring the title of the window - riddlegame
        riddlegame.title('RIDDLE')
        # size of riddlegame
        riddlegame.geometry('600x500')
        # changing the bg color of window
        riddlegame.config(bg = 'lightcyan')
        
        # declaring the variable score as global
        global score
        score = 0
                
        tkinter.Label(riddlegame, text = 'SCORE:', bg = 'lightcyan', fg = 'teal', font = ('Consolas', 15)).place(x = 10, y = 20)
        score_label = tkinter.Label(riddlegame, text = 0, bg = 'lightcyan', fg = 'teal', font = ('Consolas', 15))
        score_label.place(x = 80, y = 20)
        
        tkinter.Label(riddlegame, text = 'Let your brain exercise', bg = 'lightcyan', fg = 'teal', font = ('Consolas', 20)).pack(padx = 20, pady = 80)
        
        riddles = ["You answer me,\nalthough I never\n ask you questions.\nWhat am I?", "What has\n hands but\n doesn’t claps?", "What word is\n always \npronounced\n wrong?" ]
            
        # First set of riddles
        
        def clicktry1():
            global answer1
            # change text on the TRY ME button after clicking on it and display the input box
            try1['text'] = riddles[0]
            answer1 = tkinter.Entry(riddlegame, width = 19)
            answer1.place(x = 30, y = 410)
            answer1.focus_set()
            tkinter.Button(riddlegame, text = 'Done', command = check1, bg = 'lightseagreen').place(x = 35, y = 440)
            
        try1 = tkinter.Button(riddlegame, text = "TRY ME", command = clicktry1, font = ('Candara', 13), fg = 'white', bg = 'lightseagreen', activebackground = 'cadetblue', activeforeground = 'white')
        try1.place(bordermode = 'outside', height = 200, width = 150, x = 35, y = 200)

        
        # Second set of riddles

        def clicktry2():
            global answer2
            # change text on the TRY ME button after clicking on it and display the input box
            try2['text'] = riddles[1]
            answer2 = tkinter.Entry(riddlegame, width = 19)
            answer2.place(x = 220, y = 410)
            answer2.focus_set()
            tkinter.Button(riddlegame, text = 'Done', command = check2, bg = 'lightseagreen').place(x = 225, y = 440)
            
        try2 = tkinter.Button(riddlegame, text = "TRY ME", command = clicktry2, font = ('Candara', 13), fg = 'white', bg = 'lightseagreen', activebackground = 'cadetblue', activeforeground = 'white')
        try2.place(bordermode = 'outside', height = 200, width = 150, x = 225, y = 200)
               
        # Third set of riddles
        
        def clicktry3():
            global answer3
            # change text on the TRY ME button after clicking on it and display the input box
            try3['text'] = riddles[2]
            answer3 = tkinter.Entry(riddlegame, width = 19)
            answer3.place(x = 410, y = 410)
            answer3.focus_set()
            tkinter.Button(riddlegame, text = 'Done', command = check3, bg = 'lightseagreen').place(x = 415, y = 440)
        
        try3 = tkinter.Button(riddlegame, text = "TRY ME", command = clicktry3, font = ('Candara', 13), fg = 'white', bg = 'lightseagreen', activebackground = 'cadetblue', activeforeground = 'white')
        try3.place(bordermode = 'outside', height = 200, width = 150, x = 415, y = 200)

        # checkpoint for the first riddle
        
        def check1():
            global score
            s = answer1.get()
            answer1.destroy()
            
            if s.lower() == 'telephone':
                print("correct")
                score += 5
                score_label.config(text = score)
                tkinter.Label(riddlegame, text = "Correct answer!", bg = 'white', fg = 'green').place(x = 90, y = 443)
            else:
                print("wrong")
                score -= 4
                score_label.config(text = score)
                tkinter.Label(riddlegame, text = "Wrong answer!", bg = 'white', fg = 'red').place(x = 90, y = 443)

        # checkpoint for the second riddle

        def check2():
            global score
            s = answer2.get()
            answer2.destroy()
            
            if s.lower() == 'clock':
                print("correct")
                score += 5
                score_label.config(text = score)
                tkinter.Label(riddlegame, text = "Correct answer!", bg = 'white', fg = 'green').place(x = 280, y = 443)
            else:
                print("wrong")
                score -= 4
                score_label.config(text = score)                
                tkinter.Label(riddlegame, text = "Wrong answer!", bg = 'white', fg = 'red').place(x = 280, y = 443)

        # checkpoint for the third riddle

        def check3():
            global score
            s = answer3.get()
            answer3.destroy()
            
            if s.lower() == 'wrong':
                print("correct")
                score += 5
                score_label.config(text = score)
                tkinter.Label(riddlegame, text = "Correct answer!", bg = 'white', fg = 'green').place(x = 470, y = 443)
            else:
                print("wrong")
                score -= 4
                score_label.config(text = score)
                tkinter.Label(riddlegame, text = "Wrong answer!", bg = 'white', fg = 'red').place(x = 470, y = 443)

        # destroying the previous window
        playgame.destroy()
        # loop of the window
        riddlegame.mainloop()

        
    # G.K.

    def gk():
        # creating the window gkgame
        gkgame = tkinter.Tk()
        # delcaring the title of the window - gkgame
        gkgame.title('GK')
        # size of gkgame
        gkgame.geometry('600x500')
        # changing the bg color of window
        gkgame.config(bg = 'lightcyan')
        
        # declaring the variable score as global
        global score
        score = 0
                
        tkinter.Label(gkgame, text = 'SCORE:', bg = 'lightcyan', fg = 'teal', font = ('Consolas', 15)).place(x = 10, y = 20)
        score_label = tkinter.Label(gkgame, text = 0, bg = 'lightcyan', fg = 'teal', font = ('Consolas', 15))
        score_label.place(x = 80, y = 20)
        
        tkinter.Label(gkgame, text = 'Test your knowledge!', bg = 'lightcyan', fg = 'teal', font = ('Consolas', 20)).pack(padx = 20, pady = 80)
        
        knowledge = ["Which country has\nthe biggest \npopulation?", "Which country has\nthe largest \nland area?", "Which is the \nbiggest state of\n U.S.A.?" ]
            
        # First set of knowledge
        
        def clicktry1():
            global answer1
            # change text on the TRY ME button after clicking on it and display the input box
            try1['text'] = knowledge[0]
            answer1 = tkinter.Entry(gkgame, width = 19)
            answer1.place(x = 30, y = 410)
            answer1.focus_set()
            tkinter.Button(gkgame, text = 'Done', command = check1, bg = 'lightseagreen').place(x = 35, y = 440)
            
        try1 = tkinter.Button(gkgame, text = "TRY ME", command = clicktry1, font = ('Candara', 13), fg = 'white', bg = 'lightseagreen', activebackground = 'cadetblue', activeforeground = 'white')
        try1.place(bordermode = 'outside', height = 200, width = 150, x = 35, y = 200)

        
        # Second set of knowledge

        def clicktry2():
            global answer2
            # change text on the TRY ME button after clicking on it and display the input box
            try2['text'] = knowledge[1]
            answer2 = tkinter.Entry(gkgame, width = 19)
            answer2.place(x = 220, y = 410)
            answer2.focus_set()
            tkinter.Button(gkgame, text = 'Done', command = check2, bg = 'lightseagreen').place(x = 225, y = 440)
            
        try2 = tkinter.Button(gkgame, text = "TRY ME", command = clicktry2, font = ('Candara', 13), fg = 'white', bg = 'lightseagreen', activebackground = 'cadetblue', activeforeground = 'white')
        try2.place(bordermode = 'outside', height = 200, width = 150, x = 225, y = 200)
               
        # Third set of knowledge

        def clicktry3():
            global answer3
            # change text on the TRY ME button after clicking on it and display the input box
            try3['text'] = knowledge[2]
            answer3 = tkinter.Entry(gkgame, width = 19)
            answer3.place(x = 410, y = 410)
            answer3.focus_set()
            tkinter.Button(gkgame, text = 'Done', command = check3, bg = 'lightseagreen').place(x = 415, y = 440)
        
        try3 = tkinter.Button(gkgame, text = "TRY ME", command = clicktry3, font = ('Candara', 13), fg = 'white', bg = 'lightseagreen', activebackground = 'cadetblue', activeforeground = 'white')
        try3.place(bordermode = 'outside', height = 200, width = 150, x = 415, y = 200)

        # checkpoint for the first question

        def check1():
            global score
            s = answer1.get()
            answer1.destroy()
            
            if s.lower() == 'china':
                print("correct")
                score += 5
                score_label.config(text = score)
                tkinter.Label(gkgame, text = "Correct answer!", bg = 'white', fg = 'green').place(x = 90, y = 443)
            else:
                print("wrong")
                score -= 4
                score_label.config(text = score)
                tkinter.Label(gkgame, text = "Wrong answer!", bg = 'white', fg = 'red').place(x = 90, y = 443)

        # checkpoint for the second question

        def check2():
            global score
            s = answer2.get()
            answer2.destroy()
            
            if s.lower() == 'russia':
                print("correct")
                score += 5
                score_label.config(text = score)
                tkinter.Label(gkgame, text = "Correct answer!", bg = 'white', fg = 'green').place(x = 280, y = 443)
            else:
                print("wrong")
                score -= 4
                score_label.config(text = score)                
                tkinter.Label(gkgame, text = "Wrong answer!", bg = 'white', fg = 'red').place(x = 280, y = 443)

        # checkpoint for the third question

        def check3():
            global score
            s = answer3.get()
            answer3.destroy()
            
            if s.lower() == 'alaska':
                print("correct")
                score += 5
                score_label.config(text = score)
                tkinter.Label(gkgame, text = "Correct answer!", bg = 'white', fg = 'green').place(x = 470, y = 443)
            else:
                print("wrong")
                score -= 4
                score_label.config(text = score)
                tkinter.Label(gkgame, text = "Wrong answer!", bg = 'white', fg = 'red').place(x = 470, y = 443)

        # destroying the previous window
        playgame.destroy()
        # loop of the window
        gkgame.mainloop()

       
    # displaying headings in Label
    tkinter.Label(playgame, text = 'WHAT ARE YOU CAPABLE OF?', font = ('consolas', 22), fg = 'white', bg = 'teal').place(x = 108, y = 80)
    # displaying MATH card (button)
    b1 = tkinter.Button(playgame, text = "MATH", command = math, font = ('Candara', 18), fg = 'teal', bg = 'lightcyan', activebackground = 'cadetblue', activeforeground = 'white')
    b1.place(bordermode = 'outside', height = 200, width = 150, x = 35, y = 200)
    # displaying RIDDLE card (button)    
    b2 = tkinter.Button(playgame, text = "RIDDLE", command = riddle, font = ('Candara', 18), fg = 'teal', bg = 'lightcyan', activebackground = 'cadetblue', activeforeground = 'white')
    b2.place(bordermode = 'outside', height = 200, width = 150, x = 225, y = 200)
    # displaying G.K. card (button)    
    b3 = tkinter.Button(playgame, text = "G.K.", command = gk, font = ('Candara', 18), fg = 'teal', bg = 'lightcyan', activebackground = 'cadetblue', activeforeground = 'white')
    b3.place(bordermode = 'outside', height = 200, width = 150, x = 415, y = 200)
    
    # destroying the previous window        
    main_window.destroy()
    # loop of the window
    playgame.mainloop()

# PLAY GAME! and GAME INFO buttons.
tkinter.Button(main_window, text = "PLAY GAME!", command = play, font = ('Calibiri light', 18), fg = 'white', bg = 'teal', activebackground = 'white', activeforeground = 'teal').place(bordermode = 'outside', height = 45, width = 190, x = 372, y = 350)
tkinter.Button(main_window, text = "GAME INFO", command = info, font = ('Calibiri light', 18), fg = 'white', bg = 'teal', activebackground = 'white', activeforeground = 'teal').place(bordermode = 'outside',height = 45, width = 170, x = 380, y = 420)

main_window.mainloop()