from sqlalchemy import create_engine
db = "postgresql://postgres:18031996@localhost:5432/QA_test"
from sqlalchemy import text

class StudentTables():

    def __init__(self, db):
        self.db = create_engine(db)

    def get_tables(self):

        data_base = self.db
        connection = data_base.connect()
        transaction = connection.begin()
        len_of_tables = connection.execute(text('SELECT USER_ID FROM GROUP_STUDENT'))
        row = len_of_tables.mappings().all()

        result = connection.execute(text('INSERT INTO GROUP_STUDENT (USER_ID, GROUP_ID) VALUES (15, 20)'))

        len_of_tables_1 = connection.execute(text('SELECT USER_ID FROM GROUP_STUDENT'))
        row1 = len_of_tables_1.mappings().all()
        transaction.commit()
        connection.close()
        return row, row1


    def update_table(self):
        data_base = self.db
        connection = data_base.connect()
        transaction = connection.begin()

        result = connection.execute(text('UPDATE GROUP_STUDENT SET GROUP_ID = 4 WHERE USER_ID = 42568'))

        row_count = connection.execute(text('SELECT USER_ID FROM GROUP_STUDENT WHERE USER_ID = 42568'))

        return row_count


    def delete_table(self):
        data_base = self.db
        connection = data_base.connect()
        transaction = connection.begin()

        result = connection.execute(text('DELETE FROM GROUP_STUDENT WHERE USER_ID = 42568'))

        row_count = connection.execute(text('SELECT USER_ID FROM GROUP_STUDENT WHERE USER_ID = 42568'))

        return row_count