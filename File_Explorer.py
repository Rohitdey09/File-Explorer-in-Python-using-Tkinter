# Python program to create
# a file explorer in Tkinter
  
# import all components
# from the tkinter library
from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import os
import shutil  


# Creating the backend functions for python file explorer project
def open_file():
   file = fd.askopenfilename(title='Choose a file of any type', filetypes=[("All files", "*.*")])

   os.startfile(os.path.abspath(file))


def copy_file():
   file_to_copy = fd.askopenfilename(title='Choose a file to copy', filetypes=[("All files", "*.*")])
   dir_to_copy_to = fd.askdirectory(title="In which folder to copy to?")

   try:
       shutil.copy(file_to_copy, dir_to_copy_to)
       mb.showinfo(title='File copied!', message='Your desired file has been copied to your desired location')
   except:
       mb.showerror(title='Error!', message='We were unable to copy your file to the desired location. Please try again')


def delete_file():
   file = fd.askopenfilename(title='Choose a file to delete', filetypes=[("All files", "*.*")])

   os.remove(os.path.abspath(file))

   mb.showinfo(title='File deleted', message='Your desired file has been deleted')

def rename_file():
   file = fd.askopenfilename(title='Choose a file to rename', filetypes=[("All files", "*.*")])
   print(file)
   path1 = os.path.dirname(file)
   extension=os.path.splitext(file)[1]
   print("Enter new name for the chosen file")
   newName=input()
   path = os.path.join(path1, newName+extension)
   print(path)
   os.rename(file,path) 
   mb.showinfo(title="File Renamed", message='Your desired file has been renamed')


def open_folder():
   folder = fd.askdirectory(title="Select Folder to open")
   os.startfile(folder)


def delete_folder():
   folder_to_delete = fd.askdirectory(title='Choose a folder to delete')
   os.rmdir(folder_to_delete)
   mb.showinfo("Folder Deleted", "Your desired folder has been deleted")


def move_folder():
   folder_to_move = fd.askdirectory(title='Select the folder you want to move')
   mb.showinfo(message='You just selected the folder to move, now please select the desired destination where you want to move the folder to')
   destination = fd.askdirectory(title='Where to move the folder to')

   try:
       shutil.move(folder_to_move, destination)
       mb.showinfo("Folder moved", 'Your desired folder has been moved to the location you wanted')
   except:
       mb.showerror('Error', 'We could not move your folder. Please make sure that the destination exists')


def list_files_in_folder():
   temp=""
   folderList = fd.askdirectory()
   sortlist=sorted(os.listdir(folderList))
   i=0
   print("Files in ", folderList, "folder are:")
   while(i<len(sortlist)):
       temp+=sortlist[i]+'\n'
       print(sortlist[i]+'\n')
       i+=1
   file=open("list.txt","w")
   file.write(temp)
   file.close()
   
button_font = ("Times New Roman", 12)
button_background = 'Grey'      
                                                                                                  
# Create the root window
window = Tk()
  
# Set window title
window.title('File Explorer')
  
# Set window size
window.geometry("250x400")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 140, height = 4,
                            fg = "blue")
  
      


  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
#label_file_explorer.grid(column = 1, row = 1)
  

  
#button_exit.grid(column = 1,row = 3)


# Creating and placing the components in the window
Label(window, text='File Manager using Tk', font=("Comic Sans MS", 15), wraplength=250).place(x=20, y=0)

Button(window, text='Open a file', width=20, font=button_font, bg=button_background, command=open_file).place(x=30, y=50)

Button(window, text='Copy a file', width=20, font=button_font, bg=button_background, command=copy_file).place(x=30, y=90)

Button(window, text='Rename a file', width=20, font=button_font, bg=button_background, command=rename_file).place(x=30, y=130)

Button(window, text='Delete a file', width=20, font=button_font, bg=button_background, command=delete_file).place(x=30, y=170)

Button(window, text='Open a folder', width=20, font=button_font, bg=button_background, command=open_folder).place(x=30, y=210)

Button(window, text='Delete a folder', width=20, font=button_font, bg=button_background, command=delete_folder).place(x=30, y=250)

Button(window, text='Move a folder', width=20, font=button_font, bg=button_background, command=move_folder).place(x=30, y=290)

Button(window, text='List all files in a folder', width=20, font=button_font, bg=button_background,
      command=list_files_in_folder).place(x=30, y=330)

Button(window,text = "Exit",width=20,command = exit).place(x=50,y=370)  

# Let the window wait for any events
window.update()
window.mainloop()
