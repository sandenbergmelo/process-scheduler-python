from time import sleep

from rich import print

from process_scheduler_python.utils.process import Process


class FCSF:
    def __init__(self, processes: list[Process]) -> None:
        self.processes = processes

    def run(self):
        total_wait_time = 0.0

        for current_process in self.processes:
            current_process.wait_time = total_wait_time
            total_wait_time += current_process.execution_time

            print(f'Executando: {current_process}')

            try:
                sleep(current_process.execution_time)
            except Exception as e:
                print(e)
