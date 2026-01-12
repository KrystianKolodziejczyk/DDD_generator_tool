import os


domain: list[str] = ["models", "enums", "repositories", "services"]
infrastructure: list[str] = ["repositories", "services"]
presentation: list[str] = ["controllers", "dto", "responses"]


def create_module(name: str) -> None:
    os.system(f"mkdir {name} && cd {name}")

    # Creates application directory
    os.system("mkdir -p application/services")

    # Creates domain directory
    os.system("mkdir domain && cd domain")
    for dirName in domain:
        os.system(f"mkdir {dirName}")
    os.system("cd ..")

    # Creates infrastructure directory
    os.system("mkdir infrastructure && cd infrastructure")
    for dirName in infrastructure:
        os.system(f"mkdir {dirName}")
    os.system("cd ..")

    # Creates presentation directory
    os.system("mkdir presentation && cd presentation")
    for dirName in presentation:
        os.system(f"mkdir {dirName}")
    os.system("cd ..")


create_module(name="test")
