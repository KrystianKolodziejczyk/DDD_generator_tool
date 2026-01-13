import typer
import functions
from pathlib import Path

app = typer.Typer()


@app.command("project-gen")
def create_all() -> None:
    main_dir_name: str = typer.prompt("Enter source-code project name")
    module_dir_name: str = typer.prompt("Enter first module name")
    functions.create_all(src_dir_name=main_dir_name, module_name=module_dir_name)


@app.command("add-module")
def create_module() -> None:
    module_name: str = typer.prompt("Enter module name")
    functions.create_module(name=module_name)


@app.callback()
def message(context: typer.Context) -> None:
    print(f"Executing: {context.invoked_subcommand}\n")


# if __name__ == "__main__":
#     app()

my_dir = Path("./test")
my_file = Path("./spr")

my_dir.mkdir(mode=511)
my_file.touch(mode=438)

new_file = my_dir / "test_file.txt"
new_file.mkdir(mode=438)

print(my_dir.parent)
print(new_file)
print(new_file.parent)
