#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tkinter as tk
import time

def five_sec_start():
    print("5秒スタート ")
    time_sta = time.time()
    time.sleep(5)
# 時間計測終了
    time_end = time.time()
# 経過時間（秒）
    tim = time_end- time_sta
    print(tim)

root = tk.Tk()                # 窓を作る
root.title("Timer")   # 窓のタイトルを設定
root.geometry("640x480") 
#ウィンドウだけ出来た。タイトルはTimer

label = tk.Label(root, text="5分スタート")  # ラベルを作成

#ラベルを表示
label.pack()    

button = tk.Button()                        # ボタンを作成
button["text"] = "5秒スタート"         # ボタンにラベルを設定
button["command"] = lambda: five_sec_start() # ボタンの動作を設定
button.pack()    

root.mainloop()  # ループ（対話型環境では不要）


# In[ ]:




