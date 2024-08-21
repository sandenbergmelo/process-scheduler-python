from process_scheduler_python.algorithms.first_come_first_served import FCFS
from process_scheduler_python.algorithms.priority_scheduling import PS
from process_scheduler_python.algorithms.shortest_job_first import SJF
from process_scheduler_python.utils.factories import ProcessFactory


def run_simulations(amount: int):
    algorithms = ['FCFS', 'SJF', 'PS']
    all_results = {}
    averages_data = []

    for algo in algorithms:
        processes = ProcessFactory.create_batch(amount)
        if algo == 'FCFS':
            scheduler = FCFS(processes)
        elif algo == 'SJF':
            scheduler = SJF(processes)
        elif algo == 'PS':
            scheduler = PS(processes)

        print(f'\nRodando {algo}')
        scheduler.run()

        headers = [
            'ID',
            'Execution Time (s)',
            'Priority',
            'Wait Time (s)',
            'Turnaround Time (s)',
        ]

        rows = [
            [
                process.id,
                process.execution_time,
                process.priority,
                process.wait_time,
                process.turn_around_time,
            ]
            for process in scheduler.processes
        ]

        all_results[algo] = (headers, rows)

        avg_wait_time = sum(
            process.wait_time for process in scheduler.processes
        ) / len(scheduler.processes)

        avg_turnaround_time = sum(
            process.turn_around_time for process in scheduler.processes
        ) / len(scheduler.processes)

        averages_data.append([algo, avg_wait_time, avg_turnaround_time])

    averages_headers = [
        'Algorithm',
        'Average Wait Time (s)',
        'Average Turnaround Time (s)',
    ]

    return all_results, (averages_headers, averages_data)
