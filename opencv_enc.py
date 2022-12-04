import cv2
import numpy as np

demo = cv2.imread("D:\Kuliah\SEMESTER III\Sistem Kemanan Data\File\IMG_20200731_091521.jpg", 0)
r, c = demo.shape
key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)  # Generate random key image
cv2.imwrite("D:\Kuliah\SEMESTER III\Sistem Kemanan Data\File\key.jpg", key)   # Save key image

cv2.imshow("demo", demo)  # Display original image
cv2.imshow("key", key)  # Display key image

encryption = cv2.bitwise_xor(demo, key)  # encryption
cv2.imwrite("D:\Kuliah\SEMESTER III\Sistem Kemanan Data\File\image_asli_enkripsi.jpg", encryption)  
   # Save the encrypted image
decryption = cv2.bitwise_xor(encryption, key)  # decrypt
cv2.imwrite("D:\Kuliah\SEMESTER III\Sistem Kemanan Data\File\image_asli_dekripsi.jpg", decryption) # Save the decrypted image

cv2.imshow("encryption", encryption)  # Display ciphertext image
cv2.imshow("decryption", decryption)  # Displays the decrypted image

cv2.waitKey(-1)
cv2.destroyAllWindows()