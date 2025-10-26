from PIL import Image
import numpy as np


#Encryption of the image 

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img) 
    
    # Apply XOR operation for encryption
    encrypted_array = img_array ^ key  

    # Convert back to an image
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save("encrypted_image.png")
    print("Encryption complete! Encrypted image saved as 'encrypted_image.png'.")

#Decryption of the image 
def decrypt_image(image_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Apply XOR again to decrypt
    decrypted_array = img_array ^ key  

    # Convert back to an image
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save("decrypted_image.png")
    print("Decryption complete! Decrypted image saved as 'decrypted_image.png'.")

# User input
image_path = "cat.png"
key = 123  # A simple encryption key (0-255)

# Encrypt and decrypt
encrypt_image(image_path, key)
decrypt_image("encrypted_image.png", key)
