import configparser
import os


config = configparser.ConfigParser()
config.read('./RNDPyTorch/config.conf')
#config.read("C:/sers/Xu/Documents/PythonScripts/RNDPyTorch/config.conf")

# ---------------------------------
default = 'DEFAULT'
# ---------------------------------
default_config = config[default]


