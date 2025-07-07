LAYOUT_TABLE = """
                    SELECT column_name 
                            FROM information_schema.columns
                            WHERE table_schema = {SCHEMA}
                            AND table_name = {TABLE};
"""

