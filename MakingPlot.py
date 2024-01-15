import matplotlib.pyplot as plt
import ast


def start(result_dict, min_value=1000):
    if __name__ == '__main__':
        # Читаем данные из текстового файла
        with open("message_counts_data.txt", 'r', encoding='utf-8') as file:
            data = file.read()

        # Преобразуем строку обратно в словарь
        result_dict = ast.literal_eval(data)

    result_dict_without_blanks = {key: value for (key, value) in result_dict.items() if len(value) > 0}
    filtered_dict = {key: value for (key, value) in result_dict_without_blanks.items() if value[-1] > min_value}

    line_styles = ['-', '--', '-.', ':']  # Список различных стилей линий

    # Создаем график с различными стилями линий
    for i, (sender, data) in enumerate(filtered_dict.items()):
        style = line_styles[i % len(line_styles)]  # Выбор стиля линии из списка с помощью деления по модулю
        plt.plot(range(1, len(data) + 1), data, label=sender, linestyle=style)
    plt.ylabel('Количество сообщений')
    plt.xlabel('Часов от создания группы')
    plt.legend()

def show_plot():
    plt.show()

if __name__ == '__main__':
    start()