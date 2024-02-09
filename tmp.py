def print_tables_in_two_columns(tables_data, column_width=14):
    # Дополнить каждый список строк до максимально возможного количества строк, чтобы колонки были равны
    max_rows = max(len(table) for table in tables_data)
    for table in tables_data:
        while len(table) < max_rows:
            table.append(" " * column_width)  # Дополняем пробелами для выравнивания

    # Выводим таблицы попарно
    for i in range(0, len(tables_data), 2):
        left_table = tables_data[i]
        right_table = (
            tables_data[i + 1]
            if i + 1 < len(tables_data)
            else [" " * column_width] * max_rows
        )
        for left_line, right_line in zip(left_table, right_table):
            print(f"{left_line}    {right_line}")


# Пример использования:
tables_data = [
    [
        "/--Table 1:--|",
        "|  - Daryoush |",
        "|  - Fabienne |",
        "|  - Gerrit   |",
        "|  - Niels    |",
        "--------------",
    ],
    [
        "/--Table 2:--|",
        "|  - Ariana   |",
        "|  - Andrea   |",
        "|  - Ivan     |",
        "|  - Nathalie |",
        "--------------",
    ],
    [
        "/--Table 3:--|",
        "|  - Jens     |",
        "|  - Em       |",
        "|  - Karel    |",
        "|  - Danil    |",
        "--------------",
    ],
    [
        "/--Table 4:--|",
        "|  - Mahsa    |",
        "|  - Yanina   |",
        "|  - Geraldine|",
        "|  - Free     |",
        "--------------",
    ],
    [
        "/--Table 5:--|",
        "|  - Free     |",
        "|  - Free     |",
        "|  - Free     |",
        "|  - Free     |",
        "--------------",
    ],
    [
        "/--Table 6:--|",
        "|  - Free     |",
        "|  - Free     |",
        "|  - Free     |",
        "|  - Free     |",
        "--------------",
    ],
]

print_tables_in_two_columns(tables_data)
