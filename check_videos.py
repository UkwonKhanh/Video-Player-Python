import tkinter as tk  # import tkinter a module for creating GUIs
import tkinter.scrolledtext as tkst  # import a scroll bar

from video_library import ipt_data, library  # import the
import video_library as lib  # import the video_library
import font_manager as fonts  # import the font from the font_manager


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


class CheckVideos:  # create a class to for CheckVideos
    def __init__(self, window):  # define the constructor
        window.geometry("950x370")  # set the window size
        window.title("Check Videos")  # set the title of the window

        list_videos_btn = tk.Button(window, text="List All Videos",
                                    command=self.list_videos_clicked)  # Create the button to list all videos
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)  # set the position of the button

        enter_lbl = tk.Label(window, text="Enter Video Number")  # Create the label
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  # set the position

        self.input_txt = tk.Entry(window, width=3)  # Create the input text to enter the video number
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)  # set the position

        check_video_btn = tk.Button(window, text="Check Video",
                                    command=self.check_video_clicked)  # Create the button to check video
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)  # set the position

        self.list_txt = tkst.ScrolledText(window, width=50, height=12,
                                          wrap="none")  # Create a scroll text widget to display all videos
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="NW", padx=10,
                           pady=10)  # set the position of the scroll text

        self.video_txt = tk.Text(window, width=45, height=10,
                                 wrap="none")  # Create a text widget to show the detail of a video
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)  # Set the position of the text widget

        #   input text for search string
        self.search_txt = tk.Entry(window, width=45)
        self.search_txt.grid(row=1, column=3, sticky="N", pady=208, padx=10)
        search_btn = tk.Button(window, text="Search", command=self.search)
        search_btn.grid(row=1, column=3, pady=250, sticky="N")

        self.status_lbl = tk.Label(window, text="",
                                   font=("Helvetica", 10))  # Create a label to display the announcement of GUIs
        self.status_lbl.grid(row=1, column=0, columnspan=2, sticky="WE", padx=10,
                             pady=250)  # Set the position of the label

        self.refresh_list()  # call the method to list all videos when GUIS is initialised

    def check_video_clicked(self):  # define a method where the check video button is clicked
        key = self.input_txt.get()  # get the user input widget
        key = str(add_zero(key))
        name = lib.get_name(key)  # get the name of the video from the library

        try:
            if key.isalpha():  # if key is alphabetical
                raise ValueError  # raise the error
        except ValueError:  # handle the error
            self.status_lbl.configure(text="Please enter a number from the list of videos!")  # announce the label

        else:
            if name is not None:  # This mean that the video exists
                director = lib.get_director(key)  # Get the director of the video
                rating = lib.get_rating(key)  # Get the rating of the video
                play_count = lib.get_play_count(key)  # Get the play count of the video from the library using key
                video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"  # format the video
                # detail as a string
                set_text(self.video_txt,
                         video_details)  # set the text of the status label to message when the button is clicked
            else:
                set_text(self.video_txt,
                         f"Video {key} not found")  # set the text in case of the input is an unknown video
            self.status_lbl.configure(
                text="Check Video button was clicked!")  # set the text to announce when the check video button
            # is clicked

    def search(self):  # define a function to search
        global library
        key = self.search_txt.get().lower()  # get the output
        out = ""  # define output

        if key == "":
            set_text(self.video_txt, "Please enter a search string!")
        elif key == key:  # if key is not empty
            set_text(self.video_txt, f"There's no videos has '{key}'")  # set text to announce
            self.status_lbl.configure(text="Not Found!")  # set the label to announce

        else:  # if key is not empty
            for item in library:  # loop through the key
                search_name = library[item].name.lower()
                search_director = library[item].director.lower()
                if key in search_name or key in search_director:  # if the value of the key
                    out += f"{library[item].info()}\n"  # set the output in the loop

            if out:  # check for output not an empty string
                set_text(self.video_txt, out)  # set text to display the output
                self.status_lbl.configure(text="Search button clicked")  # set the label to announce the action search

    def list_videos_clicked(self):  # define the function to list the
        video_list = lib.list_all()  # Get the video list in the video_library
        set_text(self.list_txt, video_list)  # set the text of the list text widget to the video list
        self.status_lbl.configure(
            text="List Videos button was clicked!")  # set the text when the list video button is clicked

    def refresh_list(self):  # define a function to refresh the playlist
        set_text(self.list_txt, lib.list_all())  # refresh playlist


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    ipt_data()  # call the data
    fonts.configure()  # configure the fonts
    CheckVideos(window)  # open the CheckVideo GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc
