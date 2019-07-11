#!/usr/bin/python
import webbrowser
from time import time
import pickle
import click

from fsnavigator_map import FsNavigatorMap
from route_finder import RouteFinder

@click.group()
def cli():
    pass

@cli.command()
def build():
    stats = time()
    map = FsNavigatorMap()
    stats = time() - stats
    click.echo(f'Route map built in {stats:.1f}s.')
    with open('.map', 'wb') as file:
        pickle.dump(map, file)

def get_map():
    try:
        with open('.map', 'rb') as file:
            return pickle.load(file)
    except TypeError:
        return FsNavigatorMap()

@cli.command()
@click.argument('start')
@click.argument('end')
@click.option('--open/--no-open', '-o/-no', default=False)
def route(start, end, open):
    map = get_map()

    start = map.nodes[start]
    end = map.nodes[end]
    route = RouteFinder(map=map, start=start, end=end)

    stats = time()
    route.find()
    stats = time() - stats
    click.echo(f'Found route in {stats:.1f}s.')
    click.echo(f'ROUTE: {route.atc_route}')
    webbrowser.open(f'https://skyvector.com/?fpl={route.atc_route}')

if __name__ == '__main__':
    cli()
