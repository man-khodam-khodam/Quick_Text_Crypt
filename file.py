
# github   : github.com/man-khodam-khodam
# telegram : t.me/man_khodam_khodam

import base64

BASE_OPTIONS = {
    '1': 64,
    '2': 32
}

def show_menu(menu_items):
    for key, value in menu_items.items():
        print(f"{key}- {value}")

def main_menu():
    print("Hello")
    print("Choose an operation:")
    menu_items = {
        '1': 'Decode',
        '2': 'Encode'
    }
    show_menu(menu_items)
    choice = input()
    if choice in menu_items:
        if choice == '1':
            decode_menu()
        elif choice == '2':
            encode_menu()
    else:
        print("Invalid choice. Back to the main menu.")
        main_menu()

def decode_menu():
    print("Choose a base:")
    show_menu(BASE_OPTIONS)
    base_choice = input()
    if base_choice in BASE_OPTIONS:
        base = BASE_OPTIONS[base_choice]
    else:
        print("Invalid choice. Back to the decode menu.")
        decode_menu()

    text = input("Enter your text: ")
    decoded_text = decode(text, base)
    print("Decoded text:", decoded_text)
    main_menu()

def encode_menu():
    print("Choose a base:")
    show_menu(BASE_OPTIONS)
    base_choice = input()
    if base_choice in BASE_OPTIONS:
        base = BASE_OPTIONS[base_choice]
    else:
        print("Invalid choice. Back to the encode menu.")
        encode_menu()

    text = input("Enter your text: ")
    encoded_text = encode(text, base)
    print("Encoded text:", encoded_text)
    main_menu()

def decode(text, base):
    try:
        if base == 64:
            decoded_bytes = base64.b64decode(text)
        elif base == 32:
            decoded_bytes = base64.b32decode(text)
        decoded_text = decoded_bytes.decode('utf-8')
        return decoded_text
    except Exception as e:
        print("Error decoding:", str(e))
        return "Decoding error"

def encode(text, base):
    try:
        text_bytes = text.encode('utf-8')
        if base == 64:
            encoded_bytes = base64.b64encode(text_bytes)
        elif base == 32:
            encoded_bytes = base64.b32encode(text_bytes)
        encoded_text = encoded_bytes.decode('utf-8')
        return encoded_text
    except Exception as e:
        print("Error encoding:", str(e))
        return "Encoding error"

main_menu()

# github   : github.com/man-khodam-khodam
# telegram : t.me/man_khodam_khodam
