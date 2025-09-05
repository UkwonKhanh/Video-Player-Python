import tkinter.scrolledtext as st  # import a scroll bar
from tkinter import *

import font_manager as fonts  # import the font from the font_manager
import video_library as lib  # import the video_library
from video_library import library, ipt_data, save_data_to_json  # import following function


def set_text(text_area, content):  # a function to set the text of the text area
    text_area.delete("1.0", END)  # delete the existing text from the previous etc
    text_area.insert(1.0, content)  # insert the content when the function is call

def add_zero(inp):
    for i in inp:
        if "0" in i:
            return inp
        else:
            zero_added = inp.zfill(len(inp) + 1)
            return zero_added

class CreateVideoList:
    def __init__(self, window):
        window.geometry("900x350")  # set the window size
        window.title("Create Video List")  # set the title of the window

        add_video_btn = Button(window, text="Add Video To Playlist",
                               command=self.add_video_clicked)  # Create the button to list all videos
        add_video_btn.grid(row=0, column=3, padx=10, pady=10)  # set the position of the button

        list_videos_btn = Button(window, text="List All Videos",
                                 command=self.list_videos_clicked)  # Create the button to list all videos
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)  # set the position of the button

        clear_play_list_btn = Button(window, text="Clear Playlist", command=self.clear_play_list_clicked)
        clear_play_list_btn.grid(row=2, column=3, padx=10, pady=5, sticky="E")

        play_playlist_btn = Button(window, text="Play", command=self.play_playlist_clicked)
        play_playlist_btn.grid(row=2, column=3, padx=3, pady=5)

        enter_lbl = Label(window, text="Enter Video Number")  # Create the label
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  # set the position

        self.input_txt = Entry(window, width=3)  # Create the input text to enter the video number
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)  # set the position

        self.list_txt = st.ScrolledText(window, width=50, height=12,
                                        wrap="none")  # Create a scroll text widget to display all videos
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10,
                           pady=10)  # set the position of the scroll text

        self.video_txt = st.ScrolledText(window, width=40, height=12,
                                         wrap="none")  # Create a text widget to show the detail of a video
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)  # Set the position of the text widget

        self.status_lbl = Label(window, text="",
                                font=("Helvetica", 10))  # Create a label to display the announcement of GUIs
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10,
                             pady=10)  # Set the position of the label
        self.refresh_list()
        self.row_counter = 0
        self.playlist = []

    def add_video_clicked(self):  # define the function to add a video to the playlist
        key = self.input_txt.get()
        key = str(add_zero(key)) # get the input text
        name = lib.get_name(key)
        director = lib.get_director(key)
        if not name:  # if the name is None
            self.status_lbl.configure(text=f"Invalid video number!")  # set the text when the video number is invalid
        else:  # if the name is not None
            self.playlist.append(name)  # append the name to the playlist
            self.row_counter += 1  # increment the row counter
            self.video_txt.insert(f"{self.row_counter}.0",
                                  f"{name} - {director}\n")  # insert the name to the video text widget
            self.status_lbl.configure(text=f"Added {name} to the playlist!")  # set the text when the video is added

    def play_playlist_clicked(self):  # define the function to play the playlist and update the play count
        global library  # import global library

        if self.playlist:  # if playlist is not None
            """loop through the play list and 
            increase the play count"""
            for video_name in self.playlist:
                key = None  # assign None because the key has no value
                for k, item in library.items():  # loop  through the item in the library
                    # if the name of item which is the key is equal to video nam in playlist
                    if item.name == video_name:
                        key = k  # match the 'key' to the corresponding key in the library
                        break  # break out of the loop
                if key:  # if key is not None
                    lib.increment_play_count(key)  # increment the play count

            save_data_to_json(library)  # save play count into json
            set_text(self.list_txt, lib.list_all())  # call the set text function

            self.status_lbl.configure(text="Playing the playlist")
        else:
            self.status_lbl.configure(text="The playlist is empty!")

    def list_videos_clicked(self):  # define the function to list the
        video_list = lib.list_all()  # Get the video list in the video_library
        set_text(self.list_txt, video_list)  # set the text of the list text widget to the video list
        self.status_lbl.configure(
            text="List Videos button was clicked!")  # set the text when the list video button is clicked

    def clear_play_list_clicked(self):  # define a function to clear the playlist
        self.playlist = []  # refresh playlist
        set_text(self.video_txt, "")  # set text
        self.status_lbl.configure(text="The playlist is cleared")  # set label

    def refresh_list(self):  # define a function to refresh the playlist
        set_text(self.list_txt, lib.list_all())  # refresh playlist


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = Tk()  # create a TK object
    ipt_data()
    fonts.configure()  # configure the fonts
    CreateVideoList(window)  # open the CheckVideo GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc
