import tkinter as tk
from tkinter import filedialog
import os

#추가한 기능은 없습니다

def encrypt_text():
    # 파일 대화 상자 열기
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    if file_path:
        # 키워드 입력을 위한 윈도우 창 생성
        keyword_window = tk.Tk()
        keyword_window.title("암호화 키워드 입력")

        # 키워드 입력을 위한 레이블 및 텍스트 상자 생성
        keyword_label = tk.Label(keyword_window, text="암호화에 사용할 키워드를 입력하세요:")
        keyword_label.pack()

        keyword_entry = tk.Entry(keyword_window)
        keyword_entry.pack()

        def confirm_keyword():
            # 키워드 확인 및 윈도우 창 닫기
            keyword = keyword_entry.get()
            keyword_window.destroy()

            # 파일 읽기
            with open(file_path, "r", encoding="utf-8") as file:
                original_text = file.read()

            # 텍스트 암호화
            encrypted_text = vigenere_cipher(original_text, keyword)

            # 저장 파일 경로 생성
            save_path = get_encrypted_filename1(file_path)

            # 암호화된 텍스트 파일 저장
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(encrypted_text)

        # 확인 버튼 생성
        confirm_button = tk.Button(keyword_window, text="확인", command=confirm_keyword)
        confirm_button.pack()

        keyword_window.mainloop()

def decrypt_text():
    # 파일 대화 상자 열기
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.tenc")])

    if file_path:
        # 키워드 입력을 위한 윈도우 창 생성
        keyword_window = tk.Tk()
        keyword_window.title("복호화 키워드 입력")

        # 키워드 입력을 위한 레이블 및 텍스트 상자 생성
        keyword_label = tk.Label(keyword_window, text="복호화에 사용할 키워드를 입력하세요:")
        keyword_label.pack()

        keyword_entry = tk.Entry(keyword_window)
        keyword_entry.pack()

        def confirm_keyword():
            # 키워드 확인 및 윈도우 창 닫기
            keyword = keyword_entry.get()
            keyword_window.destroy()

            # 파일 읽기
            with open(file_path, "r", encoding="utf-8") as file:
                encrypted_text = file.read()

            # 텍스트 복호화
            decrypted_text = vigenere_decipher(encrypted_text, keyword)

            # 저장 파일 경로 생성
            save_path = get_decrypted_filename1(file_path)

            # 복호화된 텍스트 파일 저장
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(decrypted_text)

        # 확인 버튼 생성
        confirm_button = tk.Button(keyword_window, text="확인", command=confirm_keyword)
        confirm_button.pack()

        keyword_window.mainloop()

def encrypt_file():
    # 파일 대화 상자 열기
    file_path = filedialog.askopenfilename()

    if file_path:
        # 키워드 입력을 위한 윈도우 창 생성
        keyword_window = tk.Tk()
        keyword_window.title("암호화 키워드 입력")

        # 키워드 입력을 위한 레이블 및 텍스트 상자 생성
        keyword_label = tk.Label(keyword_window, text="암호화에 사용할 키워드를 입력하세요:")
        keyword_label.pack()

        keyword_entry = tk.Entry(keyword_window)
        keyword_entry.pack()

        def confirm_keyword():
            # 키워드 확인 및 윈도우 창 닫기
            keyword = keyword_entry.get()
            keyword_window.destroy()

            # 이진 파일 읽기
            with open(file_path, "rb") as file:
                original_data = file.read()

            # 이진 파일 암호화
            encrypted_data = rc4_cipher(original_data, keyword)

            # 저장 파일 경로 생성
            save_path = get_encrypted_filename2(file_path)

            # 암호화된 이진 파일 저장
            with open(save_path, "wb") as file:
                file.write(encrypted_data)

        # 확인 버튼 생성
        confirm_button = tk.Button(keyword_window, text="확인", command=confirm_keyword)
        confirm_button.pack()

        keyword_window.mainloop()

