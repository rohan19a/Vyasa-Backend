INSERT INTO Users (user_id, username, password)
VALUES (1, 'JohnDoe', 'password123');


INSERT INTO EmailAddresses (email_id, user_id, email_address)
VALUES (1, 1, 'johndoe@example.com');


INSERT INTO EmailAttributes (attribute_id, email_id, name, role, description, authority, department)
VALUES (1, 1, 'John Doe', 'Manager', 'Description', 'Authority', 'Department');
