-- Convert datebase to UTF8;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- convert the table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET  utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the specific field/column to UTF8
ALTER TABLE hbtn_0c_0.first_table MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
