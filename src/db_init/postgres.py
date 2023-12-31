import psycopg2

create_users_table = """
CREATE TABLE Users (
  user_id INT PRIMARY KEY,
  username VARCHAR(255),
  password VARCHAR(255)
);
"""

create_email_messages_table = """
CREATE TABLE EmailMessages (
  message_id INT PRIMARY KEY,
  user_id INT,
  message_content VARCHAR(255),
  timestamp TIMESTAMP,
  other_message_attributes VARCHAR(255),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
"""

create_email_addresses_table = """
CREATE TABLE EmailAddresses (
  email_id INT PRIMARY KEY,
  user_id INT,
  email_address VARCHAR(255),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
"""

create_email_attributes_table = """
CREATE TABLE EmailAttributes (
  email_address VARCHART(255) PRIMARY KEY,
  email_id INT,
  name VARCHAR(255),
  role VARCHAR(255),
  description VARCHAR(255),
  authority VARCHAR(255),
  department VARCHAR(255),
  FOREIGN KEY (email_id) REFERENCES EmailAddresses(email_id)
);
"""



