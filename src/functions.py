import resources
import os


def make_dir(dir_name: str, dir_name_space: list[str]) -> None:
    os.system(f"mkdir {dir_name} && touch {dir_name}/__init__.py")
    os.chdir(dir_name)
    for oneDirName in dir_name_space:
        os.system(f"mkdir {oneDirName} && touch {oneDirName}/__init__.py")
    os.chdir("..")


def create_module(name: str) -> None:
    os.system(f"mkdir {name}")
    os.chdir(name)

    # Creates application directory
    make_dir(dir_name="application", dir_name_space=["services"])

    # Creates domain directory
    make_dir(dir_name="domain", dir_name_space=resources.domain)

    # Creates infrastructure directory
    make_dir(dir_name="infrastrucutre", dir_name_space=resources.infrastructure)

    # Creates presentation directory
    make_dir(dir_name="presentation", dir_name_space=resources.presentation)


def create_all(src_dir_name: str, module_name: str) -> None:
    make_dir(dir_name=src_dir_name, dir_name_space=resources.src)
    os.chdir(f"{src_dir_name}/modules")
    create_module(name=module_name)
    os.chdir("..")
