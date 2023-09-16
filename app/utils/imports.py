import os
from importlib import import_module

from app.utils import paths


def import_models_for_alembic():
    models_file_glob = paths.app_dir.glob("**/models.py")
    models_dir_glob = paths.app_dir.glob("**/models/*.py")
    # Combine the two generators
    models_file_glob = [*models_file_glob, *models_dir_glob]

    for file in models_file_glob:
        # Skip __init__.py
        if file.name == "__init__.py":
            continue

        relative_path = file.relative_to(paths.root_dir)
        module = str(relative_path).replace(os.sep, ".").replace(".py", "")
        import_module(module)
