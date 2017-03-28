#! 
# SQl Script  
# Inserts contact record into CustomerDB
 =
SET @name  = "full name"  
SET @title = "title"  
SET @email = "intuit email"  
SET @phone = "contact phone" 
 
INSERT INTO contact (name, title, email, phone) 
VALUES (@name, @title, @email, @phone);

# Insert record into BU
SET @projectId = "Id"
SET @contactId = "Id"

INSERT INTO xref_contact_ in_project (project_id, contact_id)
VALUES (@projectId, @contactId);

# Insert record into BU
SET @projectId = "Id"
SET @buId      = "Id"

INSERT INTO xref_projects_in_bu (project_id, contact_id)
VALUES (@projectId, @contactId);




