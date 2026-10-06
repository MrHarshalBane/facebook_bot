import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import time
import sys

# Selenium imports with error handling
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False


class FacebookBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Facebook Bot by Harshal")
        self.root.geometry("820x680")
        self.root.configure(bg="#434343")
        self.root.resizable(True, True)

        self.setup_ui()

    def setup_ui(self):
        # Header / Title "Welcome"
        title_frame = tk.Frame(self.root, bg="#434343")
        title_frame.pack(pady=(20, 15))

        title_label = tk.Label(
            title_frame,
            text="Welcome",
            font=("Segoe UI", 22, "bold"),
            bg="#ccff00",
            fg="#000000",
            padx=35,
            pady=4
        )
        title_label.pack()

        # "Type the text :-" Label
        text_lbl_frame = tk.Frame(self.root, bg="#434343")
        text_lbl_frame.pack(pady=(5, 5))

        text_lbl = tk.Label(
            text_lbl_frame,
            text="Type the text :-",
            font=("Segoe UI", 12, "bold"),
            bg="#00e5ff",
            fg="#000000",
            padx=18,
            pady=3
        )
        text_lbl.pack()

        # Text Area Box
        text_box_frame = tk.Frame(self.root, bg="#434343", padx=40)
        text_box_frame.pack(fill="x", pady=5)

        self.msg_text = tk.Text(
            text_box_frame,
            height=6,
            font=("Consolas", 11),
            bg="#ffffff",
            fg="#000000",
            relief="solid",
            bd=2
        )
        self.msg_text.insert("1.0", "Hi this is a test message from Harshal's Facebook Bot")
        self.msg_text.pack(fill="x")

        # Form Inputs Frame
        form_frame = tk.Frame(self.root, bg="#434343", padx=40)
        form_frame.pack(fill="x", pady=15)

        # Row 1: Enter usernames
        row1 = tk.Frame(form_frame, bg="#434343")
        row1.pack(fill="x", pady=6)

        lbl_target = tk.Label(
            row1,
            text="Enter usernames:-",
            font=("Segoe UI", 11, "bold"),
            bg="#00e5ff",
            fg="#000000",
            padx=12,
            pady=2
        )
        lbl_target.pack(side="left", padx=(0, 15))

        self.entry_targets = tk.Entry(
            row1,
            font=("Segoe UI", 11),
            bg="#ffffff",
            fg="#000000",
            relief="solid",
            bd=2
        )
        self.entry_targets.insert(0, "john.doe alex99 mark.zuckerberg")
        self.entry_targets.pack(side="left", fill="x", expand=True)

        # Row 2: Credentials (Username & Password side-by-side)
        row2 = tk.Frame(form_frame, bg="#434343")
        row2.pack(fill="x", pady=6)

        # Left: Your username
        lbl_user = tk.Label(
            row2,
            text="Your username:-",
            font=("Segoe UI", 11, "bold"),
            bg="#00e5ff",
            fg="#000000",
            padx=12,
            pady=2
        )
        lbl_user.pack(side="left", padx=(0, 10))

        self.entry_user = tk.Entry(
            row2,
            font=("Segoe UI", 11),
            bg="#ffffff",
            fg="#000000",
            relief="solid",
            bd=2,
            width=22
        )
        self.entry_user.insert(0, "harshal.test")
        self.entry_user.pack(side="left", padx=(0, 20))

        # Right: Your password
        lbl_pass = tk.Label(
            row2,
            text="Your password:-",
            font=("Segoe UI", 11, "bold"),
            bg="#00e5ff",
            fg="#000000",
            padx=12,
            pady=2
        )
        lbl_pass.pack(side="left", padx=(0, 10))

        self.entry_pass = tk.Entry(
            row2,
            font=("Segoe UI", 11),
            bg="#ffffff",
            fg="#000000",
            relief="solid",
            bd=2,
            show="*",
            width=22
        )
        self.entry_pass.pack(side="left")

        # Submit Button
        btn_frame = tk.Frame(self.root, bg="#434343")
        btn_frame.pack(pady=10)

        self.btn_submit = tk.Button(
            btn_frame,
            text="SUBMIT",
            font=("Segoe UI", 13, "bold"),
            bg="#ffffff",
            fg="#000000",
            relief="solid",
            bd=2,
            padx=25,
            pady=2,
            cursor="hand2",
            command=self.on_submit
        )
        self.btn_submit.pack()

        # Status / Console Log Window
        log_frame = tk.Frame(self.root, bg="#434343", padx=40)
        log_frame.pack(fill="both", expand=True, pady=(10, 20))

        self.log_area = scrolledtext.ScrolledText(
            log_frame,
            font=("Consolas", 10),
            bg="#1e1e1e",
            fg="#00ff66",
            height=8
        )
        self.log_area.pack(fill="both", expand=True)

        self.log("[SYSTEM] Facebook Bot by Harshal loaded successfully.")
        if not SELENIUM_AVAILABLE:
            self.log("[NOTICE] Selenium module is not installed yet. Run 'pip install selenium' for full automated browser execution.")

    def log(self, text):
        self.log_area.insert(tk.END, f"{text}\n")
        self.log_area.see(tk.END)

    def on_submit(self):
        message = self.msg_text.get("1.0", tk.END).strip()
        targets = [t for t in self.entry_targets.get().strip().split(" ") if t]
        username = self.entry_user.get().strip()
        password = self.entry_pass.get().strip()

        if not message or not targets or not username or not password:
            messagebox.showwarning("Missing Fields", "Please complete all fields before submitting.")
            return

        self.btn_submit.config(state="disabled")
        threading.Thread(target=self.run_bot, args=(message, targets, username, password), daemon=True).start()

    def run_bot(self, message, targets, username, password):
        self.log(f"\n--- STARTING BOT PROCESS ---")
        self.log(f"[INFO] Facebook User: {username}")
        self.log(f"[INFO] Target Accounts ({len(targets)}): {', '.join(targets)}")
        self.log(f"[INFO] Message: '{message[:30]}...'")

        if SELENIUM_AVAILABLE:
            try:
                self.log("[BROWSER] Launching Chrome driver...")
                options = Options()
                options.add_argument("--disable-notifications")
                options.add_argument("--start-maximized")

                driver = webdriver.Chrome(options=options)
                driver.get("https://www.facebook.com/")
                time.sleep(2)

                self.log("[AUTH] Logging in to Facebook...")
                email_elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
                pass_elem = driver.find_element(By.ID, "pass")

                email_elem.send_keys(username)
                pass_elem.send_keys(password)
                pass_elem.send_keys(Keys.RETURN)
                time.sleep(5)

                for target in targets:
                    self.log(f"[MESSAGE] Navigating to target user: {target}...")
                    driver.get(f"https://www.facebook.com/messages/t/{target}")
                    time.sleep(4)

                    try:
                        msg_box = WebDriverWait(driver, 8).until(
                            EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]'))
                        )
                        msg_box.send_keys(message)
                        msg_box.send_keys(Keys.RETURN)
                        self.log(f"[SUCCESS] Sent message to {target}!")
                    except Exception as e:
                        self.log(f"[ERROR] Could not send message to {target}: {e}")

                    time.sleep(2)

                driver.quit()
                self.log("[COMPLETE] Process finished.")
            except Exception as ex:
                self.log(f"[EXCEPTION] Automation error: {ex}")
        else:
            # Demonstration / Fallback simulation loop
            self.log("[SIMULATION] Running bot simulation...")
            for t in targets:
                time.sleep(1.5)
                self.log(f"[SIMULATION] Message delivered successfully to @{t}")
            self.log("[COMPLETE] Bot execution complete (Install selenium to send real messages).")

        self.root.after(0, lambda: self.btn_submit.config(state="normal"))


if __name__ == "__main__":
    root = tk.Tk()
    app = FacebookBotApp(root)
    root.mainloop()
