#LIST FUNGSI YANG DIJALANKAN
def TAMBAH(x, y):
    return x + y

def KURANG(x, y):
    return x - y

def KALI(x, y):
    return x * y

def BAGI(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

#LIST PILIHAN FUNGSI YANG AKAN MUNCUL
def calculator():
    print("Select operation:")
    print("1. TAMBAH")
    print("2. KURANG")
    print("3. KALI")
    print("4. BAGI")

    choice = input("PILIH AKSI (1/2/3/4): ")

#INPUT BILANGAN
    num1 = float(input("MASUKAN NO PERTAMA: "))
    num2 = float(input("MASUKAN NO KEDUA: "))

#LIST INSTRUKSI TUGAS
    if choice == '1':
        result = TAMBAH(num1, num2)
    elif choice == '2':
        result = KURANG(num1, num2)
    elif choice == '3':
        result = KALI(num1, num2)
    elif choice == '4':
        result = BAGI1(num1, num2)
    else:
        raise ValueError("Invalid choice")

    print(f"HASIL: {result}")

if __name__ == "__main__":
    try:
        calculator()
    except ValueError as e:
        print(e)