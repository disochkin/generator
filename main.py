import hashlib

def read_large_file(object_file):
    while True:
        data = object_file.readline()
        if not data:
            break
        yield hashlib.md5(str(data).encode("utf-8")).hexdigest()

def process_file(path):
    with open(path, "r") as file_handler:
        for line in read_large_file(file_handler):
            print(line)

if __name__ == "__main__":
    file = "countries.json"
    process_file(file)