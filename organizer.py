import shutil
from pathlib import Path

from config import (
    DEFAULT_TRG_FOLDER,
    FILE_CATS,
    OTHER_CAT_NAME,
    SKIP_HIDDEN_FILES,
    ALLOW_OVERWRITE,
    SHOW_MOVED_FILES
)

def get_category(file_ext: str) -> str:
    for category, extensions in FILE_CATS.items():
        if file_ext.lower() in extensions:
            return category
    return OTHER_CAT_NAME

def is_hidden(file_path: Path) -> bool:
    return file_path.name.startswith(".")

def resolve_conflict(target_file: Path) -> Path:
    if ALLOW_OVERWRITE or not target_file.exists():
        return target_file

    counter = 1
    while True:
        new_file = target_file.with_name(
            f"{target_file.stem}_{counter}{target_file.suffix}"
        )
        if not new_file.exists():
            return new_file
        counter += 1

def organize_folder(folder_path: Path) -> None:
    if not folder_path.exists():
        print("Folder doesn't exist!")
        return

    if not folder_path.is_dir():
        print("Given path is not a directory!")
        return 
    
    moved_files = 0

    for item in folder_path.iterdir():
        if not item.is_file():
            continue
    
        if SKIP_HIDDEN_FILES and is_hidden(item):
            continue

        category = get_category(item.suffix)
        target_dir = folder_path / category
        target_dir.mkdir(exist_ok = True)

        target_file = resolve_conflict(target_dir / item.name)
        shutil.move(str(item), str(target_file))

        moved_files += 1
        if SHOW_MOVED_FILES:
            print(f"{item.name} -> {category}")
    print(f"Done. {moved_files} file(s) organized.")


if __name__ == "__main__":
    print("AUTOMATED_FILE_ORGANIZER")
  
    print("Press Enter to use default folder or provide a custom path.\n")

    user_input = input(f"Folder path [{DEFAULT_TRG_FOLDER}]: ").strip()
    target_folder = Path(user_input) if user_input else DEFAULT_TRG_FOLDER

    organize_folder(target_folder)

