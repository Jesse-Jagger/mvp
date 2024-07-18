from flask import current_app
from flask.cli import with_appcontext
import click

@click.command(name='list-routes')
@with_appcontext
def list_routes():
    output = []
    for rule in current_app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = f"{rule.endpoint:50s} {methods:20s} {rule}"
        output.append(line)

    for line in sorted(output):
        print(line)