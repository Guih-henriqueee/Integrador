EXIST_TABLE = """
    SELECT EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_schema =  {SCHEMA}
          AND table_name =  {TABLE}
    );
"""