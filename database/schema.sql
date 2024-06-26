CREATE
DATABASE IF NOT EXISTS tax_payment_system;
USE
tax_payment_system;
-- Payment Table
CREATE TABLE `payment`
(
    `id`           INT AUTO_INCREMENT PRIMARY KEY,
    `company`      VARCHAR(255),
    `amount`       FLOAT,
    `payment_date` VARCHAR(255),
    `status`       VARCHAR(255),
    `due_date`     VARCHAR(255),
    `created_at`   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at`   TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX          `idx_company` (`company`),           -- Index on company
    INDEX          `idx_payment_date` (`payment_date`), -- Index on payment date
    INDEX          `idx_due_date` (`due_date`),         -- Index on due date
);
