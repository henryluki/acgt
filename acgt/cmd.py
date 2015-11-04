import click
from acgt import Acgt

@click.group()
def cli():
    """Example script."""
    pass

@click.command()
@click.argument('project_name')
@click.option('--js',default=False, help="generate js file")
@click.option('--flask',default=False, help="generate flask file")
def init(project_name, js, flask):
  project = project_name

  if js:
    click.echo(" init js ... ")
    Acgt(project).parse_apis("js")
  elif flask:
    click.echo("init flask app ...")
    Acgt(project).parse_apis("flask")
  else:
    click.echo("*** usage info ***")
    click.echo("--(flask,js)   generate code by acgt")

  click.echo("done!")

cli.add_command(init)

