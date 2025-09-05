from library_item import LibraryItem
import json

library = {}  # create an empty library
def object_dict(obj):  # define a function to reverse object to dictionary
    return vars(obj)  # return obj to a dictionary using vars


def save_data_to_json(library, filename='data.json'):  # define a function to save library item into json
    library_data = {key: vars(item)
                    for key, item in library.items()}  # create a variable to store new data
    with open(filename, 'w') as jsonfile:  # open data json as write
        # convert dictionary in to json string and write into the data.json
        json.dump({"library_items": library_data}, jsonfile, indent=4)


def ipt_data():  # define a function to import database
    global library  # Assuming 'library' is a global variable
    try:  # try block
        with open('data.json', 'r') as jsonfile:  # read the content and assigned it to a variable name jsonfile
            data = json.load(jsonfile)  # read the content and parses it as a json object
    except FileNotFoundError:  # catch the error when data.json is not found
        data = {"library_items": {}}  # assign an empty dictionary

    # start a loop to iterate over the key-value pairs in dictionary
    for key, item_data in data["library_items"].items():
        # create an instance of LibraryItem class
        library[key] = LibraryItem(item_data["name"], item_data["director"], item_data["rating"])

    try:
        with open('data.json', 'r') as jsonfile:  # open as read mode
            data = json.load(jsonfile)  # read and parse it as a json object to a variable name data
            # get the value associated with the key or return empty dictionary if key not exist
            library_data = data.get("library_items", {})
            # create new variable name library
            library = {key: LibraryItem(**item) for key, item in library_data.items()}
    except FileNotFoundError:  # catch the error
        library = {}  # set an empty value when file corrupted or missing

    # open the library.json as write and assign it to variable name jsonfile
    with open('library.json', 'w') as jsonfile:
        # convert dictionary in to json string and write into the library.json
        json.dump({"library_items": library}, jsonfile, indent=4, default=object_dict)

    return library  # return the library


def get_new_video(name, director, rating):
    for key, item in library.items():  # check for duplicate
        if item.name == name and item.director == director:  # if video added is already in the playlist
            return None
    key = f"0{len(library) + 1}"  # format the key value based on the length of library
    library[key] = LibraryItem(name, director, rating)  # format how the value is taken by the library
    return key  # return the key


def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return
