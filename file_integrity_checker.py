import hashlib
import datetime

print("=" * 50)
print("File Integrity Checker")
print("=" * 50)

print("\n1. Save Hash")
print("2. Verify File")

choice = input("\nEnter choice: ")

filename = input("Enter file name: ")

with open(filename, "rb") as file:
    data = file.read()

file_size = len(data)

sha256_hash = hashlib.sha256(data).hexdigest()

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# SAVE HASHw
if choice == "1":

    records = {}

    try:
        with open ("hashes.txt", "r") as file:

            for line in file:

                part = line.strip().split(":", 2)

                if len(part) == 3:
                    stroed_file, stored_hash, saved_time = part
                    records[stroed_file] = (stored_hash, saved_time)

    except FileNotFoundError:
        pass

    records[filename] = (sha256_hash, timestamp)      

    with open("hashes.txt", "a") as file:

        for file_name,(file_hash, file_time) in records.items():
                
                file.write(
                    f"{file_name}:{file_hash}:{file_time}\n"
                )

    print("\nHash saved successfully!")
    print("\nFile Name:")
    print(filename)

    print("SHA256 Hash:")
    print(sha256_hash)

    print("\nSaved Time:")
    print(timestamp)

# VERIFY HASH
elif choice == "2":

    try:
        with open("hashes.txt", "r") as file:
            saved_hashes = file.readlines()

    except FileNotFoundError:
        print("\nNo hashes have been saved yet.")
        exit()

    found = False

    for line in saved_hashes:

        stored_file, stored_hash, saved_time = line.strip().split(":", 2)

        if stored_file == filename:

            found = True

            print("\n" + "=" * 50)
            print("File Integrity MONITORING REPORT")
            print("=" * 50)

            print("\nFile Name:")
            print(filename)

            print("\nFile Size:")
            print(f"{file_size} bytes")

            print("\nSaved Time:")
            print(saved_time)

            print("\nCurrent Time:")
            print(timestamp)

            print("\nOriginal Hash:")
            print(stored_hash)

            print("\nCurrent Hash:")
            print(sha256_hash)

            print("\nStatus:")

            if stored_hash == sha256_hash:
                print("✅ SECURE")
                print("File Integrity Verified")

            else:
                print("🚨 COMPROMISED")
                print("File Integrity Failed")

    if not found:
        print("File not found in hash records.")

else:
    print("Invalid Choice")