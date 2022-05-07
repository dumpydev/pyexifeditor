from exif import Image
import json
from colorama import *
init()
print(Fore.GREEN + "Welcome to the Exif Reader!")
print(Fore.YELLOW)
locationOfFile = input("Enter the location of the file: ")
config = input("Do you have a config? (y/n): ")

if config == "y" or " ":
    configlocation = input("Enter the location of the config: ")
    f = open(configlocation, "r")
    configasjson = json.load(f)
elif config == "n":
    print("Please create a config.")
    exit(1)


with open(locationOfFile, 'rb') as img_file:
    img = Image(img_file)

print("-----------------------------------------------------")
print("reading json...")
print(Fore.YELLOW)
print("copyright:" + img.copyright)
print("model:" + img.model)
print("make:" + img.make)
print("lens model:" + img.lens_model)
print("lens make:" + img.lens_make)
print("-----------------------------------------------------")


try:
    print(Fore.RED + "writing copyright as: " + configasjson["copyright"])
    img.copyright = configasjson["copyright"]
    print(Fore.RED + "writing make as: " + configasjson["make"])
    img.make = configasjson["make"]
    print(Fore.RED + "writing model as: " + configasjson["model"])
    img.model = configasjson["model"]
    print(Fore.RED + "writing lens model as: " + configasjson["lens_model"])
    img.lens_model = configasjson["lens_model"]
    print(Fore.RED + "writing lens make as: " + configasjson["lens_make"])
    img.lens_make = configasjson["lens_make"]
    print(Fore.RED + "writing focal length as: " +
          configasjson["focal_length"])
    img.focal_length = configasjson["focal_length"]
    print(Fore.RED + "writing f-stop as: " + configasjson["f_number"])
    img.f_number = configasjson["f_stop"]
    print(Fore.RED + "writing exposure time as: " +
          configasjson["exposure_time"])
    img.exposure_time = configasjson["exposure_time"]
    print(Fore.RED + "writing iso as: " + configasjson["iso"])
    img.iso_speed = configasjson["iso_speed"]
except:
    print("An Error Occured, Make sure JSON is valid!")


with open(locationOfFile, 'wb') as new_image_file:
    new_image_file.write(img.get_file())

with open(locationOfFile, 'rb') as img_file:
    new_img = Image(img_file)


print("-----------------------------------------------------")
print("reading NEW json...")
print(Fore.YELLOW)
print("copyright:" + new_img.copyright)
print("model:" + new_img.model)
print("make:" + new_img.make)
print("lens model:" + new_img.lens_model)
print("lens make:" + new_img.lens_make)
print("exposure time: " + str(new_img.exposure_time))
print("focal length: " + str(new_img.focal_length))
print("f-stop: " + str(new_img.f_number))
print("-----------------------------------------------------")

input("Press Enter to exit...")
exit(0)
