import os

from sqlalchemy.orm import Session

from src.semc.core.storage import StorageManager
from src.semc.database.models import Media


class MediaController:

    def __init__(self, session: Session):

        self.session = session

        self.storage = StorageManager()


    def import_media(self, file_path):

        filename = os.path.basename(file_path)

        extension = os.path.splitext(
            filename
        )[1].lower()


        if extension in [
            ".png",
            ".jpg",
            ".jpeg",
            ".bmp"
        ]:

            media_type = "image"


        elif extension in [
            ".mp4",
            ".avi",
            ".mov"
        ]:

            media_type = "video"


        else:

            raise ValueError(
                "Unsupported file type"
            )


        saved_path = self.storage.save_file(
            file_path,
            media_type
        )


        media = Media(
            filename=filename,
            filepath=saved_path,
            media_type=media_type
        )


        self.session.add(
            media
        )

        self.session.commit()


        return media