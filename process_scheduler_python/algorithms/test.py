from dataclasses import dataclass
import heapq

@dataclass(order=True)
class Aircraft:
    priority: int
    id: int
    type: str
    arrival_time: int
    execution_time: int  # Tempo necessário para o processo, como tempo para aterrissar

class PriorityScheduler:
    def __init__(self):
        self.queue = []
        self.current_time = 0  # Mantém o tempo total de simulação
        self.total_wait_time = 0
        self.total_turnaround_time = 0
        self.process_count = 0

    def add_aircraft(self, aircraft: Aircraft):
        heapq.heappush(self.queue, aircraft)

    def run(self):
        results = []
        while self.queue:
            # Pega a aeronave com a maior prioridade (menor valor de 'priority')
            current_aircraft = heapq.heappop(self.queue)

            # Calcular tempo de espera
            wait_time = max(0, self.current_time - current_aircraft.arrival_time)
            self.total_wait_time += wait_time

            # Atualizar o tempo corrente
            self.current_time += current_aircraft.execution_time

            # Calcular turnaround time
            turnaround_time = self.current_time - current_aircraft.arrival_time
            self.total_turnaround_time += turnaround_time

            # Registrar os resultados
            results.append((current_aircraft.id, wait_time, turnaround_time))

            print(f'Aeronave {current_aircraft.id} ({current_aircraft.type}) aterrissou com prioridade {current_aircraft.priority}')
            print(f'Tempo de espera: {wait_time}, Turnaround time: {turnaround_time}')
            self.process_count += 1

        return results

    def get_average_metrics(self):
        avg_wait_time = self.total_wait_time / self.process_count if self.process_count else 0
        avg_turnaround_time = self.total_turnaround_time / self.process_count if self.process_count else 0
        return avg_wait_time, avg_turnaround_time

# Exemplo de uso
scheduler = PriorityScheduler()

# Adicionando aeronaves com diferentes prioridades
scheduler.add_aircraft(Aircraft(priority=1, id=1, type="Emergência", arrival_time=0, execution_time=3))
scheduler.add_aircraft(Aircraft(priority=3, id=2, type="Comercial", arrival_time=1, execution_time=5))
scheduler.add_aircraft(Aircraft(priority=2, id=3, type="Particular", arrival_time=2, execution_time=2))
scheduler.add_aircraft(Aircraft(priority=1, id=4, type="Emergência", arrival_time=3, execution_time=4))

# Executando o escalonador
results = scheduler.run()

# Calculando as métricas médias
avg_wait_time, avg_turnaround_time = scheduler.get_average_metrics()
print(f'Tempo médio de espera: {avg_wait_time}')
print(f'Tempo médio de turnaround: {avg_turnaround_time}')
