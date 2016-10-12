Users
+--------------+--------------------------------------+------+-----+---------+-------+
| Field        | Type                                 | Null | Key | Default | Extra |
+--------------+--------------------------------------+------+-----+---------+-------+
| loginID      | varchar(32)                          | NO   | PRI | NULL    |       |
| loginSecret  | varchar(256)                         | NO   |     | NULL    |       |
| displayName  | varchar(64)                          | NO   | MUL | NULL    |       |
| email        | varchar(254)                         | NO   | UNI | NULL    |       |
| role         | enum('Student','Instructor','Tutor') | NO   |     | Student |       |
| isSuper      | tinyint(1)                           | NO   |     | 0       |       |
| isActive     | tinyint(1)                           | NO   |     | 0       |       |
| numFailLogin | tinyint(3) unsigned                  | NO   |     | 0       |       |
+--------------+--------------------------------------+------+-----+---------+-------+

UsersStat	

Instructors are associated with courses;                       *
 *   while students/tutors are assoicated with courseOffers.      *
 * Questions are associated with courses;                         *
 *   while assessments are associated with courseOffers.    

Courses;
+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| courseCode  | varchar(15) | NO   | PRI | NULL    |       |
| courseTitle | varchar(50) | NO   |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+
