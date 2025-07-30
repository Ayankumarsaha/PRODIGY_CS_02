from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    encrypted_img = Image.new(img.mode, img.size)
    pixels = img.load()
    encrypted_pixels = encrypted_img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            # XOR each channel with key
            encrypted_pixels[i, j] = (r ^ key, g ^ key, b ^ key)
    
    encrypted_img.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    # Since XOR is reversible, we use the same function
    encrypt_image(input_path, output_path, key)

def main():
    print("Image Encryption Tool using Pixel Manipulation")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").strip().lower()
    input_path = input("Enter input image path (e.g., image.png): ")
    output_path = input("Enter output image path (e.g., output.png): ")
    key = int(input("Enter numeric key (0-255): "))

    if 0 <= key <= 255:
        if choice == 'e':
            encrypt_image(input_path, output_path, key)
        elif choice == 'd':
            decrypt_image(input_path, output_path, key)
        else:
            print("Invalid choice. Please choose 'e' or 'd'.")
    else:
        print("Invalid key. Please enter a number between 0 and 255.")

if __name__ == "__main__":
    main()
