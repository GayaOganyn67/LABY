import requests

### Задача 1

def get_all_students_json():
    req = requests.get("http://127.0.0.1:80/students")
    return req.json()
    

def get_all_students():
    req_json = get_all_students_json()
    res = []
    for s in req_json:
        res.append(s['name'])
    return res

def get_student_by_id(id):
    req_json = get_all_students_json()
    for s in req_json:
        if s['id'] == id:
            return s
    return None

### Задача 2

def get_largest_id():
    req_json = get_all_students_json()
    return max([s['id'] for s in req_json])

def add_student(id, name, age, major):
    student_data = {'id': id, 'name': name, 'age': age, 'major': major}
    response = requests.post("http://127.0.0.1:80/students", json=student_data)
    return response.json()

### Задача 3

def update_student(id, name, age, major):
    student_data = {'name': name, 'age': age, 'major': major}
    res = requests.put("http://127.0.0.1:80/students/{0}".format(id), student_data)
    return res.json()
    

### Проверки
print(get_all_students())
#print(get_student_by_id(2))

# print(add_student(get_largest_id() + 1, 'Глеб', 17, 'Математика'))

#print(update_student(2, "Дима", 25, "Математика"))




