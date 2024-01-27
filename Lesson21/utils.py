from open_file import MyOpen
import zipfile


def compress_file(file_obj: MyOpen):
    with zipfile.ZipFile(f"{file_obj.file_name}.zip", "w") as archive:
        archive.write(file_obj.full_file_name)