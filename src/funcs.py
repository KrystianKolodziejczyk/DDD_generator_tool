from pathlib import Path
import resources


def make_dir(dir_name: str, dir_name_space: list[str]) -> None:
    for name in dir_name_space:
        p = Path(f"./{dir_name}/{name}")
        new_dir = p / name
        new_dir.mkdir(parents=True)
