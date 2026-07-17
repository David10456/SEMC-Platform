from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QHBoxLayout,
    QListWidget,
    QStatusBar,
    QMenuBar,
    QToolBar
)

from PySide6.QtCore import Qt

from src.semc.ui.pages.dashboard import DashboardPage
from src.semc.ui.workspace import WorkspaceManager


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

        menu.addMenu("File")
        menu.addMenu("Project")
        menu.addMenu("Controller")
        menu.addMenu("Simulation")
        menu.addMenu("Tools")
        menu.addMenu("Help")


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


        # Navigation panel

        self.navigation = QListWidget()


        pages = [
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


        self.navigation.addItems(
            pages
        )


        self.navigation.setFixedWidth(
            240
        )


        # Workspace manager

        self.workspace = WorkspaceManager()


        # Dashboard page

        self.workspace.add_page(
            "Dashboard",
            DashboardPage()
        )


        # Placeholder pages

        for page in pages:

            if page != "Dashboard":

                placeholder = QLabel(
                    f"{page}\n\nModule Under Development"
                )

                placeholder.setAlignment(
                    Qt.AlignCenter
                )

                self.workspace.add_page(
                    page,
                    placeholder
                )


        # Navigation event

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

        self.workspace.show_page(
            name
        )


    def create_status(self):

        status = QStatusBar()

        self.setStatusBar(
            status
        )


        status.showMessage(
            "System Ready | Controller Offline | Simulation Stopped"
        )