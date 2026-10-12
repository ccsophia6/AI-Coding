-- ============================================
-- 3.10.4 SQLite 基本操作练习（对应教材第3章）
-- 执行方式: sqlite3 example.db ".read students.sql"
-- ============================================

-- ===== 1. 创建 students 表 =====
DROP TABLE IF EXISTS students;  -- 为便于重复运行脚本，先删除旧表
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    major TEXT,
    enrollment_date TEXT
);

-- ===== 2. 插入数据 =====
INSERT INTO students (id, name, age, major, enrollment_date) VALUES (1, '张三', 20, '计算机科学与技术', '2024-09-01');
INSERT INTO students (id, name, age, major, enrollment_date) VALUES (2, '李四', 21, '软件工程', '2023-09-01');
INSERT INTO students (id, name, age, major, enrollment_date) VALUES (3, '王五', 19, '人工智能', '2024-09-01');

-- ===== 3. 查看表结构 =====
.tables
.schema students
PRAGMA table_info(students);

-- ===== 4. 查询数据（先设置友好输出格式）=====
.mode column
.headers on
SELECT * FROM students;

-- 条件查询：年龄大于等于20岁的学生
SELECT name, age FROM students WHERE age >= 20;

-- ===== 5. 更新数据：将1号学生的专业修改为"数据科学" =====
UPDATE students SET major = '数据科学' WHERE id = 1;
SELECT * FROM students;

-- ===== 6. 删除数据：删除编号为3的学生记录 =====
DELETE FROM students WHERE id = 3;
SELECT * FROM students;
