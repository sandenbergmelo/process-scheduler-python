from process_scheduler_python.algorithms.base_algorithm import BaseAlgorithm
from process_scheduler_python.utils.process import Process


class PS(BaseAlgorithm):
    def __init__(self, processes: list[Process]) -> None:
        self.processes = sorted(
            processes, key=lambda process: -process.priority
        )
