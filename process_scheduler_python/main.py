from rich.console import Console
from rich.table import Table

from process_scheduler_python.utils.run_simulations import run_simulations


def print_table(title: str, headers: list[str], rows: list[list]):
    console = Console()

    table = Table(title=title)

    for header in headers:
        table.add_column(header, justify='left', style='cyan')

    for row in rows:
        table.add_row(*map(str, row))

    console.print(table)


def main():
    all_results, (averages_headers, averages_data) = run_simulations(5)

    print()
    for algo, (headers, rows) in all_results.items():
        print_table(f'Simulação do {algo}', headers, rows)

    print_table('Médias', averages_headers, averages_data)


if __name__ == '__main__':
    main()
