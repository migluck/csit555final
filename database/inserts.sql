USE tax_payment_system;
DELETE FROM payment;
INSERT INTO payment (company, amount, payment_date, status, due_date) VALUES ('derm', 4100.00, '2023-09-26', 'paid', '2024-01-15');
INSERT INTO payment (company, amount, payment_date, status, due_date) VALUES ('derm', 4100.00, '2023-10-12', 'paid', '2024-01-15');
INSERT INTO payment (company, amount, payment_date, status, due_date) VALUES ('tek', 15200.00, '2023-06-09', 'paid', '2023-06-15');
INSERT INTO payment (company, amount, payment_date, status, due_date) VALUES ('tek', 15200.00, '2023-07-12', 'paid', '2023-09-15');
INSERT INTO payment (company, amount, payment_date, status, due_date) VALUES ('tek', 11400.00, '2023-08-11', 'paid', '2023-09-15');
INSERT INTO payment (company, amount, payment_date, status, due_date) VALUES ('tek', 14440.00, '2023-09-21', 'paid', '2024-01-15');
INSERT INTO payment (company, amount, payment_date, status, due_date) VALUES ('tek', 15200.00, '2023-10-18', 'paid', '2024-01-15');
INSERT INTO payment (company, amount, payment_date, status, due_date) VALUES ('tek', 23520.00, NULL, 'unpaid', '2024-01-15');
INSERT INTO payment (company, amount, payment_date, status, due_date) VALUES ('tek', 16800.00, NULL, 'unpaid', '2024-01-15');
INSERT INTO payment (company, amount, payment_date, status, due_date) VALUES ('tek', 16800.00, NULL, 'unpaid', '2024-01-15');
INSERT INTO payment (company, amount, payment_date, status, due_date) VALUES ('tek', 16800.00, NULL, 'unpaid', '2024-01-15');


