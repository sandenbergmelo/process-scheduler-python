import pandas as pd

from process_scheduler_python.algorithms.first_come_first_served import FCFS
from process_scheduler_python.algorithms.priority_scheduling import PS
from process_scheduler_python.algorithms.shortest_job_first import SJF
from process_scheduler_python.utils.factories import ProcessFactory


def save_results_to_excel(
    results: dict, averages: pd.DataFrame, filename: str
):
    try:
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            for algo, df in results.items():
                df.to_excel(writer, index=False, sheet_name=algo)
            averages.to_excel(writer, index=False, sheet_name='Averages')

        print(f'\nResultados salvos em {filename}.')

    except Exception as e:
        print(f'\nErro ao salver resultados em {filename}: {e}')


def run_simulations():
    algorithms = ['FCFS', 'SJF', 'PS']
    all_results = {}
    averages_data = []

    for algo in algorithms:
        processes = ProcessFactory.create_batch(5)
        if algo == 'FCFS':
            scheduler = FCFS(processes)
        elif algo == 'SJF':
            scheduler = SJF(processes)
        elif algo == 'PS':
            scheduler = PS(processes)

        print(f'\nRodando {algo}')
        scheduler.run()

        df = pd.DataFrame([
            {
                'ID': process.id,
                'Execution Time (s)': process.execution_time,
                'Priority': process.priority,
                'Wait Time (s)': process.wait_time,
                'Turnaround Time (s)': process.turn_around_time,
            }
            for process in scheduler.processes
        ])

        all_results[algo] = df

        averages_data.append({
            'Algorithm': algo,
            'Average Wait Time (s)': df['Wait Time (s)'].mean(),
            'Average Turnaround Time (s)': df['Turnaround Time (s)'].mean(),
        })

    save_results_to_excel(
        all_results,
        pd.DataFrame(averages_data),
        'process_scheduler_results.xlsx',
    )


def main():
    run_simulations()


if __name__ == '__main__':
    main()
