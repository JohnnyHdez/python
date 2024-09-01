from livesplit_parser import LivesplitData

# Ruta al archivo .lss
lss_path = 'Silent Hill - NG (Easy, Emulator).lss'

# Cargar los datos del archivo .lss
my_run = LivesplitData(lss_path)

# Imprimir información básica
print('Número de intentos:', my_run.num_attempts)
print('Número de intentos completados:', my_run.num_completed_attempts)
print('Porcentaje de intentos completados:', my_run.percent_runs_completed)
print('Datos de los intentos:\n', my_run.attempt_info_df)
print('Datos de los splits:\n', my_run.split_info_df)


