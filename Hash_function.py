import cv2
import numpy as np

def average_hash(img, hash_size=8):
    A_hash = cv2.resize(img,(hash_size,hash_size),interpolation=cv2.INTER_CUBIC)
    A_hash = cv2.cvtColor(A_hash,cv2.COLOR_BGR2GRAY)
    cv2.imshow('A_hash',A_hash)
    cv2.waitKey(0)
    avg_pixel = A_hash.mean()
    
    hash_value = "".join(['1' if pixel > avg_pixel else '0' for pixel in A_hash.flatten()])
    
    return hash_value

def hamming_distance(hash1, hash2):
    # Calculate the Hamming distance between two hashes
    return sum(bit1 != bit2 for bit1, bit2 in zip(hash1, hash2))

def perceptual_Hash(img, hash_size=32):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray_image, (hash_size, hash_size),interpolation=cv2.INTER_CUBIC)
    dct_image = cv2.dct(np.float32(resized_image))
    dct_image = dct_image[:8, :8]
    cv2.imshow('dct_image',dct_image)
    cv2.waitKey(0)
    mean_value = np.mean(dct_image)
    hash_value = "".join(['1' if pixel > mean_value else '0' for pixel in dct_image.flatten()])
    
    return hash_value

def difference_Hash(img):
    image = cv2.resize(img,(9,8),interpolation=cv2.INTER_CUBIC )
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    dhash_str = ''
    for i in range(8):
        for j in range(8):
            if gray[i,j]>gray[i, j+1]:
                dhash_str = dhash_str + '1'
            else:
                dhash_str = dhash_str + '0'
    return dhash_str
