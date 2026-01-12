import os


domain: list[str] = ["models", "enums", "repositories", "services"]
infrastructure: list[str] = ["repositories", "services"]
presentation: list[str] = ["controllers", "dto", "responses"]


def make_dir(dirName: str, dirNameSpace: list[str]) -> None:
    os.system(f"mkdir {dirName}")
    os.chdir(dirName)
    for oneDirName in dirNameSpace:
        os.system(f"mkdir {oneDirName}")
    os.chdir("..")


def create_module(name: str) -> None:
    os.system(f"mkdir {name}")
    os.chdir(name)

    # Creates application directory
    make_dir(dirName="application", dirNameSpace=["services"])

    # Creates domain directory
    make_dir(dirName="domain", dirNameSpace=domain)

    # Creates infrastructure directory
    make_dir(dirName="infrastrucutre", dirNameSpace=infrastructure)

    # Creates presentation directory
    make_dir(dirName="presentation", dirNameSpace=presentation)


# create_module(name="program")


def create_all() -> None:
    os.system("mkdir src && mkdir shared && mkdir core")
    os.chdir("src")
    os.system("mkdir modules")
    os.chdir("modules")
    create_module(name="example")
    os.chdir("..")
