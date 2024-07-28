from db import db
db_instance = None
study_buddy_instance = None

def set_instances(study_buddy, database):
    global db_instance
    global study_buddy_instance

    study_buddy_instance = study_buddy
    db_instance = database

def get_db() -> db:
    return db_instance

def join_threads():
    study_buddy_instance.stop_event.set()
    # study_buddy_instance.r.join()
    # study_buddy_instance.m.join()
