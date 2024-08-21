from process_scheduler_python.algorithms.first_come_first_served import FCSF
from process_scheduler_python.algorithms.priority_scheduling import PS
from process_scheduler_python.algorithms.shortest_job_first import SJF
from process_scheduler_python.utils.factories import ProcessFactory


def main():
    processes = ProcessFactory.create_batch(5)

    print('FCFS simulation exemple')
    fcsf = FCSF(processes)
    fcsf.run()

    print('\nSJF simulation exemple')
    sjf = SJF(processes)
    sjf.run()

    print('\nPS simulation exemple')
    sjf = PS(processes)
    sjf.run()


if __name__ == '__main__':
    main()
