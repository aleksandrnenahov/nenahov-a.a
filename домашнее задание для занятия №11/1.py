import json
import requests
from tkinter import*

def buttonAction():
	with open('1.txt','w') as file:
		user = txtField.get()
		url = f"https://api.github.com/users/{user}"
		userInfo = requests.get(url).json()
		enum = ['company','created_at','email','id','name','url']
		data = userInfo.keys()
		for c in data:
			if c in enum:
				file.write(F"{c}:{userInfo[c]}" + '\n')
	head.configure(text = "Данные записаны!")


root = Tk()
root.title('Get request')
root.geometry('1000x1000')
root["bg"] = "orange"

head = Label(root, bg = "blue", fg = "orange", text = "Введите имя пользователя github: ", font = ('Franklin Gothic Medium',24))
head.pack(expand = True)
txtField = Entry(root, width = 40, font = ('Franklin Gothic Medium', 16))
txtField.pack(expand = True)
button = Button(root, bg = "red", fg = "white", text = "Click here", command = buttonAction)
button.pack(expand = True)

root.mainloop()