import tkinter as tk
from tkinter import filedialog, Button, Label, Entry
from tkinter.ttk import Combobox
from typing import TextIO, Any, List, Union, Tuple, Literal
from PIL import Image, ImageDraw, ImageFont
from tkinter import ttk
import random
import datetime as DT
import os


root = tk.Tk()
file: TextIO
with open ('addresses.txt', 'r', encoding='utf-8') as file:
    addresses: list[str] = file.read().split('\n')
    

def open_files()->str:
    """
    searching for images in chosen directory with jpeg, jpg extensions
    """
    global image_paths
    image_paths = filedialog.askopenfilenames(title = "Select image",filetypes = (("jpeg files",".jpg"),("jpeg files",".jpeg"),("all files",".*")))
    return image_paths


def add_text_to_images() ->None :
    """
    define and adding selected address to photo
    """
    nam: int = 0
    # Get the text input by the user
    value: str = address_combo.get()
    # date_time = date_time_entry.get()

    ##    # Concatenate the address and date_time into one string
    ##    text = date_time + ":" + sec2 +"\n" + value + "\n"  + " Юго-Западный административный округ" + "\n" "Москва"

    # Create an ImageDraw object
    for image_path in image_paths:
        # now: DT = DT.datetime.now(DT.timezone.utc).astimezone()
        # date_time = now
        # time_format: str = "%Y-%m-%d %H:%M:%S"
        # sec: int = random.randint(1, 59)
        # if sec < 10:
        #     sec2 = '0' + str(sec)
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        # text = f"{now:{time_format}}" + "\n" + value + "\n" + " Юго-Западный административный округ" + "\n" "Москва"  # +  ":" + sec2

        fsz: float = image.width / 50 + image.height / 64
        # Define the font and size
        font = ImageFont.truetype("arial.ttf", int(fsz))

        # Get the size of the text
        textwidth, textheight = draw.textsize(text, font)

        # Set the position of the text
        x = image.width - textwidth - 10
        y = image.height - textheight - 10
        x1 = image.width - textwidth - 10.2
        y1 = image.height - textheight - 10.2

        # Add the text to the image
        draw.text((x1, y1), text, font=font, fill=(0, 0, 0), align="right")
        draw.text((x, y), text, font=font, fill=(255, 255, 255), align="right")

        # Save the image with the text added
        # save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        nam += 1
        image.save(f"{value}.jpg")  # f"C:/testpy1/res/
        # image.save(save_path,fp={nam})
        # delt = image_path
        # os.remove(delt)


# Создаем объект Combobox
def suggest_address(event: Any) -> None:
    """
    creates auto-dropping list of suggested addresses out of combobox field
    """
    value: Any = event.widget.get()
    if value == '':
        address_combo['values'] = addresses
    else:
        data: list[str] = []
        item: str
        for item in addresses:
            if value.lower() in item.lower():
                data.append(item)
        address_combo['values'] = data


def time_turn():
    global text
    if var.get() == 0:
        now = DT.datetime.now(DT.timezone.utc).astimezone()
        time_format: str = "%Y-%m-%d %H:%M:%S"
        value: str = address_combo.get()
        text = f"{now:{time_format}}" + "\n" + value + "\n" + " Юго-Западный административный округ" + "\n" "Москва"
    else:
        date_time_entry.pack()
        date_time = date_time_entry.get()
        sec: int = random.randint(1, 59)
        value: str = address_combo.get()
        sec2: str = str(sec)
        if sec < 10:
            sec2 = '0' + str(sec)
        text = date_time + ":" + sec2 + "\n" + value + "\n" + " Юго-Западный административный округ" + "\n" "Москва"
    return text


var: Any = tk.IntVar()  # construct an integer variable
var.set(0)

auto = tk.Radiobutton(text="Вручную", variable=var, value=1,command=time_turn)
manual = tk.Radiobutton(text="Текущее время", variable=var, value=0,command=time_turn)
# button: Button = tk.Button(text="Изменить", command=time_turn)


open_file_button: Button = tk.Button(root, text="Открыть картинки", command=lambda: open_files())
open_file_button.pack()

date_time_label: Label = tk.Label(root, text="Дата и время:")
date_time_label.pack()

##Create an entry widget for the date and time input
date_time_entry: Entry = tk.Entry(root)
auto.pack()
manual.pack()
# date_time_entry.pack()
##address_var = tk.StringVar()

##Create a label for the address input
address_label: Label = tk.Label(root, text="Адрес: (Начните вводить значение)")
address_label.pack()

address_combo: Combobox = ttk.Combobox(root, value=addresses, width=100)# value=addresses
address_combo.bind('<KeyRelease>', suggest_address)
address_combo.pack()

root.geometry( '600x200' )
root.title("Добавить геотег на фото")

##Create a button to add text to images
add_text_button = tk.Button(root, text="Поставить геотег", command=lambda: add_text_to_images())
add_text_button.pack()


##Create an entry widget for the address input
##address_entry = tk.Entry(root)
##address_entry.pack()

root.mainloop()

