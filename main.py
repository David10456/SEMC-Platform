import sys

from PySide6.QtWidgets import QApplication

from src.semc.ui.main_window import SEMCMainWindow


def main():
    app = QApplication(sys.argv)

    window = SEMCMainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()