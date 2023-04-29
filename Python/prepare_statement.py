import pandas as pd

INSERT_SQL = \
    "INSERT INTO TABELA (name, age, birthday, money) VALUES ({name}, {age}, {birthday}, {money}, {valentine})"

def prepare_statement(row: dict, sql: str):
    """Prepare a SQL statement from a dictionary
    
    Args:   
        row (dict): A dictionary with the values to be inserted
        sql (str): A SQL statement with the columns to be inserted. The columns must be named as the keys of the dictionary. Example: "INSERT INTO TABELA (name, age, birthday, money) VALUES ({name}, {age}, {birthday}, {money})"
    
    Returns:
        str: A SQL statement with the values from the dictionary
    """
    for key, value in row.items():
        if isinstance(value, str):
            row[key] = f"'{value}'"
        elif value is None or pd.isnull(value):
            row[key] = 'NULL'
        elif isinstance(value, datetime.datetime):
            row[key] = f"'{value.strftime('%Y-%m-%d %H:%M:%S')}'"
        elif isinstance(value, datetime.date):
            row[key] = f"'{value.strftime('%Y-%m-%d')}'"
        else:
            row[key] = str(value)

    return sql.format(**row)