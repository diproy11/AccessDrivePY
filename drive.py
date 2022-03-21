import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from tkinter import *
from tkinter import filedialog


gauth = GoogleAuth()
drive = GoogleDrive(gauth)


folder_path = '19mBXIWIwuYQvkRLTS0Zhz_C5K1_jriEe'
dir = "/Users/musubimanagement/Desktop/Resume"


#Upload File
def openFile():
    #file_type= {("csv files",".csv"),("Excel files",".xlsx"),("Documents",".docx"),("Documents",".doc"),("jpeg files",".jpg"),("png files",".png"),("all files","*.*")}
    global filepath
    filepath = filedialog.askopenfilename(multiple = True)
    
    if(filepath):
        for file in filepath:
            name_file = os.path.basename(file)
            file_up = drive.CreateFile({'parents':[{'id':folder_path}],'title':name_file})
            file_up.SetContentFile(file)
            file_up.Upload()
            exit()
    else:
        exit()
    
        
        
# window = Tk()
# button = Button(text = "Open", command=openFile,)
# button.pack()
# window.mainloop()



#Creating file on drive
def creating_file():
    create_file = input("")
    input_data = input("")
    file_d = drive.CreateFile({'parents':[{'id':folder_path}],'title':create_file})
    file_d.SetContentString(input_data)
    file_d.Upload()



# #UPLOADING ALL FILES ON DRIVE
# def upload_file():
#     for file in os.listdir(dir):
#         file_dir_path= os.path.join(dir,file)
#         print(file_dir_path)
#         file_up = drive.CreateFile({'parents':[{'id':folder_path,'title':file}]})
#         file_up.SetContentFile(file_dir_path)
#         file_up.Upload()


#LIST ALL FILE
def getList():
    file_list = drive.ListFile({'q' : f"'{folder_path}' in parents and trashed=false"}).GetList()

    for file in file_list:
        print(file['title'])
