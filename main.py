# Import necessary classes from tkinter and ttk.
# `*` imports all main classes and functions from tkinter.
# `Progressbar` is a themed widget from ttk used to display task progress.
from tkinter import *
from tkinter.ttk import Progressbar

# ! Functionality

def start():
    """
    Main function that starts the download simulation.
    This function defines an internal recursive function to update the progress.
    """
    def update_progress(download=0):
        """
        Internal function that simulates the progress of a download.
        This function is called recursively to update the progress bar and dynamic texts.

        Parameters:
        - download (float): Amount downloaded so far (in GB). Initially 0.
        """
        # Define the total download size and speed.
        GB = 10  # Total download size in GB.
        speed = 1  # Download speed in GB per second.

        # Check if the downloaded amount is less than the total size.
        if download < GB:
            # Increment the progress bar value.
            # The formula `(speed / GB) * 100` calculates the percentage corresponding to the increment.
            bar['value'] += (speed / GB) * 100

            # Update the downloaded amount.
            download += speed

            # Update the dynamic text showing the download percentage.
            percentage.set(str(int((download / GB) * 100)) + '%')

            # Update the dynamic text showing the download status.
            com.set(str(download) + '/' + str(GB) + ' GB complete')

            # Force immediate GUI update.
            window.update_idletasks()

            # Schedule the next recursive call after 1000 ms (1 second).
            window.after(1000, lambda: update_progress(download))

    # Start the download simulation by calling the internal function.
    update_progress()

# ! Graphic Interface

# Create the main application window.
window = Tk()  # Initializes an instance of the Tk class, representing the main window.
window.title('Simple Progress Bar') # Title.

# Dynamic variables for text in the interface.
# `StringVar` is a special tkinter class that allows binding variables to dynamic widgets.
percentage = StringVar()  # Variable to store the download percentage (e.g., "20%").
com = StringVar()  # Variable to store the download status (e.g., "2/10 GB complete").

# Create a horizontal progress bar.
bar = Progressbar(window, orient='horizontal', length=350)
# Configuration:
# - `orient='horizontal'`: Defines that the progress bar will be horizontal.
# - `length=350`: Sets the width of the progress bar in pixels.
bar.pack(padx=20, pady=20)  # Place the progress bar in the window with external margins.

# Create labels to display the percentage and download status.
percentage_text = Label(window, textvariable=percentage)
percentage_text.pack()  # Place the label in the window.
com_text = Label(window, textvariable=com)
com_text.pack()  # Place the label in the window.

# Create a button to start the download simulation.
download_button = Button(window, text='Download', command=start)
# Configuration:
# - `text='Download'`: Visible text on the button.
# - `command=start`: Function executed when the button is clicked.
download_button.pack()  # Place the button in the window.

# Start the main application loop.
window.mainloop()