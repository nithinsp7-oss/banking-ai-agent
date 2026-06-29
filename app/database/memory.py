from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3


def get_memory():

    conn = sqlite3.connect(
        "banking_memory.db",
        check_same_thread=False
    )

    memory = SqliteSaver(conn)

    return memory