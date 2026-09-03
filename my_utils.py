def get_column(file_name, query_column, query_value, result_column=1):
    results = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            fields = line.split(',')
            if fields[query_column] == query_value:
                results.append(fields[result_column])
    return results