from app import app

new_group = ''
new_student = ''
new_course = ''


def test_groups_get():
    tester = app.test_client()
    response = tester.get('api/v1/groups')
    groups = response.get_json()
    assert 'group_name' in groups[0] and 'id' in groups[0]
    assert groups[0]['id'] == 1
    assert groups[0]['group_name'] == 'RW-19'
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert {'group_name': 'RW-19', 'id': 1} in response.json


def test_groups_post():
    global new_group
    data = {
        'name': 'post_group'
    }
    tester = app.test_client()
    response = tester.post('api/v1/groups', json=data)
    new_group = response.json['id']
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert {'group_name': 'post_group', 'id': new_group} == response.json


def test_groups_put():
    data = {
        'id': new_group,
        'name': 'put_group'
    }
    tester = app.test_client()
    response = tester.put('api/v1/groups', json=data)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert {'id': new_group, 'group_name': 'put_group'} == response.json


def test_groups_delete():
    data = {
        'id': new_group
    }
    tester = app.test_client()
    response = tester.delete('api/v1/groups', json=data)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert {'id': new_group, 'group_name': 'put_group'} == response.json


def test_students_get():
    tester = app.test_client()
    response = tester.get('api/v1/students')
    groups = response.get_json()
    assert 'first_name' in groups[0] and 'last_name' in groups[0] and 'group' in groups[0]
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert {'courses': ['trigonometry', 'english', 'chemistry'],
            'first_name': 'William',
            'group': 10, 'id': 1,
            'last_name': 'Michael'
            } in response.json


def test_students_post():
    global new_student
    data = {
        'first_name': 'Tester',
        'last_name': 'Testerov',
        'group_id': 1
    }
    tester = app.test_client()
    response = tester.post('api/v1/students', json=data)
    new_student = response.json['id']
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert {'id': new_student,
            'first_name': 'Tester',
            'last_name': 'Testerov',
            'group_id': 1,
            'courses': []
            } == response.json


def test_students_put():
    data = {
        'id': new_student,
        'first_name': 'Sauran',
        'last_name': 'Akhmetzhanov',
        'group_id': 1,
        'add_courses': [1, 2]
    }
    tester = app.test_client()
    response = tester.put('api/v1/students', json=data)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert {'id': new_student,
            'first_name': 'Sauran',
            'last_name': 'Akhmetzhanov',
            'group_id': 1
            } == response.json


def test_students_delete():
    data = {
        'id': new_student
    }
    tester = app.test_client()
    response = tester.delete('api/v1/students', json=data)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert {
        'id': new_student,
        'first_name': 'Sauran',
        'last_name': 'Akhmetzhanov',
        'group_id': 1
    } == response.json


def test_courses_get():
    tester = app.test_client()
    response = tester.get('api/v1/courses')
    groups = response.get_json()
    assert 'course_name' in groups[0] and 'id' in groups[0]
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert {'course_name': 'algebra', 'id': 1} in response.json


def test_courses_post():
    global new_course
    data = {
        'name': 'test_course_post',
        'description': None
    }
    tester = app.test_client()
    response = tester.post('api/v1/courses', json=data)
    new_course = response.json['id']
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert {'id': new_course, 'name': 'test_course_post', 'description': None} == response.json


def test_courses_put():
    data = {
        'id': new_course,
        'name': 'test_course_put'
    }
    tester = app.test_client()
    response = tester.put('api/v1/courses', json=data)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert {'id': new_course, 'name': 'test_course_put'} == response.json


def test_courses_delete():
    data = {
        'id': new_course
    }
    tester = app.test_client()
    response = tester.delete('api/v1/courses', json=data)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert {'id': new_course, 'name': 'test_course_put'} == response.json
