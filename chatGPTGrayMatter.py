from tkinter import *
import customtkinter
import openai
import os
import pickle


tkGUI = customtkinter.CTk()
tkGUI.title("GPT Chat Bot")
tkGUI.geometry('600x600')
#tkGUI.iconbitmap('ai_lt.ico') need icon file

#set Color scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def speak():
    if(chatEntry.get()):
        #do something
        fileName = "apikey"

        try:
            if os.path.isfile(fileName):
                # open the file
                inputFile = open(fileName, 'rb')

                # Load the data from the file into a variable
                stuff = pickle.load(inputFile)

                #query chat GPT
                #define API Key
                openai.api_key = stuff

                #create an instance
                openai.Model.list()

                response = openai.Completion.create(model="text-davinci-003", prompt=chatEntry.get(),
                                                    temperature=0, max_tokens=200,
                                                    top_p=1.0,
                                                    frequency_penalty=0.0,
                                                    presence_penalty=0.0)

                myText.insert(END, (response["choices"][0]["text"]).strip())
                myText.insert(END, "\n\n")


            else:
                inputFile = open(fileName, 'wb')
                inputFile.close()
                #Error - need an api key
                myText.insert(END, "\n\n No Secret Key. Get one at https://platform.openai.com/account/api-keys")

        except Exception as e:
            myText.insert(END, f"\n\n There was an error \n\n {e}")
    else:
        myText.insert(END, "\n\n Ask a question before you submit")

def clear():
    #clear main text box
    myText.delete(1.0, END)
    #clear query box
    chatEntry.delete(0, END)

def key ():
    #resize app
    tkGUI.geometry('600x750')
    #Reshow API frame
    apiFrame.pack(pady=20)
    apiBtnFrame.pack(pady=10, padx=10)

    #define file name
    fileName = "apikey"

    try:
        if os.path.isfile(fileName):
            #open the file
            inputFile = open(fileName, 'rb')

            #Load the data from the file into a variable
            stuff = pickle.load(inputFile)

            #output stuff to entry box
            apiEntry.insert(END, stuff)

        else:
            inputFile = open(fileName, 'wb')
            inputFile.close()

    except Exception as e:
        myText.insert(END, f"\n\n There was an error \n\n {e}")

#save api key

def saveKey():
    #define filename
    filename = "apikey"

    try:
        #open file
        outputFile = open(filename, 'wb')

        #add data to file
        pickle.dump(apiEntry.get(), outputFile)

        #delete entry box
        apiEntry.delete(0, END)

        #hide api frame
        apiFrame.pack_forget()
        apiBtnFrame.pack_forget()
        #make app smaller
        tkGUI.geometry('600x600')

    except Exception as e:
        myText.insert(END, f"\n\n There was an error \n\n {e}")


def clearKey():
    # define filename
    filename = "apikey"

    try:
        # open file
        outputFile = open(filename, 'wb')

        outputFile.flush()

        # delete entry box
        apiEntry.delete(0, END)

        # hide api frame
        apiFrame.pack_forget()
        apiBtnFrame.pack_forget()
        # make app smaller
        tkGUI.geometry('600x600')

    except Exception as e:
        myText.insert(END, f"\n\n There was an error \n\n {e}")

def onEnter():
    speak()


textFrame = customtkinter.CTkFrame(tkGUI)
textFrame.pack(pady=20)

#add text to widget
myText = Text(textFrame, bg="#343638", width=65, border=1, fg="#d6d6d6", relief=FLAT, wrap=WORD, selectbackground= "#1f538d")
myText.grid(row=0, column=0)

#create Scroll bar for text widget
textScroll = customtkinter.CTkScrollbar(textFrame, command=myText.yview)
textScroll.grid(row=0, column=1, sticky="ns")

#add scrollbar to textbox
myText.configure(yscrollcommand=textScroll.set)

#add entry widget for questions

chatEntry = customtkinter.CTkEntry(tkGUI, placeholder_text="Ask a question!", width=535, height=50, border_width=1)
chatEntry.bind("<Return>", onEnter())
chatEntry.pack(pady=10)

#create button frame

buttonGrid = customtkinter.CTkFrame(tkGUI, fg_color="#242424")
buttonGrid.pack(pady=10)

#create submit button

submitButton = customtkinter.CTkButton(buttonGrid, text="Submit", command=speak)
submitButton.grid(row=0, column=0, padx=25)

#create clear button
clearButton = customtkinter.CTkButton(buttonGrid, text="Clear", command=clear)
clearButton.grid(row=0, column=1, padx=25)

#create key button
keyButton = customtkinter.CTkButton(buttonGrid, text="Secret  Key", command=key)
keyButton.grid(row=0, column=2, padx=25)

#add api key frame
apiFrame = customtkinter.CTkFrame(tkGUI, border_width=1)
apiFrame.pack(pady=20)

#add api widget
apiEntry = customtkinter.CTkEntry(apiFrame, placeholder_text="Enter API Key", width=350, height=30, border_width=1)
apiEntry.grid(row=0, column=0, padx=20, pady=20)

#create button frame
apiBtnFrame = customtkinter.CTkFrame(tkGUI, width= 350, height=40, border_width=1)
apiBtnFrame.pack(padx=5, pady=5)

#create save api key button
apiSaveButton = customtkinter.CTkButton(apiBtnFrame, text="Save Key", command=saveKey)
apiSaveButton.grid(row=0, column=1, padx=10, pady=10)

#create clear Key button
clearKeyBtn = customtkinter.CTkButton(apiBtnFrame, text="Clear Key", command=clearKey)
clearKeyBtn.grid(row=0, column=2, padx=10, pady=10)

tkGUI.mainloop()




