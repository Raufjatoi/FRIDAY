import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FRIDAY Assistant")
        self.setGeometry(100, 100, 400, 300)

        # Set up the label to display GIF or image
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Load default image
        self.label.setPixmap(QPixmap("lis.png"))
        self.is_gif = False
        self.movie = None

    def update_status(self, status):
        if status == "listening":
            if self.is_gif:
                self.movie.stop()
                self.label.clear()
                self.label.setPixmap(QPixmap("lis.png"))
                self.is_gif = False
        elif status == "speaking":
            self.movie = QMovie("speaking.gif")
            self.label.setMovie(self.movie)
            self.movie.start()
            self.is_gif = True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
