from voice_recognition import listen_for_hotword
from gui import MainWindow
from commands import search_google, search_wikipedia, play_music, play_movie, get_news

import sys
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    listen_for_hotword()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
