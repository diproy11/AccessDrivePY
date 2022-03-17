import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder_path = '1-0lhOBBZST4UrQFmChYSaQnc4T-ICy8u'
dir = "/Users/musubimanagement/Desktop/Resume"


#Creating file on drive
def creating_file():
    create_file = input("")
    input_data = input("")
    file_d = drive.CreateFile({'parents':[{'id':folder_path}],'title':create_file})
    file_d.SetContentString(input_data)
    file_d.Upload()



#UPLOADING FILE ON DRIVE
def upload_file():
    for file in os.listdir(dir):
        file_dir_path= os.path.join(dir,file)
        print(file_dir_path)
        file_up = drive.CreateFile({'parents':[{'id':folder_path,'title':file}]})
        file_up.SetContentFile(file_dir_path)
        file_up.Upload()


#LIST ALL FILE
def getList():
    file_list = drive.ListFile({'q' : f"'{folder_path}' in parents and trashed=false"}).GetList()

    for file in file_list:
        print(file['title'])

