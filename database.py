import psycopg2

con = psycopg2.connect(
  database="NEFAZ",
  user="postgres",
  password="postgres",
  host="localhost",
  port="5432"
)

cur = con.cursor()

# cur.execute("""CREATE TABLE New_January (
#             id SERIAL PRIMARY KEY,
#             model_id INT,
#             plan_id INT,
#             assembly_day INT,
#             assembly_month INT,
#             welding_day INT,
#             welding_month INT,
#             change_id INT,
#             FOREIGN KEY (model_id) REFERENCES model_directory (id),
#             FOREIGN KEY (plan_id) REFERENCES User_Directory (id),
#             FOREIGN KEY (change_id) REFERENCES User_Directory (id));""")

# cur.execute("""ALTER TABLE user_directory ADD
#             change BOOLEAN
#             plan BOOLEAN
#             assembly BOOLEAN,
#             welding BOOLEAN,
#             staff_member VARCHAR(255),
#             login VARCHAR(255),
#             password VARCHAR(255),
#             date_of_creation DATE,
#             units VARCHAR(255);""")


# cur.execute("""CREATE TABLE model_directory (
#               id SERIAL PRIMARY KEY,
#               model VARCHAR(255) PRIMARY KEY);
#             """)

# model_id = int(input())
# plan_id = int(input())
# assembly_day = int(input())
# assembly_month = int(input())
# welding_day = int(input())
# welding_month = int(input())
# change_id = int(input())
#
#
# cur.execute("""insert into new_january (model_id, plan_id, assembly_day, assembly_month, welding_day, welding_month, change_id) values (%s,%s,%s,%s,%s,%s,%s)""", (model_id, plan_id, assembly_day, assembly_month, welding_day, welding_month, change_id))

# cur.execute("""CREATE TABLE users (
#             id SERIAL PRIMARY KEY,
#             user_name VARCHAR(255),
#             password VARCHAR(255))""")


# cur.execute("""UPDATE new_january SET model_id = %s, plan_id = %s, assembly_day = %s, assembly_month = %s,
#         welding_day = %s, welding_month = %s, change_id = %s where id = 1""",
#             (model_id, plan_id, assembly_day, assembly_month, welding_day, welding_month, change_id))

# model = input()
# cur.execute("insert into model_directory (model) values (%s)", (model,))

# cur.execute("""ALTER TABLE user_directory ADD units VARCHAR(255);""")

# cur.execute("""ALTER TABLE model_directory ADD title VARCHAR(255);""")

# change = input()
# plan = input()
# assembly = input()
# welding = input()
# staff_member = input()
# login = input()
# password = input()
# date_of_creation = input()
# units = input()
# ids = input()
# cur.execute("""UPDATE user_directory SET change = %s, plan = %s, assembly = %s, welding = %s,
#         staff_member = %s, login = %s, password = %s, date_of_creation = %s, units = %s where id=%s""",
#                          (change, plan, assembly, welding, staff_member, login, password, date_of_creation, units, ids))


# cur.execute("""insert into user_directory (change, plan, assembly, welding, staff_member, login,
#     password, date_of_creation, units) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
#                    (change, plan, assembly, welding, staff_member, login, password, date_of_creation, units))


# cur.execute("""CREATE USER KO WITH LOGIN PASSWORD '55'""")

# cur.execute("""SELECT * FROM model_directory""")
#
# print(cur.fetchall())

# designation = input()
# model = input()
# title = input()
# # ids = input()
# # cur.execute("""UPDATE model_directory SET designation = %s, model = %s, title = %s
# #                     where id=%s""", (designation, model, title, ids))
#
# cur.execute("""INSERT INTO model_directory (designation, model, title) VALUES (%s,%s,%s)""",
#             (designation, model, title))

id = '6'
cur.execute("""SELECT change, plan, assembly, welding from user_directory WHERE id=%s""", (id))
all = cur.fetchone()
print([all])

if True in all:
  print('yes')
else:
  print('ni')


# cur.execute("""GRANT UPDATE %s on user_directory to %s WHERE """)


con.commit()


psycopg2.errors.InsufficientPrivilege