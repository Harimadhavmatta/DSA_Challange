import string

def discount(p, l):
    a = p // 10
    if a > l:
        return l
    return a

def encrypt(input_str, shift):
    encrypted = []
    for i in input_str:
        if i.isalpha():
            base = 'A' if i.isupper() else 'a'
            encrypted.append(chr((ord(i) - ord(base) + shift) % 26 + ord(base)))
        else:
            encrypted.append(i)
    return ''.join(encrypted)

def decrypt(input_str, shift):
    return encrypt(input_str, 26 - shift)

def generate_list(map_obj):
    print("Generated List:")
    for key, value in map_obj.items():
        print(f"{key} : {value}")

def get_discount(map_obj, encrypted_key):
    result = map_obj.get(encrypted_key)
    if result:
        print("Discount details:", result)
        map_obj.pop(encrypted_key)
    else:
        print("No details found for the provided key.")

def user_coupons(user, map_obj):
    print(f"Coupon list of {user}")
    for key, value in map_obj.items():
        if value == user:
            print(key)

def main():
    n = int(input("Enter the number of bills: "))
    user_map1 = {}
    user_map2 = {}

    for i in range(n):
        purchase = int(input("Enter the total bill amount: "))
        user = input("Enter user ID: ")
        item = input("Enter item category: ")
        limit = 700
        discount_amt = discount(purchase, limit)
        input_str = f"{item}.{discount_amt}.{user}"
        shift = 4
        encrypted = encrypt(input_str, shift)
        print("Encrypted:", encrypted)
        user_map1[encrypted] = f"{item} with discount: {discount_amt}"
        user_map2[encrypted] = user
        decrypted = decrypt(encrypted, shift)
        print("Decrypted:", decrypted)
        print("...................................")

    generate_list(user_map1)
    encrypted_key = input("Enter encrypted key to get discount: ")
    get_discount(user_map1, encrypted_key)
    print("......................................")
    generate_list(user_map1)
    print("......................................")
    user_coupons("hari", user_map2)
    print("......................................")

if __name__ == "__main__":
    main()
