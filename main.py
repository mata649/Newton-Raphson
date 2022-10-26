
import math
import click
from rich.console import Console
from rich.table import Table


def get_interval_numbers(interval: str):
    p1 = float(interval.split(',')[0].split('[')[1])
    p2 = float(interval.split(',')[1].split(']')[0])
    return p1, p2


def get_parsed_func(function: str):
    print(function)
    return lambda x: eval(function)


def percentage_error(current, previous) -> float:
    return abs(((current - previous) / current) * 100)


def middle_point(a, b) -> float:

    return (a + b) / 2


def function_derivade(func):
    return lambda x: eval(func)


def newton_raphson(func, mid_point, dev_func):

    return (mid_point - (func(mid_point) / dev_func(mid_point)))


def set_table(func: str):
    table = Table(title=f'Newton-Raphson Method {func}')

    table.add_column("Iteration", justify="center", style="cyan")
    table.add_column("Newton-Raphson Result", justify="center", style="cyan")
    table.add_column("Percentage Error", justify="center", style="cyan")
    return table


def add_row(table: Table, iteration: int, result: float, error: float):
    table.add_row(str(iteration), str(result), f'{round(error, 5)}%')


@click.command()
@click.option('--interval', help='function interval', type=str, required=True)
@click.option('--function',
              help='function to do the calculus',
              type=str,
              required=True)
@click.option('--derivade',
              help='derivade of the function',
              type=str,
              required=True)
@click.option('--error', help='error', type=float, required=True)
def run(interval: str, function: str, derivade: str, error: str):
    console = Console()
    table = set_table(function)
    func = get_parsed_func(function)
    a, b = get_interval_numbers(interval)
    current_error = 100
    iteration = 1
    previous_result = 0
    current_result = middle_point(a, b)
  
    derivade_func = function_derivade(derivade)
    while current_error > error:

        current_result = newton_raphson(func, current_result, derivade_func)
        current_error = percentage_error(current_result, previous_result)

        add_row(table, iteration, current_result, current_error)
        previous_result = current_result
        iteration += 1
    console.print(table)


if __name__ == '__main__':
    run()
