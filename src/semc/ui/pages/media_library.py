from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QListWidget,
    QFrame,
    QListWidgetItem,
    QGridLayout,
    QLineEdit
)

from PySide6.QtCore import Qt

class MediaLibraryPage(QWidget):

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)

        # Header
        header = QHBoxLayout()

        title = QLabel("Media Library")
        title.setStyleSheet("font-size:22px;font-weight:bold;")

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search media...")

        header.addWidget(title)
        header.addStretch()
        header.addWidget(self.search)

        main_layout.addLayout(header)

        # Toolbar
        toolbar = QHBoxLayout()

        self.import_image_btn = QPushButton("Import Image")
        self.import_video_btn = QPushButton("Import Video")
        self.delete_btn = QPushButton("Delete")
        self.refresh_btn = QPushButton("Refresh")

        toolbar.addWidget(self.import_image_btn)
        toolbar.addWidget(self.import_video_btn)
        toolbar.addWidget(self.delete_btn)
        toolbar.addWidget(self.refresh_btn)
        toolbar.addStretch()

        main_layout.addLayout(toolbar)

        # Workspace
        workspace = QHBoxLayout()

        # Folder panel
        self.folder_list = QListWidget()
        self.folder_list.addItem(QListWidgetItem("📁 Images"))
        self.folder_list.addItem(QListWidgetItem("📁 Videos"))

        self.folder_list.setMaximumWidth(180)

        workspace.addWidget(self.folder_list)

        # Media area
        center_frame = QFrame()

        grid = QGridLayout(center_frame)

        placeholder = QLabel("No media imported yet.")
        placeholder.setAlignment(Qt.AlignCenter)

        grid.addWidget(placeholder, 0, 0)

        workspace.addWidget(center_frame, 1)

        # Preview panel
        preview = QFrame()
        preview.setMaximumWidth(260)

        preview_layout = QVBoxLayout(preview)

        preview_layout.addWidget(QLabel("<b>Preview</b>"))
        preview_layout.addWidget(QLabel("Filename:"))
        preview_layout.addWidget(QLabel("Resolution:"))
        preview_layout.addWidget(QLabel("Size:"))
        preview_layout.addWidget(QLabel("Duration:"))
        preview_layout.addStretch()

        workspace.addWidget(preview)

        main_layout.addLayout(workspace)