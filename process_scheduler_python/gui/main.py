import tkinter as tk
from tkinter import ttk

import customtkinter as ctk

from process_scheduler_python.algorithms.first_come_first_served import FCFS
from process_scheduler_python.algorithms.priority_scheduling import PS
from process_scheduler_python.algorithms.shortest_job_first import SJF
from process_scheduler_python.utils.factories import ProcessFactory
from process_scheduler_python.utils.process import Process


class SchedulerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Process Scheduler Simulation')
        self.geometry('1000x700')

        # Frame for buttons
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=20)

        # FCFS Button
        self.fcfs_button = ctk.CTkButton(
            self.button_frame, text='Run FCFS', command=self.run_fcfs
        )
        self.fcfs_button.pack(padx=10, pady=5, side=tk.LEFT)

        # SJF Button
        self.sjf_button = ctk.CTkButton(
            self.button_frame, text='Run SJF', command=self.run_sjf
        )
        self.sjf_button.pack(padx=10, pady=5, side=tk.LEFT)

        # PS Button
        self.ps_button = ctk.CTkButton(
            self.button_frame, text='Run PS', command=self.run_ps
        )
        self.ps_button.pack(padx=10, pady=5, side=tk.LEFT)

        # Frame for Treeview results
        self.result_frame = ctk.CTkFrame(self)
        self.result_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        # Label for algorithm name
        self.algorithm_label = ctk.CTkLabel(
            self.result_frame, text='', font=('Arial', 20)
        )
        self.algorithm_label.pack(pady=10, anchor=tk.CENTER)

        # Treeview widget
        self.tree = ttk.Treeview(
            self.result_frame,
            columns=(
                'ID',
                'Execution Time (s)',
                'Priority',
                'Wait Time (s)',
                'Turnaround Time (s)',
            ),
            show='headings',
        )

        # Column headings
        self.tree.heading('ID', text='ID')
        self.tree.heading('Execution Time (s)', text='Execution Time (s)')
        self.tree.heading('Priority', text='Priority')
        self.tree.heading('Wait Time (s)', text='Wait Time (s)')
        self.tree.heading('Turnaround Time (s)', text='Turnaround Time (s)')

        # Column widths
        self.tree.column('ID', width=50, anchor=tk.CENTER)
        self.tree.column('Execution Time (s)', width=150, anchor=tk.CENTER)
        self.tree.column('Priority', width=50, anchor=tk.CENTER)
        self.tree.column('Wait Time (s)', width=150, anchor=tk.CENTER)
        self.tree.column('Turnaround Time (s)', width=150, anchor=tk.CENTER)

        style = ttk.Style(self)
        style.configure(
            'Treeview',
            background='black',
            foreground='white',
            fieldbackground='black',
            font=('Arial', 12),
        )

        style.configure(
            'Treeview.Heading',
            background='gray',
            foreground='white',
            font=('Arial', 14),
        )

        style.map(
            'Treeview',
            background=[('selected', 'gray')],
            foreground=[('selected', 'white')],
        )

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Label for averages
        self.averages_label = ctk.CTkLabel(
            self.result_frame, text='', font=('Arial', 16)
        )
        self.averages_label.pack(pady=10, anchor=tk.CENTER)

    def clear_results(self):
        self.tree.delete(*self.tree.get_children())
        self.algorithm_label.configure(text='')

    def add_processes_to_result(self, processes: list[Process]):
        for process in processes:
            self.tree.insert(
                '',
                tk.END,
                values=(
                    process.id,
                    f'{process.execution_time:.6f}',
                    process.priority
                    if process.priority is not None
                    else 'N/A',
                    f'{process.wait_time:.6f}',
                    f'{process.turn_around_time:.6f}',
                ),
            )

    def add_text_to_result(self, text: str):
        self.algorithm_label.configure(text=text)

    def display_averages(self, processes: list[Process]):
        avg_wait_time = sum(p.wait_time for p in processes) / len(processes)
        avg_turnaround_time = sum(p.turn_around_time for p in processes) / len(
            processes
        )
        self.averages_label.configure(
            text=f'Average Wait Time: {avg_wait_time:.6f} s | '
            f'Average Turnaround Time: {avg_turnaround_time:.6f} s'
        )

    def run_fcfs(self):
        self.clear_results()
        processes = ProcessFactory.create_batch(20)
        fcfs = FCFS(processes)
        self.add_text_to_result('Algorithm: FCFS')
        fcfs.run()
        self.add_processes_to_result(fcfs.processes)
        self.display_averages(fcfs.processes)

    def run_sjf(self):
        self.clear_results()
        processes = ProcessFactory.create_batch(20)
        sjf = SJF(processes)
        self.add_text_to_result('Algorithm: SJF')
        sjf.run()
        self.add_processes_to_result(sjf.processes)
        self.display_averages(sjf.processes)

    def run_ps(self):
        self.clear_results()
        processes = ProcessFactory.create_batch(20)
        ps = PS(processes)
        self.add_text_to_result('Algorithm: PS')
        ps.run()
        self.add_processes_to_result(ps.processes)
        self.display_averages(ps.processes)


if __name__ == '__main__':
    app = SchedulerApp()
    app.mainloop()
