# core/io.py
import pandas as pd
import os

def infer_field_types(df):
    """Automatische Typenerkennung: numeric oder categorical"""
    field_types = {}
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            field_types[col] = "numeric"
        else:
            field_types[col] = "categorical"
    return field_types

def import_data(hdc, filepath, max_rows=None, infer_types=True):
    ext = os.path.splitext(filepath)[1]
    if ext == ".csv":
        df = pd.read_csv(filepath)
    elif ext == ".parquet":
        df = pd.read_parquet(filepath)
    else:
        raise ValueError("Unsupported file format")

    if max_rows:
        df = df.head(max_rows)

    df = df.fillna(0)

    if infer_types:
        field_types = infer_field_types(df)
        hdc.set_field_types(field_types)

    for idx, row in df.iterrows():
        uid = str(row.get("id", f"row_{idx}"))
        hdc.add(uid, row.to_dict())

    return df
