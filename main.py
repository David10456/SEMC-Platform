import sys

from PySide6.QtWidgets import QApplication

from src.semc.ui.main_window import SEMCMainWindow
from src.semc.ui.theme import DARK_THEME


def main():

    app = QApplication(sys.argv)

    app.setStyleSheet(
        DARK_THEME
    )

    window = SEMCMainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()