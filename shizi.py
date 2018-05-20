#coding=utf-8
'''from PIL import Image
import pytesseract
text=pytesseract.image_to_string(Image.open('./d.png'),lang='chi_sim')
print(text)'''


from aip import AipOcr
import json
from tkinter import *
import tkinter.filedialog


# 定义常量
APP_ID = '9851066'
API_KEY = 'LUGBatgyRGoerR9FZbV4SQYk'
SECRET_KEY = 'fB2MNz1c2UHLTximFlC4laXPg7CVfyjV'

# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
root= Tk(className='识字')

def go():
    for i in result['words_result']:
        text.insert(END,i['words'])

def select():
    return tkinter.filedialog.askopenfilename()
def xz():
    filePath = select()
    if filePath != '':
        lb.config(text="您选择的文件是：" + filePath);
    else:
        lb.config(text="您没有选择任何文件");

Label(root, text='选择路径：').pack()
lb = Label(root, text='')
lb.pack()
Button(root, text="弹出选择文件对话框", command=xz).pack()

text = Text(root)
text.pack()

Button(root, text="开始识别", command=go).pack()






def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

    # 定义参数变量


options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}

# 调用通用文字识别接口
result = aipOcr.basicGeneral(get_file_content(select()), options)
#print(result)
'''for i in result['words_result']:
    print(i['words'])
    #print(result['words_result'][i]['words'])

#root = Tk()
'''

'''label = Label(root)
label['text'] = 'be on your own'
label.pack()
button = Button(root)
button['text'] = '识别'
button.pack()
text = Text(root)
text.pack();'''

root.mainloop()