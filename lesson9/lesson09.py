db = "postgresql://postgres:18031996@localhost:5432/QA_test"
from test_sqlalch import StudentTables

def test_insert():
    student_tables = StudentTables(db)
    row, row1 = student_tables.get_tables()
    assert len(row1) > len(row)


def test_update():
    student_tables = StudentTables(db)
    row_count = student_tables.update_table()
    assert row_count.rowcount == 1

def test_delete():
    student_tables = StudentTables(db)
    row_count = student_tables.delete_table()

    assert row_count.rowcount == 0
