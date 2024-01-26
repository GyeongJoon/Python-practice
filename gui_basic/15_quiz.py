import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480") # 가로 * 세로

# 열기, 저장 파일 이름
filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): # 파일 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) # 파일 내용을 본문에 입력

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

txt = Text(root, wrap="word", yscrollcommand=scrollbar.set) # wrap="word" 옵션을 추가하여 단어 단위로 자동 줄 바꿈 / yscrollcommand를 사용하여 Text 위젯과 스크롤바를 연동
txt.pack(side="left", fill=BOTH, expand=True)

scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()