CREATE TABLE ip_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip VARCHAR(255) NOT NULL,
    inbound INT NOT NULL,
    outbound INT NOT NULL,
    country VARCHAR(255) NOT NULL,
    country_code VARCHAR(255) NOT NULL,
    isp VARCHAR(255) NOT NULL,
    status INT NOT NULL
);

CREATE TABLE vpn_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_id INT,
    vpn_name VARCHAR(255),
    vpn_url VARCHAR(255),
    vpn_source_url VARCHAR(255),
    socket_type VARCHAR(255),
    confirmed_time DATETIME,
    FOREIGN KEY (data_id) REFERENCES ip_data(id)
);

CREATE TABLE category_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_id INT,
    confirmed_time DATETIME,
    detect_reason VARCHAR(255),
    detect_source INT,
    detect_type VARCHAR(255),
    detect_cnt INT,
    FOREIGN KEY (data_id) REFERENCES ip_data(id)
);