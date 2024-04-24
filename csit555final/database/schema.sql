CREATE DATABASE IF NOT EXISTS tax_payment_system;
USE tax_payment_system;
-- Payment Table
CREATE TABLE `payment` (
       `id`           INT AUTO_INCREMENT PRIMARY KEY,
       `company`      VARCHAR(255),
       `amount`       FLOAT,
       `payment_date` DATE,
       `status`       VARCHAR(255),
       `due_date`     DATE,
       `created_at`   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       `updated_at`   TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
