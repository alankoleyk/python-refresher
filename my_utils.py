def get_column(file_name, query_column, query_value, result_column=1):
    results = []

    try:
        with open(file_name, 'r') as f:
            for line_num, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue

                fields = line.split(',')

                try:
                    if fields[query_column] == query_value:
                        try:
                            results.append(int(float(fields[result_column])))
                        except ValueError:
                            print(f"Warning: could not convert '{fields[result_column]}' "
                                  f"to int on line {line_num}, skipping.")
                except IndexError:
                    print(f"Warning: line {line_num} does not have enough columns, skipping.")

    except FileNotFoundError:
        print(f"Error: file '{file_name}' not found.")
    except PermissionError:
        print(f"Error: permission denied when trying to read '{file_name}'.")
    except OSError as e:
        print(f"Error: could not open '{file_name}': {e}")

    return results