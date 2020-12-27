worker_dict = {"wage": 50000, "bonus": 10000}


class Worker:
    def __init__(self):
        self.name = 'Иван'
        self.surname = 'Иванов'
        self.position = 'Менеджер'
        self._income = worker_dict


class Position(Worker):
    def get_full_name(self):
        fio = self.name + ' ' + self.surname
        print(f'ФИО сотрудника: {fio}')

    def get_total_income(self):
        income = self._income["wage"] + self._income["bonus"]
        print(f'Доход сотрудника составляет : {income}')


worker = Position()
print(worker.name, worker.surname, worker.position, worker._income)
worker.get_full_name()
worker.get_total_income()
