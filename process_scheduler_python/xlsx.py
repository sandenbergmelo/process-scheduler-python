import pandas as pd

from process_scheduler_python.utils.run_simulations import run_simulations


def save_results_to_excel(
    results: dict, averages: pd.DataFrame, filename: str
):
    try:
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            for algo, (headers, rows) in results.items():
                df = pd.DataFrame(rows, columns=headers)
                df.to_excel(writer, index=False, sheet_name=algo)
            averages.to_excel(writer, index=False, sheet_name='Averages')

        print(f'\nResultados salvos em {filename}.')

    except Exception as e:
        print(f'\nErro ao salvar resultados em {filename}: {e}')


def main():
    all_results, (averages_headers, averages_data) = run_simulations(100)
    averages_df = pd.DataFrame(averages_data, columns=averages_headers)
    save_results_to_excel(
        all_results, averages_df, 'process_scheduler_results.xlsx'
    )


if __name__ == '__main__':
    main()
