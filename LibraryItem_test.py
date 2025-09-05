from library_item import LibraryItem


def test_library_item(capsys):  # Define a function to test the LibraryItem class
    item = LibraryItem("Oppenheimer", "Christopher Nolan", 5, 0)  # Create an instance of LibraryItem

    assert item.name == "Oppenheimer"  # Assert the name attribute
    assert item.director == "Christopher Nolan"  # Assert the director attribute
    assert item.rating == 5  # Assert the rating attribute
    assert item.play_count == 0  # Assert the play_count attribute

    with capsys.disabled():  # use the disabled to capture the output
        print()
        print(f" Tested {item.__class__.__name__} successfully")  # print a message to indicate the test was successful


def test_info(capsys):
    item = LibraryItem("Oppenheimer", "Christopher Nolan", 5, 0)  # Create an instance of LibraryItem
    sample_info = "Oppenheimer - Christopher Nolan ***** - Views: 0"  # define a sample string of the output
    assert item.info() == sample_info  # assert that the info method of the item return the same as sample string

    with capsys.disabled():  # use the disabled to capture the output
        print()
        print(f" Tested {item.__class__.__name__} successfully")  # print a message to indicate the test was successful


def test_stars(capsys):
    item = LibraryItem("Oppenheimer", "Christopher Nolan", 5, 0)  # Create an instance of LibraryItem
    sample_stars = "*****"  # define a sample string of the output
    assert item.stars() == sample_stars  # assert that the info method of the item return the same as sample string

    with capsys.disabled():  # use the disabled to capture the output
        print()
        print(f" Tested {item.__class__.__name__} successfully")
