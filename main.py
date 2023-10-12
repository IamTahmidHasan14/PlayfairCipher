def prepare_text(text):
  text = text.replace(" ", "").upper().replace("J", "I")
  i = 0
  while i < len(text) - 1:
    if text[i] == text[i + 1]:
      text = text[:i + 1] + 'X' + text[i + 1:]
    i += 2
  if len(text) % 2 != 0:
    text += 'X'
  return text

def playfair_matrix(key):
  key = key.replace(" ", "").upper().replace("J", "I")
  key_set = set(key)
  alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
  alphabet = ''.join([char for char in alphabet if char not in key_set])

  matrix = []
  row = []

  for char in key + alphabet:
    row.append(char)
    if len(row) == 5:
      matrix.append(row)
      row = []
  return matrix

def find_position(matrix, char):
  for i, row in enumerate(matrix):
    if char in row:
      return i, row.index(char)

def playfair_encrypt(plain_text, key):
  matrix = playfair_matrix(key)
  plain_text = prepare_text(plain_text)
  encrypted_text = ""

  for i in range(0, len(plain_text), 2):
    char1 = plain_text[i]
    char2 = plain_text[i + 1]
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)

    if row1 == row2:
      encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
      encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
      encrypted_text += matrix[row1][col2] + matrix[row2][col1]

  return encrypted_text

def playfair_decrypt(encrypted_text, key):
  matrix = playfair_matrix(key)
  decrypted_text = ""

  for i in range(0, len(encrypted_text), 2):
    char1 = encrypted_text[i]
    char2 = encrypted_text[i + 1]
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)

    if row1 == row2:
      decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
      decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else: 
      decrypted_text += matrix[row1][col2] + matrix[row2][col1]

  return decrypted_text

key = "TAHMID"
print("Key:", key, "\n")

matrix = playfair_matrix(key)
for row in matrix:
  print(" ".join(row))

plain_text = "HUCKLEBERRY"

encrypted_text = playfair_encrypt(plain_text, key)
decrypted_text = playfair_decrypt(encrypted_text, key)

print("\nPlain Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
