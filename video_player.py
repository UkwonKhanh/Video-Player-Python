import tkinter as tk

import font_manager as fonts
from check_videos import CheckVideos
from create_video_list import CreateVideoList
from add_new_videos import AddNewVideos
from update_video import UpdateVideos
from video_library import ipt_data, save_data_to_json


def check_videos_clicked():  # define the function
    status_lbl.configure(text="Check Videos button was clicked!")  # configure status label
    CheckVideos(tk.Toplevel(window))  # create new window associated with the main one


def create_video_list_clicked():  # define the function
    status_lbl.configure(text="Create Video List button was clicked!")  # configure status label
    CreateVideoList(tk.Toplevel(window))  # create new window associated with the main one


def update_videos_clicked():  # define the function
    status_lbl.configure(text="Update Videos button was clicked!")  # configure status label
    UpdateVideos(tk.Toplevel(window))  # create new window associated with the main one


def add_new_videos_clicked():  # define the function
    status_lbl.configure(text="Add New Videos button was clicked")  # configure status label
    AddNewVideos(tk.Toplevel(window))  # create new window associated with the main one


def save():  # define the function
    save_data_to_json(library)  # call the save function
    status_lbl.configure(text="Data Saved")  # configure status label


def exit():  # define the function
    save_data_to_json(library)  # call the save function
    window.destroy()  # destroy the main window


window = tk.Tk()
window.geometry("520x250")
window.title("Video Player")

library = ipt_data()  # variable to store data imported from file

fonts.configure()  # import fonts
# define the label
header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# check video button
check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)
# add new video button
add_new_videos_btn = tk.Button(window, text="Add New Videos", command=add_new_videos_clicked)
add_new_videos_btn.grid(row=2, column=1)
# create video list button
create_video_list_btn = tk.Button(window, text="Create Video List", command=create_video_list_clicked)
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)
# update video button
update_videos_btn = tk.Button(window, text="Update Videos", command=update_videos_clicked)
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)
# save button
save_btn = tk.Button(window, text="Save", command=save)
save_btn.grid(row=3, column=1, padx=10, pady=10)
# exit button
exit_btn = tk.Button(window, text="Exit", command=exit, background="red")
exit_btn.grid(row=3, column=2, padx=10, pady=10)
# create a label widget
status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
