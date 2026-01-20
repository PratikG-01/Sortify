from pathlib import Path

# Default folder to organize
DEFAULT_TRG_FOLDER = Path.home() / "Downloads"

# File type categories and extensions
FILE_CATS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".c", ".cpp", ".js", ".html", ".css", ".java"]
}

# Fallback category
OTHER_CAT_NAME = "Others"

# Safety options
SKIP_HIDDEN_FILES = True
ALLOW_OVERWRITE = False

# Output behavior
SHOW_MOVED_FILES = True
