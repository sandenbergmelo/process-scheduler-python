from process_scheduler_python.algorithms.first_come_first_served import FCSF
from process_scheduler_python.algorithms.shortest_job_first import SJF
from process_scheduler_python.utils.process import Process


def main():
    print('FCFS simulation exemple')
    fcsf = FCSF([
        Process(id=1, execution_time=0.5),
        Process(id=2, execution_time=0.3),
        Process(id=3, execution_time=0.8),
        Process(id=4, execution_time=0.6),
    ])
    fcsf.run()

    print('\nSJF simulation exemple')
    sjf = SJF([
        Process(id=1, execution_time=0.5),
        Process(id=2, execution_time=0.3),
        Process(id=3, execution_time=0.8),
        Process(id=4, execution_time=0.6),
    ])
    sjf.run()


if __name__ == '__main__':
    main()
