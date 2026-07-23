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
    QLineEdit,
    QFileDialog,
    QMessageBox,
    QScrollArea
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

import os
from datetime import datetime

from src.semc.controllers.media_controller import MediaController
from src.semc.database.session import get_session


class ClickableFrame(QFrame):

    def __init__(self, callback):

        super().__init__()

        self.callback = callback


    def mousePressEvent(self, event):

        self.callback()

        super().mousePressEvent(event)



class MediaLibraryPage(QWidget):

    def __init__(self):

        super().__init__()


        main_layout = QVBoxLayout(self)


        # ==========================
        # Header
        # ==========================

        header = QHBoxLayout()


        title = QLabel(
            "Media Library"
        )

        title.setStyleSheet(
            "font-size:22px;font-weight:bold;"
        )


        self.search = QLineEdit()

        self.search.setPlaceholderText(
            "Search media..."
        )


        header.addWidget(title)

        header.addStretch()

        header.addWidget(
            self.search
        )


        main_layout.addLayout(
            header
        )


        # ==========================
        # Toolbar
        # ==========================

        toolbar = QHBoxLayout()


        self.import_image_btn = QPushButton(
            "Import Image"
        )

        self.import_video_btn = QPushButton(
            "Import Video"
        )

        self.delete_btn = QPushButton(
            "Delete"
        )

        self.refresh_btn = QPushButton(
            "Refresh"
        )


        toolbar.addWidget(
            self.import_image_btn
        )

        toolbar.addWidget(
            self.import_video_btn
        )

        toolbar.addWidget(
            self.delete_btn
        )

        toolbar.addWidget(
            self.refresh_btn
        )

        toolbar.addStretch()


        main_layout.addLayout(
            toolbar
        )


        self.import_image_btn.clicked.connect(
            self.import_image
        )

        self.refresh_btn.clicked.connect(
            self.load_gallery
        )


        # ==========================
        # Workspace
        # ==========================

        workspace = QHBoxLayout()


        # Folder panel

        self.folder_list = QListWidget()


        self.folder_list.addItem(
            QListWidgetItem("📁 Images")
        )

        self.folder_list.addItem(
            QListWidgetItem("📁 Videos")
        )


        self.folder_list.setMaximumWidth(
            180
        )


        workspace.addWidget(
            self.folder_list
        )



        # ==========================
        # Gallery
        # ==========================


        self.scroll = QScrollArea()

        self.scroll.setWidgetResizable(
            True
        )


        self.gallery = QWidget()


        self.gallery_layout = QGridLayout(
            self.gallery
        )


        self.gallery_layout.setSpacing(
            15
        )


        self.scroll.setWidget(
            self.gallery
        )


        workspace.addWidget(
            self.scroll,
            1
        )



        # ==========================
        # Preview Panel
        # ==========================


        preview = QFrame()

        preview.setMaximumWidth(
            280
        )


        preview_layout = QVBoxLayout(
            preview
        )


        preview_title = QLabel(
            "<b>Preview</b>"
        )


        self.preview_image = QLabel()


        self.preview_image.setFixedSize(
            240,
            180
        )


        self.preview_image.setAlignment(
            Qt.AlignCenter
        )


        self.preview_image.setStyleSheet(
            """
            border:1px solid gray;
            background:#1f1f1f;
            """
        )


        self.filename_label = QLabel(
            "Filename:"
        )

        self.resolution_label = QLabel(
            "Resolution:"
        )

        self.size_label = QLabel(
            "Size:"
        )

        self.date_label = QLabel(
            "Imported:"
        )



        preview_layout.addWidget(
            preview_title
        )

        preview_layout.addWidget(
            self.preview_image
        )

        preview_layout.addWidget(
            self.filename_label
        )

        preview_layout.addWidget(
            self.resolution_label
        )

        preview_layout.addWidget(
            self.size_label
        )

        preview_layout.addWidget(
            self.date_label
        )

        preview_layout.addStretch()



        workspace.addWidget(
            preview
        )


        main_layout.addLayout(
            workspace
        )


        # Load database media

        self.load_gallery()



    # ==================================================
    # Load Gallery From PostgreSQL
    # ==================================================

    def load_gallery(self):

        try:

            # clear current gallery

            while self.gallery_layout.count():

                item = self.gallery_layout.takeAt(0)

                widget = item.widget()

                if widget:

                    widget.deleteLater()



            session = get_session()


            controller = MediaController(
                session
            )


            media_files = controller.get_all_media()



            for media in media_files:


                if os.path.exists(
                    media.filepath
                ):


                    self.add_media_card(
                        media.filepath,
                        media.filename
                    )


        except Exception as e:


            QMessageBox.critical(
                self,
                "Loading Error",
                str(e)
            )



    # ==================================================
    # Preview
    # ==================================================

    def show_preview(self, filepath):


        pixmap = QPixmap(
            filepath
        )


        if pixmap.isNull():

            return



        scaled = pixmap.scaled(
            240,
            180,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )


        self.preview_image.setPixmap(
            scaled
        )


        self.filename_label.setText(
            f"Filename: {os.path.basename(filepath)}"
        )


        self.resolution_label.setText(
            f"Resolution: {pixmap.width()} x {pixmap.height()}"
        )


        size = os.path.getsize(filepath) / 1024


        self.size_label.setText(
            f"Size: {size:.1f} KB"
        )


        created = datetime.fromtimestamp(
            os.path.getctime(filepath)
        )


        self.date_label.setText(
            f"Imported: {created.strftime('%d-%m-%Y %H:%M')}"
        )



    # ==================================================
    # Media Card
    # ==================================================

    def add_media_card(
        self,
        filepath,
        filename
    ):


        card = ClickableFrame(
            lambda: self.show_preview(filepath)
        )


        card.setFixedSize(
            180,
            180
        )


        card.setStyleSheet(
            """
            QFrame{
                background:#2b2b2b;
                border:1px solid #444;
                border-radius:8px;
            }
            """
        )


        layout = QVBoxLayout(
            card
        )


        image = QLabel()


        image.setFixedSize(
            160,
            120
        )


        image.setAlignment(
            Qt.AlignCenter
        )


        pixmap = QPixmap(
            filepath
        )


        if not pixmap.isNull():


            thumb = pixmap.scaled(
                160,
                120,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )


            image.setPixmap(
                thumb
            )


        name = QLabel(
            filename
        )


        name.setAlignment(
            Qt.AlignCenter
        )


        layout.addWidget(
            image
        )


        layout.addWidget(
            name
        )


        count = self.gallery_layout.count()


        row = count // 4

        col = count % 4



        self.gallery_layout.addWidget(
            card,
            row,
            col
        )



    # ==================================================
    # Import Image
    # ==================================================

    def import_image(self):


        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )


        if not file_path:

            return



        try:


            session = get_session()


            controller = MediaController(
                session
            )


            media = controller.import_media(
                file_path
            )


            self.add_media_card(
                media.filepath,
                media.filename
            )


            self.show_preview(
                media.filepath
            )


            QMessageBox.information(
                self,
                "Success",
                f"Imported: {media.filename}"
            )



        except Exception as e:


            QMessageBox.critical(
                self,
                "Import Failed",
                str(e)
            )