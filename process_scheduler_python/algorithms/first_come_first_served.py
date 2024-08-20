from time import sleep

from rich import print

from process_scheduler_python.utils.process import Process


class FCSF:
    def __init__(self, processes: list[Process]) -> None:
        self.processes = processes

    def run(self):
        total_wait_time = 0.0

        for i in range(len(self.processes)):
            self.processes[i].wait_time = total_wait_time
            total_wait_time += self.processes[i].execution_time

            print(f'Executando: {self.processes[i]}')

            try:
                sleep(self.processes[i].execution_time)
            except Exception as e:
                print(e)
