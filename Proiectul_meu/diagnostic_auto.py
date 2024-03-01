from tkinter import messagebox
import obd
import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("Dark")
appWidth, appHeight = 600, 700


class DiagnosticApp:
    def __init__(self, master):
        try:
            self.connection = obd.OBD(portstr="COM1", baudrate=9600)
        except Exception as e:
            print("Eroare la inițializarea conexiunii:", e)
        self.master = master
        master.geometry(f"{appWidth}x{appHeight}")
        master.title("Diagnostic Auto")

        obd.logger.setLevel(obd.logging.DEBUG)

        self.frame = ctk.CTkFrame(master=master)
        self.frame.pack(pady=10, padx=10)

        self.connection = obd.OBD()

        self.info_display = ctk.CTkTextbox(master=master, wrap=tk.WORD, width=80, height=20)
        self.info_display.pack(padx=10, pady=10, side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.info_display.configure(state=tk.DISABLED)

        self.setup_ui()

    def setup_ui(self):
        self.create_button("Citeste Informatia la Senzor", self.read_sensor, side=tk.LEFT)
        self.create_button("Diagnostica Auto", self.perform_diagnosis, side=tk.LEFT)
        self.create_button("Sterge Erorile", self.perform_delete, side=tk.LEFT)

    def create_button(self, text, command, side):
        button = ctk.CTkButton(master=self.frame, text=text, command=command)
        button.pack(side=side, padx=5, pady=5)

    def read_sensor(self):
        raspuns = self.connection.query(obd.commands.RPM)
        result = f"RPM: {raspuns.value.magnitude}" if not raspuns.is_null() else "Nu s-a putut citi RPM"
        self.update_info_display(result)

    def perform_diagnosis(self):
        if not self.connection.is_connected():
            result = "Nu s-a stabilit conexiunea."
        else:
            r = self.connection.query(obd.commands.RPM)
            result = f"Turații motorului: {r.value.magnitude}" if not r.is_null() else "Nu s-a putut citi RPM"
        self.update_info_display(result)

    def perform_delete(self):
        if not self.connection.is_connected():
            result = "Nu s-a stabilit conexiunea."
        else:
            dtc_cmd = obd.commands.GET_DTC
            raspuns = self.connection.query(dtc_cmd)
            if not raspuns.is_null() and raspuns.value:
                result = "Există coduri de eroare. Rezolvați problemele și apoi încercați din nou."
            else:
                clear_cmd = obd.commands.CLEAR_DTC
                warning_message = (
                    "ATENȚIE: Asigurați-vă că vehiculul este într-o stare sigură și că motorul este oprit pentru "
                    "a șterge erorile. Sunteți sigur că doriți să ștergeți codurile de eroare?"
                )
                confirmation = messagebox.askyesno("Avertizare", warning_message)

                if confirmation:
                    answer = self.connection.query(clear_cmd)
                    if answer.is_null():
                        result = "Nu s-a putut șterge lumina de bord."
                    else:
                        result = "Lumina de pe bord a fost ștearsă."
                else:
                    result = "Operație anulată."

        self.update_info_display(result)

    def update_info_display(self, text):
        self.info_display.configure(state=tk.NORMAL)
        self.info_display.insert(tk.END, text + "\n")
        self.info_display.configure(state=tk.DISABLED)


app = ctk.CTk()
diagnostic_app = DiagnosticApp(app)
app.mainloop()
diagnostic_app.connection.close()
