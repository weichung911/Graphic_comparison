import cv2

def average_hash(img, hash_size=8):
    A_hash = cv2.resize(img,(hash_size,hash_size),interpolation=cv2.INTER_CUBIC)
    A_hash = cv2.cvtColor(A_hash,cv2.COLOR_BGR2GRAY)
    cv2.imshow('2',A_hash)
    cv2.waitKey(0)
    avg_pixel = A_hash.mean()
    
    hash_value = "".join(['1' if pixel > avg_pixel else '0' for pixel in A_hash.flatten()])
    
    return hash_value

def hamming_distance(hash1, hash2):
    # Calculate the Hamming distance between two hashes
    return sum(bit1 != bit2 for bit1, bit2 in zip(hash1, hash2))