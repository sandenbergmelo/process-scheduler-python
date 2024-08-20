from dataclasses import dataclass
import heapq
from time import sleep


@dataclass(order=True)
class Aircraft:
    priority: int
    id: int
    type: str
    execution_time: int  # Tempo necessário para o processo, como tempo para aterrissar


class PriorityScheduler:
    def __init__(self):
        self.queue = []

    def add_aircraft(self, aircraft: Aircraft):
        # Usamos uma heap para organizar as aeronaves por prioridade
        heapq.heappush(self.queue, aircraft)

    def run(self):
        while self.queue:
            # Pega a aeronave com a maior prioridade (menor valor de 'priority')
            current_aircraft = heapq.heappop(self.queue)
            print(f'Aeronave {current_aircraft.id} ({current_aircraft.type}) está aterrissando com prioridade {current_aircraft.priority}')
            
            try:
                # Simula o tempo necessário para a aterrissagem
                sleep(current_aircraft.execution_time)
            except Exception as e:
                print(f'Erro ao processar a aeronave {current_aircraft.id}: {e}')


# Exemplo de uso:
scheduler = PriorityScheduler()

# Adicionando aeronaves com diferentes prioridades
scheduler.add_aircraft(Aircraft(priority=1, id=1, type="Emergência", execution_time=3))
scheduler.add_aircraft(Aircraft(priority=3, id=2, type="Comercial", execution_time=5))
scheduler.add_aircraft(Aircraft(priority=2, id=3, type="Particular", execution_time=2))
scheduler.add_aircraft(Aircraft(priority=1, id=4, type="Emergência", execution_time=4))

# Rodando o escalonador
scheduler.run()
