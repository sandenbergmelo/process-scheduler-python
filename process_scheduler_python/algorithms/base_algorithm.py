from abc import ABC
from time import sleep

from rich import print

from process_scheduler_python.utils.process import Process


class BaseAlgorithm(ABC):
    def __init__(self, processes: list[Process]) -> None:
        self.processes = processes

    def _execute_process(self, process: Process):  # noqa: PLR6301
        print(f'Executando {process}')
        sleep(process.execution_time)

    def run(self):
        total_wait_time = 0.0

        for current_process in self.processes:
            current_process.wait_time = round(total_wait_time, 6)
            total_wait_time += current_process.execution_time

            current_process.turn_around_time = round(
                current_process.wait_time + current_process.execution_time, 6
            )

            self._execute_process(current_process)
