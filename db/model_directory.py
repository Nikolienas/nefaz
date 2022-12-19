import sys
import psycopg2
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QLineEdit
from PyQt5 import QtGui

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        # подключить базу данных
        self.con()
        # параметры окна
        self.setGeometry(425, 100, 500, 600)
        self.setWindowTitle('Справочник моделей')
        self.tb = Tb(self)
        # кнопка "обновить"
        self.btn = QPushButton('Обновить', self)
        self.btn.resize(150, 40)
        self.btn.move(300, 10)
        self.btn.clicked.connect(self.upd)
        # здесь идентификатор
        self.idp = QLineEdit("Идентификатор", self)
        self.idp.resize(150, 40)
        self.idp.move(300, 60)
        self.idp.setReadOnly(True)
        # здесь модель
        self.model = QLineEdit(self)
        self.model.resize(150, 40)
        self.model.move(300, 110)
        # кнопка добавить запись
        self.btn = QPushButton('Добавить', self)
        self.btn.resize(150, 40)
        self.btn.move(300, 210)
        self.btn.clicked.connect(self.ins)
        # кнопка изменить запись
        self.btn = QPushButton('Изменить', self)
        self.btn.resize(150, 40)
        self.btn.move(300, 260)
        self.btn.clicked.connect(self.refresh)
        # кнопка удалить запись
        self.btn = QPushButton('Удалить', self)
        self.btn.resize(150, 40)
        self.btn.move(300, 310)
        self.btn.clicked.connect(self.dels)

    # соединение с базой данных
    def con(self):
        self.conn = psycopg2.connect(user="postgres",
                                     password="postgres",
                                     host="localhost",
                                     port="5432",
                                     database="NEFAZ")
        self.cur = self.conn.cursor()

    # обновить таблицу и поля
    def upd(self):
        self.conn.commit()
        self.tb.updt()
        self.idp.setText('')
        self.model.setText('')
    # добавить таблицу новую строку
    def ins(self):
        model = self.model.text()
        try:
            self.cur.execute("insert into model_directory (model) values (%s)", (model))
        except:
            pass
        self.upd()

    # удалить из таблицы строку
    def dels(self):
        try:
            ids = int(self.idp.text())  # идентификатор строки
        except:
            return
        self.cur.execute("delete from model_directory where id=%s", (ids,))
        self.upd()

    def refresh(self):
        model = self.model.text()
        try:
            ids = int(self.idp.text())  # идентификатор строки
        except:
            return
        self.cur.execute("""UPDATE model_directory SET model = %s where id=%s""", (model, ids))
        self.upd()


# класс - таблица
class Tb(QTableWidget):
    def __init__(self, wg):
        self.wg = wg  # запомнить окно, в котором эта таблица показывается
        super().__init__(wg)
        self.setGeometry(10, 10, 280, 500)
        self.setColumnCount(2)
        self.verticalHeader().hide();
        self.updt()  # обновить таблицу
        self.setEditTriggers(QTableWidget.NoEditTriggers)  # запретить изменять поля
        self.cellClicked.connect(self.cellClick)  # установить обработчик щелча мыши в таблице

    # обновление таблицы
    def updt(self):
        self.clear()
        self.setRowCount(0);
        self.setHorizontalHeaderLabels(['id', 'Модель'])  # заголовки столцов
        self.wg.cur.execute("select * from model_directory order by id asc")
        rows = self.wg.cur.fetchall()
        i = 0
        for elem in rows:
            self.setRowCount(self.rowCount() + 1)
            j = 0
            for t in elem:  # заполняем внутри строки
                self.setItem(i, j, QTableWidgetItem(str(t).strip()))
                j += 1
            i += 1
        self.resizeColumnsToContents()

    # обработка щелчка мыши по таблице
    def cellClick(self, row, col):  # row - номер строки, col - номер столбца
        self.wg.idp.setText(self.item(row, 0).text())
        self.wg.model.setText(self.item(row, 1).text().strip())



app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

