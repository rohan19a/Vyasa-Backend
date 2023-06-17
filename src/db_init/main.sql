-- Create the Users table
CREATE TABLE Users (
  user_id INT PRIMARY KEY,
  username VARCHAR(255),
  password VARCHAR(255)
);

-- Create the EmailMessages table
CREATE TABLE EmailMessages (
  message_id INT PRIMARY KEY,
  user_id INT,
  message_content VARCHAR(255),
  timestamp TIMESTAMP,
  other_message_attributes VARCHAR(255),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Create the EmailAddresses table
CREATE TABLE EmailAddresses (
  email_id INT PRIMARY KEY,
  user_id INT,
  email_address VARCHAR(255),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Create the EmailAttributes table
CREATE TABLE EmailAttributes (
  attribute_id INT PRIMARY KEY,
  email_id INT,
  name VARCHAR(255),
  role VARCHAR(255),
  description VARCHAR(255),
  authority VARCHAR(255),
  department VARCHAR(255),
  FOREIGN KEY (email_id) REFERENCES EmailAddresses(email_id)
);
