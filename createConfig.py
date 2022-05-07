import json
from colorama import *
init()
print(Fore.GREEN + "Welcome to the Exif Reader!")


default = { 
    "copyright": "(c) 2022 Andrew Wang", 
    "make": "Canon", 
    "model": "Canon EOS 40D",
    "lens_make": "Canon",
    "lens_model": "Canon EF-S 17-85mm f/4-5.6 IS USM",
    "focal_length": "17",
    "exposure_time": "1/60",
    "f_stop": "4",
    "iso_speed": "400"
}
print("Welcome to the config creator!")
print("Please enter the following information:")
print("-----------------------------------------------------")
default['copyright'] = input("copyright: ")
default['make'] = input("make: ")
default['model'] = input("model: ")
default['lens_make'] = input("lens make: ")
default['lens_model'] = input("lens model: ")
default['focal_length'] = input("focal length: ")
default['exposure_time'] = input("exposure time: ")
default['f_stop'] = input("f-stop: ")
default['iso_speed'] = input("iso: ")
print("-----------------------------------------------------")
print("Thank you for your input!")
print("-----------------------------------------------------")
# write default to json file
fileName = input("Please enter the name of the file: ")
with open(fileName, 'w') as f:
    json.dump(default, f)
print("-----------------------------------------------------")
print(fileName+" has been created!")
input("Press Enter to exit...")
exit(0)