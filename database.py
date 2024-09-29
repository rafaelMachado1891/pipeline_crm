import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
from dotenv import load_dotenv
import os

from sqlalchemy import select, bindparam
scalar_subq = (
     select(user_table.c.id)
     .where(user_table.c.name == bindparam("username"))
     .scalar_subquery()
 )

with engine.connect() as conn:
     result = conn.execute(
         insert(address_table).values(user_id=scalar_subq),
         [
             {
                 "username": "spongebob",
                 "email_address": "spongebob@sqlalchemy.org",
             },
             {"username": "sandy", "email_address": "sandy@sqlalchemy.org"},
             {"username": "sandy", "email_address": "sandy@squirrelpower.org"},
         ],
     )
     conn.commit()
BEGIN (implicit)
INSERT INTO address (user_id, email_address) VALUES ((SELECT user_account.id
FROM user_account
WHERE user_account.name = ?), ?)
[...] [('spongebob', 'spongebob@sqlalchemy.org'), ('sandy', 'sandy@sqlalchemy.org'),
('sandy', 'sandy@squirrelpower.org')]
COMMIT