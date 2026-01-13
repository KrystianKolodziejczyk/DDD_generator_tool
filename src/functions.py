from pathlib import Path
import resources


def make_dir(path: Path, dir_name_list: list[str]) -> None:
    for name in dir_name_list:
        inside_folders: Path = path / name
        init_file = inside_folders / "__init__.py"

        inside_folders.mkdir()
        init_file.touch()


# Creates module
def create_module(module_name: str, project_dir_name: str) -> None:
    project_root = Path.cwd().resolve()
    projectPath: Path = project_root / project_dir_name

    modulesPath: Path = projectPath / "modules" / module_name
    init_file: Path = modulesPath / "__init__.py"

    modulesPath.mkdir(exist_ok=True)
    init_file.touch(exist_ok=True)

    make_dir(path=modulesPath, dir_name_list=resources.module)

    dirPath: Path = modulesPath / "application"
    make_dir(path=dirPath, dir_name_list=["services"])

    dirPath: Path = modulesPath / "domain"
    make_dir(path=dirPath, dir_name_list=resources.domain)

    dirPath: Path = modulesPath / "infrastructure"
    make_dir(path=dirPath, dir_name_list=resources.infrastructure)

    dirPath: Path = modulesPath / "presentation"
    make_dir(path=dirPath, dir_name_list=resources.presentation)


# Creates project
def create_all(project_dir_name: str, module_name: str) -> Path:
    project_root = Path.cwd().resolve()

    projectPath: Path = project_root / project_dir_name
    init_file: Path = projectPath / "__init__.py"

    projectPath.mkdir()
    init_file.touch()

    for name in resources.src:
        inside_folders: Path = projectPath / name
        init_file: Path = inside_folders / "__init__.py"

        inside_folders.mkdir()
        init_file.touch()

    create_module(module_name=module_name, project_dir_name=project_dir_name)
