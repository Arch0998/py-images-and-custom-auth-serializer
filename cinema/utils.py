import pathlib
import uuid
from django.utils.text import slugify


def cinema_image_path(instance, filename):
    ext = pathlib.Path(filename).suffix
    unique_id = uuid.uuid4()
    filename = f"{slugify(instance.title)}-{unique_id}{ext}"
    return pathlib.Path("uploads/movies/") / filename
