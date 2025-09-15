# import tkinter
# window=tkinter.Tk()
# window.title('My 1st GUI program')
# window.minsize(width=10,height=12)
#
# mylabel=tkinter.Label(text='Im a label')
# mylabel.pack()
#
# button=tkinter.Button(text='Press me',command=tkinter.Label(text='Im a label1').pack())
# button.pack()
#
# window.mainloop()
#
#
#
#


import json
with open('F:/Python/file.json','r') as f1:
    config=json.load(f1)

print(config["key1"])