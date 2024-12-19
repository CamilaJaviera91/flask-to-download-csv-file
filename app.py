# import necessary libraries

from flask import Flask as f, render_template as rt, send_file as sf
import os
from kaggle_connect import kaggle_connect  as kc