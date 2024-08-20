from time import sleep

from rich import print

from process_scheduler_python.utils.process import Process


class SJF:
    def __init__(self, processes: list[Process]) -> None:
        self.processes = sorted(
            processes, key=lambda process: process.execution_time
        )

    def run(self):
        while len(self.processes) > 0:
            current = self.processes.pop(0)
            print(f'Executando: {current}')

            try:
                sleep(current.execution_time)
            except Exception as e:
                print(e)
