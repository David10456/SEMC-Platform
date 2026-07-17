from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QStatusBar
)

from PySide6.QtCore import Qt


class SEMCMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "SEMC Studio v1.0"
        )

        self.resize(
            1200,
            800
        )

        self.create_ui()


    def create_ui(self):

        # Main container
        central_widget = QWidget()

        self.setCentralWidget(
            central_widget
        )


        # Main layout
        main_layout = QHBoxLayout()

        central_widget.setLayout(
            main_layout
        )


        # Navigation panel
        self.navigation = QListWidget()

        self.navigation.addItems(
            [
                "Dashboard",
                "Media Library",
                "Playlist Manager",
                "Display Designer",
                "Controller Explorer",
                "Communication",
                "Virtual LED Wall",
                "Performance",
                "Diagnostics",
                "Developer Console",
                "Settings"
            ]
        )


        self.navigation.setFixedWidth(
            220
        )


        # Workspace
        workspace = QWidget()

        workspace_layout = QVBoxLayout()

        workspace.setLayout(
            workspace_layout
        )


        title = QLabel(
            "Welcome to SEMC Studio"
        )

        title.setAlignment(
            Qt.AlignCenter
        )


        subtitle = QLabel(
            "Standalone Embedded Multimedia Controller\nDigital Twin Environment"
        )

        subtitle.setAlignment(
            Qt.AlignCenter
        )


        workspace_layout.addWidget(
            title
        )

        workspace_layout.addWidget(
            subtitle
        )


        main_layout.addWidget(
            self.navigation
        )

        main_layout.addWidget(
            workspace
        )


        # Status bar
        self.setStatusBar(
            QStatusBar()
        )

        self.statusBar().showMessage(
            "System Ready | Simulation Offline"
        )