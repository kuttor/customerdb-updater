# SQL script
# Inserts project into env

SET @project = "ProjectName"
SET @env = "EnvName"

INSERT INTO xref_projects_in_env (env_id, project_id)
VALUES (
	(SELECT id FROM env where name = @env), 
	(SELECT id FROM project where name = @project)
)