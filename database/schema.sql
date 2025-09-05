CREATE TABLE donor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    blood_type VARCHAR(3) NOT NULL,
    last_donation_date DATE
);

CREATE TABLE blood_inventory (
    id INT PRIMARY KEY AUTO_INCREMENT,
    blood_type VARCHAR(3) NOT NULL,
    quantity INT NOT NULL
);

CREATE TABLE blood_request (
    id INT PRIMARY KEY AUTO_INCREMENT,
    hospital_name VARCHAR(100) NOT NULL,
    blood_type VARCHAR(3) NOT NULL,
    quantity INT NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending'
);