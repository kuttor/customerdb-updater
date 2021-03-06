#!/bin/usr/env python
'''
Name   : CustomerDB Updater Tool
Author : Andrew Kuttor
Contact: andrew.kuttor@gmail.com
'''

from MySQLdb import connect


# Executes the initialized query
# arg = query
def execute(query=query):
    with cnx:
        cnx.cursor().cur.execute(query)


# Queries target table to output ID column based on name
# Inputs (table, name)
def select(table, name):
    query = "select id from {table} where name = {name}".format(table, name)
    return query


# Inserts records into BU table
# Columns (id, name)
def insert_into_bu(id, name):
    query = "insert into bu values ({}, {})".format(num, name)
    return query


# Inserts records into contact table
# Columns (id, name, title, phone, email)
def insert_into_contact(name, email):
    query = "insert into contact values ({}, {})".format(contact)
    return query


# Creates many-to-one relationship records for contacts in env
# Columns (contact_id, env_id)
def insert_contacts_into_env(cid, eid):
    query = "insert into bu values ({}, {})".format(num, name)
    return query


# Creates many-to-one relationship records for projects in BU
# Columns (project_id, bu_id)
def insert_projects_into_bu(pid, bid):
    query = "insert into bu values ({}, {})".format(num, name)
    return query


# Columns (project_id, bu_id)
def insert_contacts_into_env(name, env):
    query = "insert into xref_contacts_in_env values\
     (select(table, env), select(table, env))"
    return query


def insert_into_xref(xref_table, name, id_one, id_two):
    query = "insert into {} values ({}, {}) \
    where name = {}".format(xref, id_one, id_two)


def main():
    # Brokers client -> RDS connection
    connect()
    execute()


 if __name__ == "__main__":
    main()