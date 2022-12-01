from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship


DATABASE_URL = "postgresql://sauran:medieval@localhost:5432/school"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
session = sessionmaker(bind=engine)()


class GroupModel(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    students = relationship('StudentModel', back_populates='group')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Group %r>' % self.name


association_table = Table(
    "courses_students",
    Base.metadata,
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
    Column("student_id", ForeignKey("students.id"), primary_key=True),
)


class StudentModel(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
    courses = relationship("CourseModel", secondary=association_table, back_populates='students')
    group = relationship('GroupModel', back_populates='students')

    def __init__(self, first_name, last_name, group_id):
        self.first_name = first_name
        self.last_name = last_name
        self.group_id = group_id

    def __repr__(self):
        return '<Student %r %r, from group # %r>' % (self.first_name, self.last_name, self.group_id)


class CourseModel(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False, unique=True)
    description = Column(String())
    students = relationship('StudentModel', secondary=association_table, back_populates='courses')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Course %r, %r>' % (self.name, self.description)


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
