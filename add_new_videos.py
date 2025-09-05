from tkinter import *
import tkinter.scrolledtext as st  # import a scroll bar

from video_library import ipt_data, library, save_data_to_json
import video_library as lib  # import the video_library
import font_manager as fonts  # import the font from the font_manager


def set_text(text_area, content):  # a function to set the text of the text area
    text_area.delete("1.0", END)  # delete the existing text from the previous etc
    text_area.insert(1.0, content)  # insert the content when the function is call


class AddNewVideos:
    def __init__(self, window):  # define the constructor
        window.geometry("830x350")  # set the window size
        window.title("Add New Videos")  # set the title of the window

        #   add new video button
        update_video_button = Button(window, text="Add New Video", command=self.add_video_clicked)
        update_video_button.grid(row=1, column=3, sticky="SE", padx=10, pady=10)

        #   input new name
        input_name_lbl = Label(window, text="Name:", font=("Helvetica", 10))
        input_name_lbl.grid(row=1, column=2, sticky="N", padx=10, pady=5)
        self.input_name = Entry(window, width=20)
        self.input_name.grid(row=1, column=3, sticky="NW", padx=0, pady=5)

        #   input new director
        input_director_lbl = Label(window, text="Director:", font=("Helvetica", 10))
        input_director_lbl.grid(row=1, column=2, sticky="N", padx=10, pady=50)
        self.input_director = Entry(window, width=20)
        self.input_director.grid(row=1, column=3, sticky="NW", padx=0, pady=50)

        # input new rating
        input_rating_lbl = Label(window, text="Rating(1 to 5):", font=("Helvetica", 10))
        input_rating_lbl.grid(row=1, column=2, sticky="N", padx=10, pady=95)
        self.input_rating = Entry(window, width=20)
        self.input_rating.grid(row=1, column=3, sticky="NW", padx=0, pady=95)

        list_videos_btn = Button(window, text="List All Videos",
                                 command=self.list_videos_clicked)  # Create the button to list all videos
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)  # set the position of the button

        self.list_txt = st.ScrolledText(window, width=50, height=12,
                                        wrap="none")  # Create a scroll text widget to display all videos
        self.list_txt.grid(row=1, column=0, columnspan=2, sticky="W", padx=10, pady=10)

        self.status1_lbl = Label(window, text="",
                                 font=("Helvetica", 10))  # Create a label to display the announcement of GUIs
        self.status1_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)
        self.refresh_list()

    def add_video_clicked(self):  # define the function to add a new video
        global library
        name = self.input_name.get()  # get the name from the entry widget
        director = self.input_director.get()  # get the director from the entry widget
        rating = self.input_rating.get()  # get the rating from the entry widget

        if not name and not director and not rating:  # handle the error when the value is not enter
            self.status1_lbl.configure(text="Please enter name, director, rating of the video.")
        elif not name:
            self.status1_lbl.configure(text="Please enter name of the video.")
        elif not director:
            self.status1_lbl.configure(text="Please enter director of the video.")
        elif not rating:
            self.status1_lbl.configure(text="Please enter rating from 1 to 5 of the video.")
        else:
            try:
                rating = int(rating)  # convert the rating to an integer
                if rating <= 0 or rating > 5:  # check if the rating is valid
                    raise ValueError  # raise an error
            except ValueError:  # handle the value error
                self.status1_lbl.configure(
                    text="Invalid rating! Please enter a number from 1 to 5.")  # update the status label
            except Exception as e:  # handle any other exception
                self.status1_lbl.configure(text=f"Error: {e}")  # update the status label

            else:
                key = lib.get_new_video(name, director, rating)  # add the video to the library and get the key
                self.status1_lbl.configure(text=f"Video {key} added successfully!")  # update the status label "
                self.refresh_list()  # refresh the video list
                save_data_to_json(library)  # call the save function
                try:  # handle the error when the video is already added
                    if key is None:
                        raise EOFError
                except EOFError:
                    self.status1_lbl.configure(text="This video is already added")

    def list_videos_clicked(self):  # define the function to list the
        video_list = lib.list_all()  # Get the video list in the video_library
        set_text(self.list_txt, video_list)  # set the text of the list text widget to the video list
        self.status1_lbl.configure(text="List Videos button was clicked!")

    def refresh_list(self):
        set_text(self.list_txt, lib.list_all())


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = Tk()  # create a TK object
    ipt_data()
    fonts.configure()  # configure the fonts
    AddNewVideos(window)  # open the CheckVideo GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc
