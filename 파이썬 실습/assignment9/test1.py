import tkinter as tk
from tkinter import messagebox, filedialog

def encrypt_text():
    # 파일 대화 상자 열기
    file_path = filedialog.askopenfilename(filetypes=[('텍스트 파일', '*.txt')])

    if file_path:
        try:
            # 파일 읽기
            with open(file_path, 'r') as file:
                text = file.read()

            # 텍스트 암호화
            encrypted_text = vigenere_cipher(text, keyword='SECRET')  # 암호화 함수 호출 (비즈네르 암호를 예시로 사용)

            # 새로운 파일 생성하여 암호화된 텍스트 저장
            save_path = filedialog.asksaveasfilename(defaultextension='.tenc', filetypes=[('암호화된 파일', '*.tenc')])
            with open(save_path, 'w') as file:
                file.write(encrypted_text)

            messagebox.showinfo("암호화 완료", "텍스트 암호화가 완료되었습니다.")
        except IOError:
            messagebox.showerror("에러", "파일을 읽는 중에 오류가 발생했습니다.")
    else:
        messagebox.showwarning("경고", "파일을 선택하지 않았습니다.")

def decrypt_text():
    # 파일 대화 상자 열기
    file_path = filedialog.askopenfilename(filetypes=[('암호화된 파일', '*.tenc')])

    if file_path:
        try:
            # 파일 읽기
            with open(file_path, 'r') as file:
                encrypted_text = file.read()

            # 텍스트 복호화
            decrypted_text = vigenere_decipher(encrypted_text, keyword='SECRET')  # 복호화 함수 호출 (비즈네르 암호의 복호화 과정)

            # 새로운 파일 생성하여 복호화된 텍스트 저장
            save_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('텍스트 파일', '*.txt')])
            with open(save_path, 'w') as file:
                file.write(decrypted_text)

            messagebox.showinfo("복호화 완료", "텍스트 복호화가 완료되었습니다.")
        except IOError:
            messagebox.showerror("에러", "파일을 읽는 중에 오류가 발생했습니다.")
    else:
        messagebox.showwarning("경고", "파일을 선택하지 않았습니다.")

def vigenere_cipher(text, keyword):
    # 비즈네르 암호 알고리즘 구현 (예시)
    # 여기에서 실제 암호화 알고리즘을 구현하시면 됩니다.
    # 이 예시에서는 각 문자를 키워드의 문자와 XOR 연산하여 암호화합니다.
    encrypted_text = ''
    keyword_length = len(keyword)
    for i, char in enumerate(text):
        key_char = keyword[i % keyword_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        encrypted_text += encrypted_char
    return encrypted_text

def vigenere_decipher(text, keyword):
    # 비즈네르 암호 복호화 알고리즘 구현 (예시)
    # 여기에서 실제 복호화 알고리즘을 구현하시면 됩니다.
    # 이 예시에서는 각 문자를 키워드의 문자와 XOR 연산하여 복호화합니다.
    decrypted_text = ''
    keyword_length = len(keyword)
    for i, char in enumerate(text):
        key_char = keyword[i % keyword_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        decrypted_text += decrypted_char
    return decrypted_text

window = tk.Tk()
window.title("메뉴 예제")

menu = tk.Menu(window)

encryption_menu = tk.Menu(menu, tearoff=0)
encryption_menu.add_command(label="텍스트 암호화", command=encrypt_text)
encryption_menu.add_command(label="텍스트 복호화", command=decrypt_text)

menu.add_cascade(label="암호화 메뉴", menu=encryption_menu)

window.config(menu=menu)

window.mainloop()
