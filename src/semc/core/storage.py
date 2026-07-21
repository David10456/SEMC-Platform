import os
import shutil


class StorageManager:

    def __init__(self):

        self.base_path = "storage"

        self.images_path = os.path.join(
            self.base_path,
            "images"
        )

        self.videos_path = os.path.join(
            self.base_path,
            "videos"
        )

        self.thumbnail_path = os.path.join(
            self.base_path,
            "thumbnails"
        )

        self.create_storage()


    def create_storage(self):

        folders = [
            self.images_path,
            self.videos_path,
            self.thumbnail_path
        ]

        for folder in folders:

            os.makedirs(
                folder,
                exist_ok=True
            )


    def save_file(self, source_path, media_type):

        if media_type == "image":

            destination_folder = self.images_path

        elif media_type == "video":

            destination_folder = self.videos_path

        else:

            raise ValueError(
                "Unsupported media type"
            )


        filename = os.path.basename(
            source_path
        )


        destination = os.path.join(
            destination_folder,
            filename
        )


        shutil.copy2(
            source_path,
            destination
        )


        return destination