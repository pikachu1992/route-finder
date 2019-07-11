#!/usr/bin/python
import webbrowser
from time import time
import click

from fsnavigator_map import FsNavigatorMap
from route_finder import RouteFinder

@click.command()
@click.argument('start')
@click.argument('end')
def route(start, end):
    click.echo('Loading route map...')
    _start = time()
    map = FsNavigatorMap()
    _end = time()
    click.echo(f'Route map loaded in {_end - _start}s')

    start = map.nodes[start]
    end = map.nodes[end]
    route = RouteFinder(map=map, start=start, end=end)

    click.echo(f'Finding route from {start.name} to {end.name}...')
    _start = time()
    route.find()
    _end = time()
    click.echo(f'Found route: {route.atc_route} in {_end - _start}s.')
    click.echo(f'Opening SkyVector https://skyvector.com/?fpl={route.atc_route}')
    webbrowser.open(f'https://skyvector.com/?fpl={route.atc_route}')

if __name__ == '__main__':
    route()
