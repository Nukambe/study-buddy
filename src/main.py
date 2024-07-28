import os
import sys
from importlib import reload
import threading
from ui.ui import MainGUI
import ui.ui
from db.db import DB
import db.db
from handler import set_instances

class StudyBuddy:

    def __init__(self) -> None:
        self.file_modifications = {
            "ui": [ui.ui, ui.ui.__file__, 0],
            "db": [db.db, db.db.__file__, 0]
        }
        self.local = threading.local()
        self.stop_event = threading.Event()
        self.ui = None

        self.r = threading.Thread(name="refresh", target=self.refresh)
        self.m = threading.Thread(name="main", target=self.main)
        self.r.daemon = True
        self.m.daemon = True
        self.r.start()
        self.m.start()

    def restart_script(self):
        python = sys.executable
        os.execv(python, [python] + sys.argv)

    def refresh(self):
        for module in self.file_modifications:
            self.file_modifications[module][2] = os.path.getmtime(self.file_modifications[module][1])
        while not self.stop_event.is_set():
            for _import in self.file_modifications:
                module, file, mod_time = self.file_modifications[_import]
                last_mod = os.path.getmtime(file)
                if last_mod > mod_time:
                    print("Reloading", module)
                    reload(module)
                    self.file_modifications[_import][2] = last_mod
                    self.restart_script()
        self.stop_event.wait(1)

    def main(self):
        self.local.db = DB()
        set_instances(study_buddy=self, database=self.local.db)
        self.ui = MainGUI()

if __name__ == "__main__":
    app = StudyBuddy()
    app.m.join()
    app.r.join()
