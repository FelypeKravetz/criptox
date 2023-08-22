import base64
import urllib.parse
import html
import unicodedata
import quopri
from tkinter import *

def process_text():
    input_text = input_text_box.get("1.0", "end-1c")
    selected_option = option_var.get()

    if selected_option == "Base64 Encode":
        encoded_text = base64.b64encode(input_text.encode()).decode()
        result_text_box.delete("1.0", "end")
        result_text_box.insert("end", encoded_text)
    elif selected_option == "Base64 Decode":
        try:
            decoded_text = base64.b64decode(input_text.encode()).decode()
            result_text_box.delete("1.0", "end")
            result_text_box.insert("end", decoded_text)
        except base64.binascii.Error:
            result_text_box.delete("1.0", "end")
            result_text_box.insert("end", "Error: Invalid Base64 input.")
    elif selected_option == "URL Encode":
        encoded_text = urllib.parse.quote(input_text)
        result_text_box.delete("1.0", "end")
        result_text_box.insert("end", encoded_text)
    elif selected_option == "URL Decode":
        decoded_text = urllib.parse.unquote(input_text)
        result_text_box.delete("1.0", "end")
        result_text_box.insert("end", decoded_text)
    elif selected_option == "HTML Entity Encode":
        encoded_text = html.escape(input_text)
        result_text_box.delete("1.0", "end")
        result_text_box.insert("end", encoded_text)
    elif selected_option == "HTML Entity Decode":
        decoded_text = html.unescape(input_text)
        result_text_box.delete("1.0", "end")
        result_text_box.insert("end", decoded_text)
    elif selected_option == "Unicode Encode":
        encoded_text = " ".join([f"U+{ord(char):04X}" for char in input_text])
        result_text_box.delete("1.0", "end")
        result_text_box.insert("end", encoded_text)
    elif selected_option == "Unicode Decode":
        try:
            decoded_text = ""
            hex_chars = input_text.split()
            for hex_char in hex_chars:
                decoded_text += chr(int(hex_char[2:], 16))
            result_text_box.delete("1.0", "end")
            result_text_box.insert("end", decoded_text)
        except ValueError:
            result_text_box.delete("1.0", "end")
            result_text_box.insert("end", "Error: Invalid Unicode input.")
    elif selected_option == "Quoted-Printable Encode":
        encoded_bytes = quopri.encodestring(input_text.encode())
        encoded_text = encoded_bytes.decode()
        result_text_box.delete("1.0", "end")
        result_text_box.insert("end", encoded_text)
    elif selected_option == "Quoted-Printable Decode":
        try:
            decoded_bytes = quopri.decodestring(input_text.encode())
            decoded_text = decoded_bytes.decode()
            result_text_box.delete("1.0", "end")
            result_text_box.insert("end", decoded_text)
        except quopri.Error:
            result_text_box.delete("1.0", "end")
            result_text_box.insert("end", "Error: Invalid Quoted-Printable input.")

def exit_app():
    root.destroy()

root = Tk()
root.title("Text Encoder/Decoder")

option_var = StringVar()
options = ["Base64 Encode", "Base64 Decode", "URL Encode", "URL Decode", "HTML Entity Encode", "HTML Entity Decode", "Unicode Encode", "Unicode Decode", "Quoted-Printable Encode", "Quoted-Printable Decode"]
option_var.set(options[0])

input_label = Label(root, text="Enter Text:")
input_label.pack()

input_text_box = Text(root, height=5, width=40)
input_text_box.pack()

options_menu = OptionMenu(root, option_var, *options)
options_menu.pack()

process_button = Button(root, text="Process", command=process_text)
process_button.pack()

result_label = Label(root, text="Result:")
result_label.pack()

result_text_box = Text(root, height=5, width=40)
result_text_box.pack()

exit_button = Button(root, text="Exit", command=exit_app)
exit_button.pack()

root.mainloop()
