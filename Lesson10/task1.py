import argparse


def create_and_write_to_file(path: str, content: str):
    with open(path, "w") as f:
        f.write(content)


def read_file_content(path: str):
    with open(path) as f:
        print(f.read())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--path", default="myfile.txt")
    parser.add_argument("-c", "--content", default="Hello file world!")

    args = parser.parse_args()

    create_and_write_to_file(args.path, args.content)
    read_file_content(args.path)