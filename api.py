from flask_restful import Resource
from flask import request, jsonify
from sqlalchemy.orm.session import sessionmaker
from models import GroupModel, StudentModel, CourseModel, engine

session = sessionmaker(bind=engine)()


class Groups(Resource):
    def get(self, version):
        groups = session.query(GroupModel).all()
        groups_list = []
        for group in groups:
            new_group = {'id': group.id, 'group_name': group.name}
            groups_list.append(new_group)

        return jsonify(groups_list)

    def post(self, version):
        data = request.get_json()
        new_group = GroupModel(name=data['name'])
        session.add(new_group)
        session.commit()

        return jsonify({'id': new_group.id, 'group_name': new_group.name})

    def put(self, version):
        data = request.get_json()
        updating_group = session.query(GroupModel).where(GroupModel.id == data['id']).first()
        updating_group.name = data['name']
        session.commit()

        return jsonify({'id': updating_group.id, 'group_name': updating_group.name})

    def delete(self, version):
        data = request.get_json()
        deleting_group = session.get(GroupModel, data['id'])
        session.delete(deleting_group)
        session.commit()

        return jsonify({'id': deleting_group.id, 'group_name': deleting_group.name})


class Students(Resource):
    def get(self, version):
        students = session.query(StudentModel).all()
        students_list = []
        for student in students:
            student_courses = []

            for course in student.courses:
                student_courses.append(course.name)

            new_student = {'id': student.id,
                           'first_name': student.first_name,
                           'last_name': student.last_name,
                           'group': student.group_id,
                           'courses': student_courses}
            students_list.append(new_student)

        return jsonify(students_list)

    def post(self, version):
        data = request.get_json()

        new_student = StudentModel(
            first_name=data['first_name'],
            last_name=data['last_name'],
            group_id=data['group_id']
        )

        session.add(new_student)
        session.commit()

        if 'courses' in data:
            for course in data['courses']:
                course_to_add = session.query(CourseModel).filter_by(id=course).first()
                new_student.courses.append(course_to_add)

            session.commit()

        return jsonify({
            'id': new_student.id,
            'first_name': new_student.first_name,
            'last_name': new_student.last_name,
            'group_id': new_student.group_id,
            'courses': new_student.courses
        })

    def put(self, version):
        data = request.get_json()
        updating_student = session.query(StudentModel).where(StudentModel.id == data['id']).first()
        updating_student.first_name = data['first_name']
        updating_student.last_name = data['last_name']
        updating_student.group_id = data['group_id']
        session.commit()

        if 'delete_courses' in data:
            for course in data['delete_courses']:
                course_to_remove = session.query(CourseModel).filter_by(id=course).first()
                updating_student.courses.remove(course_to_remove)

            session.commit()

        if 'add_courses' in data:
            for course in data['add_courses']:
                course_to_add = session.query(CourseModel).filter_by(id=course).first()
                updating_student.courses.append(course_to_add)

            session.commit()

        return jsonify({
            'id': updating_student.id,
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'group_id': data['group_id']
        })

    def delete(self, version):
        data = request.get_json()
        student_to_delete = session.get(StudentModel, data['id'])
        session.delete(student_to_delete)
        session.commit()

        return jsonify({
            'id': student_to_delete.id,
            'first_name': student_to_delete.first_name,
            'last_name': student_to_delete.last_name,
            'group_id': student_to_delete.group_id
        })


class Courses(Resource):
    def get(self, version):
        courses = session.query(CourseModel).all()
        courses_list = []
        for course in courses:
            new_course = {'id': course.id, 'course_name': course.name}
            courses_list.append(new_course)

        # Return json object
        return jsonify(courses_list)

    def post(self, version):
        data = request.get_json()

        new_course = CourseModel(
            name=data['name'],
            description=data['description']
        )

        session.add(new_course)
        session.commit()

        if 'students' in data:
            for student in data['students']:
                student_to_add = session.query(StudentModel).filter_by(id=student).first()
                new_course.students.append(student_to_add)

            session.commit()

        return jsonify({
            'id': new_course.id,
            'name': new_course.name,
            'description': new_course.description
        })

    def put(self, version):
        data = request.get_json()
        updating_course = session.query(CourseModel).where(CourseModel.id == data['id']).first()
        updating_course.name = data['name']
        session.commit()

        return jsonify({
            'id': updating_course.id,
            'name': updating_course.name
        })

    def delete(self, version):
        data = request.get_json()
        course_to_delete = session.get(CourseModel, data['id'])
        session.delete(course_to_delete)
        session.commit()

        return jsonify({'id': course_to_delete.id, 'name': course_to_delete.name})
