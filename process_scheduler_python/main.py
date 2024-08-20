from process_scheduler_python.algorithms.first_come_first_served import FCSF
from process_scheduler_python.algorithms.shortest_job_first import SJF
from process_scheduler_python.utils.factories import ProcessFactory


def main():
    print('FCFS simulation exemple')
    fcsf = FCSF(ProcessFactory.create_batch(10))
    fcsf.run()

    print('\nSJF simulation exemple')
    sjf = SJF(ProcessFactory.create_batch(1000))
    sjf.run()


if __name__ == '__main__':
    main()
