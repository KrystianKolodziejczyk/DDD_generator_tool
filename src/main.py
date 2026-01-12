import typer
import functions

app = typer.Typer()


@app.command()
def create_all(src_dir_name: str, module_name: str):
    functions.create_all(src_dir_name=src_dir_name, module_name=module_name)


@app.command()
def create_module(name: str):
    functions.create_module(name)


app()
