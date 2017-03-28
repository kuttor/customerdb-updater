### Shows how many projects are in Env and their associated accounts. 

select p.name as "Project", e.name as "Env"
from project p
join xref_projects_in_env xpe on xpe.project_id = p.id
join env e on e.id = xpe.env_id
join xref_projects_in_biz_units xpb on xpb.project_id = 

