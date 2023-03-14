import hashlib

# Program Inputs
input_file_name = "names.txt"
output_file_name = "output.txt"

# Config
verbose = True

m = hashlib.sha256()
hash_strings = list()

# Open input file to read from
with open(input_file_name) as file:
    for line in file.readlines():
        # Get a copy of the original hash function to work with
        hasher = m.copy()
        
        # Remove whitespace around hash
        str1 = line.strip()
        hasher.update(str1.encode())
        b_hash_string = hasher.digest()

        # Convert binary to hexidecimal string
        hash_string = b_hash_string.hex()

        # Output data
        hash_strings.append(hash_string)
        if verbose:
            print(hash_string)

# Write to output file
with open(output_file_name, mode="wt") as file:
    for str1 in hash_strings:
        # file.writelines(hash_strings)
        file.write(str1)
        file.write("\n")

        