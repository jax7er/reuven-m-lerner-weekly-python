import tarfile
from pathlib import Path
from tempfile import TemporaryDirectory as tmp
from zipfile import ZipFile


def tar_to_zip(*file_names: Path, zippath = "."):
    zip_path = Path(zippath) / "output.zip"

    for file_name in file_names:
        try:
            with tmp() as tmp_dir:
                tarfile.open(file_name).extractall(tmp_dir)

                with ZipFile(zip_path, "w") as zip_file:
                    for compress_path in Path(tmp_dir).glob("**/*.*"):
                        zip_file.write(compress_path, compress_path.name)
        except tarfile.ReadError:
            print(f"Read error for {file_name}")
