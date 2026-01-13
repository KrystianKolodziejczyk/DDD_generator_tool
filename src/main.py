import typer
import funcs

# from pathlib import Path

app = typer.Typer()


@app.command("project-gen")
def create_all() -> None:
    main_dir_name: str = typer.prompt("Enter source-code directory name")
    module_dir_name: str = typer.prompt("Enter first module name")
    funcs.create_all(
        project_dir_name=main_dir_name,
        module_name=module_dir_name,
    )


@app.command("add-module")
def create_module() -> None:
    main_dir_name: str = typer.prompt("Enter source-code directory name")
    module_name: str = typer.prompt("Enter module name")
    funcs.create_module(module_name=module_name, project_dir_name=main_dir_name)


@app.callback()
def message(context: typer.Context) -> None:
    print(f"Executing: {context.invoked_subcommand}\n")


if __name__ == "__main__":
    app()