def decrypt_file():
    # 파일 대화 상자 열기
    file_path = filedialog.askopenfilename(filetypes=[("Binary Files", "*.benc")])

    if file_path:
        # 키워드 입력을 위한 윈도우 창 생성
        keyword_window = tk.Tk()
        keyword_window.title("복호화 키워드 입력")

        # 키워드 입력을 위한 레이블 및 텍스트 상자 생성
        keyword_label = tk.Label(keyword_window, text="복호화에 사용할 키워드를 입력하세요:")
        keyword_label.pack()

        keyword_entry = tk.Entry(keyword_window)
        keyword_entry.pack()

        def confirm_keyword():
            # 키워드 확인 및 윈도우 창 닫기
            keyword = keyword_entry.get()
            keyword_window.destroy()

            # 이진 파일 읽기
            with open(file_path, "rb") as file:
                encrypted_data = file.read()

            # 이진 파일 복호화
            decrypted_data = rc4_decipher(encrypted_data, keyword)

            # 저장 파일 경로 생성
            save_path = get_decrypted_filename2(file_path)

            # 복호화된 이진 파일 저장
            with open(save_path, "wb") as file:
                file.write(decrypted_data)

        # 확인 버튼 생성
        confirm_button = tk.Button(keyword_window, text="확인", command=confirm_keyword)
        confirm_button.pack()

        keyword_window.mainloop()

def get_encrypted_filename1(file_path):
    # 파일명과 확장자 분리
    file_name, file_ext = os.path.splitext(file_path)

    # 암호화된 파일명 생성
    encrypted_file_name = file_name + ".tenc"

    return encrypted_file_name

def get_encrypted_filename2(file_path):
    # 파일명과 확장자 분리
    file_name, file_ext = os.path.splitext(file_path)

    # 암호화된 파일명 생성
    encrypted_file_name = file_name + ".benc"

    return encrypted_file_name

def get_decrypted_filename1(file_path):
    # 파일명과 확장자 분리
    file_name, file_ext = os.path.splitext(file_path)

    # 복호화된 파일명 생성
    decrypted_file_name = file_name + "_복호화" + ".txt"

    return decrypted_file_name


def get_decrypted_filename2(file_path):
    # 파일명과 확장자 분리
    file_name, file_ext = os.path.splitext(file_path)

    # 복호화된 파일명 생성
    decrypted_file_name = file_name + "_복호화"

    return decrypted_file_name

def vigenere_cipher(text, keyword):
    # 비즈네르 암호화 수행
    encrypted_text = ""
    keyword_length = len(keyword)
    for i, char in enumerate(text):
        key = keyword[i % keyword_length]
        encrypted_char = chr((ord(char) + ord(key)) % 256)
        encrypted_text += encrypted_char
    return encrypted_text

def vigenere_decipher(text, keyword):
    # 비즈네르 복호화 수행
    decrypted_text = ""
    keyword_length = len(keyword)
    for i, char in enumerate(text):
        key = keyword[i % keyword_length]
        decrypted_char = chr((ord(char) - ord(key)) % 256)
        decrypted_text += decrypted_char
    return decrypted_text

def rc4_cipher(data, key):
    # RC4 암호화 수행
    S = list(range(256))
    j = 0
    encrypted_data = bytearray()

    # 키를 바이트로 변환
    key = key.encode('utf-8')

    # 초기화 단계
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # 암호화 단계
    i = 0
    j = 0
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        encrypted_data.append(byte ^ k)

    return encrypted_data



def rc4_decipher(data, key):
    # RC4 복호화 수행
    return rc4_cipher(data, key)


def main():
    root = tk.Tk()
    root.title("암호화 GUI")
    root.geometry("400x300")

    menubar = tk.Menu(root)

    encrypt_menu = tk.Menu(menubar, tearoff=0)
    encrypt_menu.add_command(label="텍스트 암호화", command=encrypt_text)
    encrypt_menu.add_command(label="파일 암호화", command=encrypt_file)

    decrypt_menu = tk.Menu(menubar, tearoff=0)
    decrypt_menu.add_command(label="텍스트 복호화", command=decrypt_text)
    decrypt_menu.add_command(label="파일 복호화", command=decrypt_file)

    menubar.add_cascade(label="암호화", menu=encrypt_menu)
    menubar.add_cascade(label="복호화", menu=decrypt_menu)

    root.config(menu=menubar)

    root.mainloop()

if __name__ == "__main__":
    main()
