SELECT * FROM teachers_portal.students;
insert into students(studentName, enrolledInCourseId, grade)
values  ("Maria Jozef", 1, 98),
		("Linda Jones", 2, 89),
        ("John McGrail", 1, 98),
        ("Patty Luna", 2, 78);

select * from teachers_portal.courses;
insert into courses (courseName)
values  ("Database Design"),
		("Calcuslus"),
        ("Physics I");


delimiter $$
CREATE PROCEDURE studentWithGrade()
BEGIN
	SELECT * FROM students LEFT JOIN courses
    ON students.enrolledInCourseID = courses.courseID; 
END $$
delimiter ; 

call studentWithGrade();
 
SELECT * FROM teachers_portal.students;
