# import necessary libraries

from flask import Flask as f, render_template as rt, send_file as sf
import os
from kaggle_connect import kaggle_connect  as kc
import curses as cr

# wrapper function to run Kaggle connect using curses.
def run_kaggle():
    return cr.wrapper(kc) # kc is passed as a function, not as a pre-executed call.

# run function
kc = run_kaggle()