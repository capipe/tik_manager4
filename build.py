import os
import os.path
import shutil
import sys


FOLDERS_TO_COPY = ["tik_manager4"]


def build(source_path, build_path, install_path, targets):

    def _build():
        for folder in FOLDERS_TO_COPY:
            src = os.path.join(source_path, folder)
            dst = os.path.join(build_path, folder)

            if os.path.exists(dst):
                shutil.rmtree(dst)

            shutil.copytree(src, dst)

    def _install():
        for folder in FOLDERS_TO_COPY:
            src = os.path.join(build_path, folder)
            dst = os.path.join(install_path, folder)

            if os.path.exists(dst):
                shutil.rmtree(dst)

            shutil.copytree(src, dst)

            print(f"Installed to {dst}")


    _build()

    if "install" in (targets or []):
        _install()


if __name__ == '__main__':
    build(
        source_path=os.environ['REZ_BUILD_SOURCE_PATH'],
        build_path=os.environ['REZ_BUILD_PATH'],
        install_path=os.environ['REZ_BUILD_INSTALL_PATH'],
        targets=sys.argv[1:]
    )
