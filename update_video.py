import tkinter as tk  # import tkinter a module for creating GUIs
import tkinter.scrolledtext as tkst  # import a scroll bar

import font_manager as fonts  # import the font from the font_manager
import video_library as lib  # import the video_library
from video_library import ipt_data, library, save_data_to_json


def set_text(text_area, content):  # a function to set the text of the text area
    text_area.delete("1.0", tk.END)  # delete the existing text from the previous etc
    text_area.insert(1.0, content)  # insert the content when the function is call

def add_zero(inp):
    for i in inp:
        if "0" in i:
            return inp
        else:
            zero_added = inp.zfill(len(inp) + 1)
            return zero_added

class UpdateVideos:  # create a class to for CheckVideos
    def __init__(self, window):  # define the constructor
        window.geometry("750x350")  # set the window size
        window.title("Update Videos")  # set the title of the window

        list_videos_btn = tk.Button(window, text="List All Videos",
                                    command=self.list_videos_clicked)  # Create the button to list all videos
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)  # set the position of the button

        enter_lbl = tk.Label(window, text="Enter Video Number")  # Create the label
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  # set the position
        # label new rating
        new_rating_lbl = tk.Label(window, text="Enter New Rating")
        new_rating_lbl.grid(row=1, column=3, pady=100, sticky="N")

        # add new rating
        self.new_rating = tk.Entry(window, width=3, )
        self.new_rating.grid(row=1, column=3, sticky="N", pady=130)
        # button takes new rating
        add_new_rating_btn = tk.Button(window, text="Add New Rating", command=self.update_video)
        add_new_rating_btn.grid(row=1, column=3, sticky="N", pady=160)

        self.input_txt = tk.Entry(window, width=3)  # Create the input text to enter the video number
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)  # set the position

        check_video_btn = tk.Button(window, text="Check Video",
                                    command=self.check_video_clicked)  # Create the button to check video
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)  # set the position

        self.list_txt = tkst.ScrolledText(window, width=50, height=12,
                                          wrap="none")  # Create a scroll text widget to display all videos
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="NW", padx=10,
                           pady=10)  # set the position of the scroll text

        self.video_txt = tk.Text(window, width=24, height=4,
                                 wrap="none")  # Create a text widget to show the detail of a video
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)  # Set the position of the text widget

        self.status_lbl = tk.Label(window, text="",
                                   font=("Helvetica", 10))  # Create a label to display the announcement of GUIs
        self.status_lbl.grid(row=1, column=0, columnspan=4, sticky="SW", padx=10,
                             pady=90)  # Set the position of the label
        self.refresh_list()

    def check_video_clicked(self):  # define a method where the check video button is clicked
        key = self.input_txt.get()  # get the user input widget
        key = str(add_zero(key))
        name = lib.get_name(key)  # get the name of the video from the library
        try:  # try block
            if key.isalpha():  # if input is alphabetic
                raise ValueError  # raise error
        except ValueError:  # handling the error
            self.status_lbl.configure(text="Please enter a number from the list of videos!")
        else:
            if name is not None:  # This mean that the video exists
                director = lib.get_director(key)  # Get the director of the video
                rating = lib.get_rating(key)  # Get the rating of the video
                play_count = lib.get_play_count(key)  # Get the play count of the video from the library using key
                video_details = (f"{name}\n"
                                 f"{director}\n"
                                 f"rating: {rating}\n"
                                 f"plays: {play_count}")  # format the video
                # detail as a string
                set_text(self.video_txt,
                         video_details)  # set the text of the status label to message when the button is clicked
            else:
                set_text(self.video_txt,
                         f"Video {key} not found")  # set the text in case of the input is an unknown video
            self.status_lbl.configure(
                text="Check Video button was clicked!")  # set the text to announce when the check video button is click

    def update_video(self):
        global library
        key = self.input_txt.get()  # get the input text
        key = str(add_zero(key))
        name = lib.get_name(key)  # get the name from the entry widget
        play_count = lib.get_play_count(key)  # get the rating from the entry widget
        director = lib.get_director(key)  # get the director from the entry widget
        new_rating = self.new_rating.get()  # get new rating

        if not new_rating or not key:  # handle the error when new rating and video number is not entered
            self.status_lbl.configure(text="Invalid input! Please enter a new rating and a correct video number")
        else:
            try:  # handle error when input number is an alpha
                if key.isalpha() or key.isalnum():
                    raise ValueError
            except ValueError:
                self.status_lbl.configure(
                    text="Invalid video number! Please enter a number from the list of videos not a string!")

            try:  # handle error when rating is not from 1 to 5
                new_rating = int(new_rating)
                if new_rating <= 0 or new_rating > 5:  # check if the rating is valid
                    raise ValueError  # raise an error
            except ValueError:  # handle the value error
                self.status_lbl.configure(
                    text="Invalid rating! Please enter a number from 1 to 5.")  # update the status label
            except Exception as e:  # handle any other exception
                self.status_lbl.configure(text=f"Error: {e}")  # update the status label

            else:
                if name:  # if name is not None
                    new_rating = int(new_rating)  # converse the rating into integer
                    lib.set_rating(key, new_rating)  # set the new rating into the library item
                    update_rating = lib.get_rating(key)  # store the new rating

                    # variable to store the text
                    video_details = (f"{name}\n"
                                     f"{director}\n"
                                     f"rating: {update_rating}\n"
                                     f"plays: {play_count}")
                    save_data_to_json(library)  # call the save function
                    set_text(self.video_txt,
                             video_details)  # set the text widget to display the new detail of the video
                    self.status_lbl.configure(
                        text="New rating is added")  # set the label to announce when new rating is added
                    self.refresh_list()

    def list_videos_clicked(self):  # define the function to list the
        video_list = lib.list_all()  # Get the video list in the video_library
        set_text(self.list_txt, video_list)  # set the text of the list text widget to the video list
        self.status_lbl.configure(
            text="List Videos button was clicked!")  # set the text when the list video button is clicked

    def refresh_list(self):  # define a function to refresh the playlist
        set_text(self.list_txt, lib.list_all())  # refresh playlist


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    fonts.configure()  # configure the fonts
    library = ipt_data()
    UpdateVideos(window)  # open the CheckVideo GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc
