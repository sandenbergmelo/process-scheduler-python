from process_scheduler_python.algorithms.first_come_first_served import FCFS
from process_scheduler_python.algorithms.priority_scheduling import PS
from process_scheduler_python.algorithms.shortest_job_first import SJF
from process_scheduler_python.utils.factories import ProcessFactory


def main():
    processes = ProcessFactory.create_batch(100)

    print('FCFS simulation exemple')
    fcsf = FCFS(processes)
    fcsf.run()

    print('\nSJF simulation exemple')
    sjf = SJF(processes)
    sjf.run()

    print('\nPS simulation exemple')
    sjf = PS(processes)
    sjf.run()


if __name__ == '__main__':
    main()
