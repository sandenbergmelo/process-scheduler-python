import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass
import heapq
import time
from threading import Thread

@dataclass(order=True)
class Aircraft:
    priority: int
    id: int
    type: str
    arrival_time: int
    execution_time: int

class PriorityScheduler:
    def __init__(self):
        self.queue = []
        self.current_time = 0
        self.total_wait_time = 0
        self.total_turnaround_time = 0
        self.process_count = 0

    def add_aircraft(self, aircraft: Aircraft):
        heapq.heappush(self.queue, aircraft)

    def run(self, update_callback):
        while self.queue:
            current_aircraft = heapq.heappop(self.queue)

            # Calcular tempo de espera
            wait_time = max(0, self.current_time - current_aircraft.arrival_time)
            self.total_wait_time += wait_time

            # Atualizar o tempo corrente
            self.current_time += current_aircraft.execution_time

            # Calcular turnaround time
            turnaround_time = self.current_time - current_aircraft.arrival_time
            self.total_turnaround_time += turnaround_time

            # Atualizar a UI com os resultados
            update_callback(current_aircraft, wait_time, turnaround_time)

            # Simula o tempo de execução (aterrissagem)
            time.sleep(current_aircraft.execution_time)

            self.process_count += 1

class SimulationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulação de Escalonamento de Prioridade - Controle de Tráfego Aéreo")

        # Configurar o layout
        self.tree = ttk.Treeview(root, columns=('ID', 'Tipo', 'Prioridade', 'Espera', 'Turnaround'), show='headings')
        self.tree.heading('ID', text='ID da Aeronave')
        self.tree.heading('Tipo', text='Tipo de Aeronave')
        self.tree.heading('Prioridade', text='Prioridade')
        self.tree.heading('Espera', text='Tempo de Espera')
        self.tree.heading('Turnaround', text='Tempo de Turnaround')

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Botão de iniciar a simulação
        self.start_button = tk.Button(root, text="Iniciar Simulação", command=self.start_simulation)
        self.start_button.pack(pady=10)

        # Criar o escalonador de prioridade
        self.scheduler = PriorityScheduler()

        # Adicionar aeronaves à fila de simulação
        self.scheduler.add_aircraft(Aircraft(priority=1, id=1, type="Emergência", arrival_time=0, execution_time=3))
        self.scheduler.add_aircraft(Aircraft(priority=3, id=2, type="Comercial", arrival_time=1, execution_time=5))
        self.scheduler.add_aircraft(Aircraft(priority=2, id=3, type="Particular", arrival_time=2, execution_time=2))
        self.scheduler.add_aircraft(Aircraft(priority=1, id=4, type="Emergência", arrival_time=3, execution_time=4))

    def update_table(self, aircraft, wait_time, turnaround_time):
        # Adicionar os resultados da aeronave na tabela
        self.tree.insert('', 'end', values=(aircraft.id, aircraft.type, aircraft.priority, wait_time, turnaround_time))

    def start_simulation(self):
        # Executar a simulação em uma thread separada
        thread = Thread(target=self.scheduler.run, args=(self.update_table,))
        thread.start()

# Configurar e rodar a interface gráfica
if __name__ == "__main__":
    root = tk.Tk()
    gui = SimulationGUI(root)
    root.mainloop()
