from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QStatusBar,
    QMenuBar,
    QToolBar,
    QMessageBox
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

        self.create_menu()

        self.create_toolbar()

        self.create_ui()

        self.create_status()


    def create_menu(self):

        menu = self.menuBar()

        file_menu = menu.addMenu("File")

        project_menu = menu.addMenu("Project")

        controller_menu = menu.addMenu(
            "Controller"
        )

        simulation_menu = menu.addMenu(
            "Simulation"
        )

        tools_menu = menu.addMenu(
            "Tools"
        )

        help_menu = menu.addMenu(
            "Help"
        )


    def create_toolbar(self):

        toolbar = QToolBar()

        self.addToolBar(
            toolbar
        )


        toolbar.addAction(
            "▶ Start"
        )

        toolbar.addAction(
            "⏸ Pause"
        )

        toolbar.addAction(
            "⏹ Stop"
        )

        toolbar.addAction(
            "⚙ Settings"
        )


    def create_ui(self):

        central = QWidget()

        self.setCentralWidget(
            central
        )


        layout = QHBoxLayout()

        central.setLayout(
            layout
        )


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
            240
        )


        self.workspace = QLabel(
            "Dashboard Workspace"
        )

        self.workspace.setAlignment(
            Qt.AlignCenter
        )


        self.navigation.currentRowChanged.connect(
            self.change_workspace
        )


        layout.addWidget(
            self.navigation
        )

        layout.addWidget(
            self.workspace
        )


    def change_workspace(self, index):

        name = self.navigation.item(index).text()

        self.workspace.setText(
            f"{name}\n\nModule Ready"
        )


    def create_status(self):

        status = QStatusBar()

        self.setStatusBar(
            status
        )

        status.showMessage(
            "System Ready | Controller Offline | Simulation Stopped"
        )