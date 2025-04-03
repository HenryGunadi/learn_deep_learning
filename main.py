from pathlib import Path

def main():
    testing_path = Path("./")
    file_path = testing_path / "lol.txt"

    if not file_path.exists():
        print("Downloading file...")

        with open(file_path, "wb") as f:
            f.write(b"Hello world")
    else:
        print("File already exists")

    

if __name__ == "__main__":
    main()