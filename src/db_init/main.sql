-- Create the Users table
CREATE TABLE Users (
  corporate_email VARCHAR(255),
  password VARCHAR(255)
);

-- Create the EmailMessages table
CREATE TABLE EmailMessages (
  sender_email INT PRIMARY KEY,
  corporate_email VARCHAR(255),
  message_content VARCHAR(255),
  timestamp TIMESTAMP,
  other_message_attributes VARCHAR(255),
  FOREIGN KEY (corporate_email) REFERENCES Users(corporate_email)
);

-- Create the EmailAddresses table
CREATE TABLE EmailAddresses (
  corporate_email VARCHAR(255),
  email_address VARCHAR(255),
  PRIMARY KEY (corporate_email),
  FOREIGN KEY (corporate_email) REFERENCES Users(corporate_email)
);

CREATE TABLE EmailAttributes (
  corporate_email VARCHAR(255),
  name VARCHAR(255),
  role VARCHAR(255),
  description VARCHAR(255),
  authority VARCHAR(255),
  department VARCHAR(255),
  FOREIGN KEY (corporate_email) REFERENCES EmailAddresses(corporate_email)
);