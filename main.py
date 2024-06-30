
### 4. main.py

from gui import create_gui
from voice_recognition import listen_for_hotword

def main():
    create_gui()
    listen_for_hotword()

if __name__ == "__main__":
    main()
