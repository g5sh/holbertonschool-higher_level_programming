-- creates the MySQL server user
CRATE USER IF NOT EXISTS 'user_0d_1'@localhost;
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@localhost;
