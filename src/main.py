import os

app: list[str] = ["modules", "shared", "core"]
domain: list[str] = ["models", "enums", "repositories", "services"]
infrastructure: list[str] = ["repositories", "services"]
presentation: list[str] = ["controllers", "dto", "responses"]


def make_dir(dirName: str, dirNameSpace: list[str]) -> None:
    os.system(f"mkdir {dirName} && touch {dirName}/__init__.py")
    os.chdir(dirName)
    for oneDirName in dirNameSpace:
        os.system(f"mkdir {oneDirName} && touch {oneDirName}/__init__.py")
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


def create_all(appDirName: str) -> None:
    make_dir(dirName=appDirName, dirNameSpace=app)
    os.chdir(f"{appDirName}/modules")
    create_module(name="example")
    os.chdir("..")


create_all(appDirName="app")
