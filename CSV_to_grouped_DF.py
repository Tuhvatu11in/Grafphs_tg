import pandas as pd
from time import time


def start(output_file, period=3600 * 24):
    print('Starting groubing by...')
    # Открываем файл csv с сообщениями и считываем в DataFrame
    df = pd.read_csv(output_file)

    # Преобразуем столбец timestamp в формат datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d.%m.%Y %H:%M:%S')

    # Находим первый отметку времени в данных
    first_timestamp = df['timestamp'].min()

    # Вычисляем количество секунд с начальной отметки времени для каждой записи
    df['seconds_from_first'] = (df['timestamp'] - first_timestamp).dt.total_seconds()

    # Вычисляем час отправки каждого сообщения
    df['hour'] = df['seconds_from_first'] // period

    # Группируем данные по отправителю и часу, затем считаем количество сообщений в каждой группе
    message_counts = df.groupby(['sender', 'hour']).size().reset_index(name='message_count')

    # Преобразуем массив в строку
    unique_senders_str = '\n'.join(message_counts['sender'].unique())

    with open('sanders', 'w+', encoding='utf-8') as p:
        p.write(str(unique_senders_str))

    # Сохраняем сгруппированные данные в файл Grouped.csv
    message_counts.to_csv('message_counts.csv', index=False)

    result_dict = {}  # Создаем пустой словарь для хранения результатов

    # Получаем уникальные имена отправителей
    unique_senders = message_counts['sender'].unique()

    t0 = time()

    # Для каждого отправителя выполняем анализ и сохраняем результат в словаре
    for sender in unique_senders:
        filtered_data = message_counts[message_counts['sender'] == sender]
        result_array = []
        for i in range(1, int(max(filtered_data['hour']) + 1)):
            subset = filtered_data[filtered_data['hour'] <= i]
            result = subset['message_count'].sum()
            result_array.append(result)

        # Добавляем результаты в словарь
        result_dict[sender] = result_array
    if __name__ != "main":
        # Сохраняем словарь в текстовый файл с использованием кодировки UTF-8
        with open('message_counts_data.txt', 'w', encoding='utf-8') as file:
            file.write(str(result_dict))

    print(f'finished in {(time() - t0):.2f}s')
    return (result_dict)

if __name__ == '__main__':
    start()