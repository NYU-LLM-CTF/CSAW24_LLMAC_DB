import numpy as np

inv_sbox = np.array([0x4a, 0xfc, 0xc3, 0x55, 0x26, 0x28, 0x3f, 0xd8, 0x14, 0x9e, 0x5a, 0xab, 0x1c, 0x96, 0xf2, 0x0d, 0x73, 0xb3, 0x98, 0xe3, 0x12, 0x1b, 0x8a, 0xcf, 0xc0, 0xa7, 0x0c, 0x87, 0xa5, 0x57, 0xcb, 0x59, 0xfb, 0x34, 0xd3, 0xfd, 0x61, 0x5f, 0xdc, 0xfa, 0xf1, 0x21, 0xa0, 0xd2, 0xf7, 0x0f, 0xf8, 0xdd, 0x0e, 0xbd, 0x8b, 0xd1, 0xc1, 0x97, 0x92, 0xca, 0x6e, 0x0b, 0x38, 0xa4, 0xec, 0x4f, 0x39, 0x9d, 0xdb, 0xda, 0xcd, 0x5e, 0x67, 0x10, 0xc8, 0xaa, 0x00, 0x27, 0x4b, 0x66, 0x69, 0xf0, 0x9a, 0xe8, 0xa6, 0xba, 0xe7, 0xe2, 0xb4, 0xfe, 0x5b, 0x15, 0x20, 0x49, 0x56, 0x2f, 0x01, 0x80, 0xe4, 0x78, 0x06, 0x95, 0x1e, 0x79, 0x9c, 0x81, 0xc9, 0x82, 0x76, 0x6c, 0xd9, 0x3e, 0xce, 0x22, 0xb5, 0xe9, 0x9f, 0xe0, 0x84, 0x7f, 0x91, 0x2a, 0x18, 0x60, 0x44, 0x30, 0xc5, 0xcc, 0x62, 0xbf, 0x7d, 0xd6, 0xbe, 0x04, 0x37, 0x48, 0x89, 0xa3, 0x45, 0x1a, 0x6f, 0xeb, 0xef, 0x7b, 0x51, 0x77, 0x19, 0x93, 0xb6, 0x05, 0x0a, 0x8f, 0x08, 0x2d, 0xb9, 0x03, 0xf5, 0x3b, 0x70, 0x35, 0xed, 0x58, 0x88, 0x2b, 0xc4, 0x83, 0x13, 0xee, 0x71, 0x36, 0x63, 0x24, 0xde, 0xd5, 0x6a, 0x4e, 0x90, 0x07, 0x17, 0x41, 0x43, 0x86, 0xb0, 0xc6, 0xd7, 0x4c, 0x16, 0xc2, 0xe1, 0x3a, 0x5d, 0x2e, 0x02, 0x7a, 0x25, 0x31, 0x5c, 0x6b, 0xb7, 0x53, 0x9b, 0xa2, 0xae, 0x50, 0x1f, 0x23, 0xad, 0x09, 0x94, 0xdf, 0xd4, 0x46, 0xc7, 0xff, 0xf4, 0xf3, 0x47, 0xa8, 0xb1, 0xbb, 0x85, 0xd0, 0x32, 0x7e, 0x74, 0x99, 0x11, 0x64, 0xe6, 0x8c, 0xac, 0x52, 0xea, 0x54, 0x72, 0x1d, 0xbc, 0xa9, 0x75, 0x33, 0xb8, 0xf9, 0xf6, 0x8e, 0x3c, 0x65, 0x42, 0x7c, 0x8d, 0x3d, 0xe5, 0xaf, 0xb2, 0x6d, 0x29, 0xa1, 0x40, 0x2c, 0x4d, 0x68])

def inverse_xor_and_shuffle(data):
    # Reverse the shuffle
    mid = len(data) // 2
    for i in range(mid):
        data[i], data[-i-1] = data[-i-1], data[i]
    
    for i in range(len(data) - 1, 0, -1):
        data[i] = data[i] ^ data[i - 1]

    return data

keys = [0xAA, 0xBB, 0xCC, 0xDD, 0xEE]
num_keys = len(keys)

# Encrypted data
def create_hieroglyph_index_map(filename="hieroglyphs.txt"):
    hieroglyph_map = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for index, line in enumerate(file):
            hieroglyph = line.strip()
            hieroglyph_map[hieroglyph] = index
    return hieroglyph_map

hieroglyph_map = create_hieroglyph_index_map()

# Define the sequence of hieroglyphs
hieroglyph_sequence = "𓁡𓆓𓅥𓀺𓃛𓆉𓃣𓁊𓀴𓅜𓀒𓃗𓆂𓄆𓃾𓀠𓅊𓃚𓃧𓄂𓁷𓁻𓅒𓅠𓁡𓀆𓁠𓁿𓅊𓆏𓆃𓁄𓆑𓅅𓆍𓅌𓄄𓆅𓁷𓅡𓆞𓆊𓁺𓁇𓁱𓆝𓁮𓆜𓀚𓅷𓀰𓆝𓅁𓆅𓃣𓁆𓀤𓃔𓅅𓀯𓁏𓃚𓄉𓆄𓀼𓀏𓃻𓁧𓅩𓅳𓀯𓀇𓀛𓀙"

hieroglyph_list = list(hieroglyph_sequence)

# Map each hieroglyph to its index using the hieroglyph map
hieroglyph_indices = [hieroglyph_map[h] for h in hieroglyph_list if h in hieroglyph_map]

encrypted_data = inverse_xor_and_shuffle(hieroglyph_indices)  # First reverse the final shuffle and XOR

# Decryption process simulating reverse of the VM operations
for i in range(len(encrypted_data)):
    byte = encrypted_data[i]
    for j in reversed(range(10)):  # Reverse order of operations
        key_index = (i * 10 + j) % num_keys
        byte = ((byte >> 3) | (byte << (8 - 3))) & 0xff  # Reverse ROTL
        byte ^= (keys[key_index])  # Reverse XOR
        byte = inv_sbox[byte]  # Apply inverse S-box
        byte = ((byte << 3) | (byte >> (8 - 3))) & 0xff  # Reverse ROTR
    encrypted_data[i] = byte

inverse_xor_and_shuffle(encrypted_data)  # Finally reverse the initial shuffle and XOR

decrypted_text = ''.join(chr(byte) for byte in encrypted_data)
print("Decrypted text:", decrypted_text)