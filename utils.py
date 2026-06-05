def clean_columns(data):
    if hasattr(data.columns, "levels"):
        data.columns = data.columns.get_level_values(0)
    return data
