from sqlalchemy import create_engine
from sqlalchemy import text


class EmployeeSQL:
    __scripts = {
        "select by id_company": text("select * from employee where company_id = :company_id"),
        "delete by id": text("delete from employee where id =:id_to_delete"),
        "insert new": text("insert into employee(\"first_name\", \"last_name\", \"middle_name\", \"company_id\", \"email\", \"phone\") values (:first_name, :last_name, :middle_name, :company_id, :email, :phone)"),
        "get max id": text("select MAX(\"id\") from employee")
    }

    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)

    def get_employees(self, my_params):
        with self.engine.connect() as conn:
            return conn.execute(self.__scripts["select by id_company"], {"company_id": my_params}).fetchall()

    def delete(self, id):
        with self.engine.connect() as conn:
            conn.execute(self.__scripts["delete by id"], {"id_to_delete": id})


    def create(self, first_name, last_name, middle_name, company_id, email, phone):
        with self.engine.connect() as conn:
            conn.execute(self.__scripts["insert new"], {"first_name": first_name, "last_name": last_name, "middle_name": middle_name, "company_id": company_id, "email": email, "phone": phone })
            self.engine.dispose()

    def get_max_id(self):
        with self.engine.connect() as conn:
            return conn.execute(self.__scripts["get max id"]).fetchall()[0][0]