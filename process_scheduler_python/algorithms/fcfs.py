from time import sleep

from utils.process import Process


class FCSF:
    def __init__(self, processes: list[Process]) -> None:
        self.processes = processes

    def run(self):
        while len(self.processes) > 0:
            current = self.processes.pop(0)
            print(f'Executando: {current}')

            try:
                sleep(current.execution_time)
            except Exception as e:
                print(e)
