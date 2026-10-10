# Facebook Bot by Harshal 🚀

A Python & Web automated messaging application for Facebook inspired by the Instagram Bot UI layout.

---

## 📁 File Structure (Flat Directory for GitHub Pages)
All files are placed directly in the root directory (no nested subfolders) so uploading directly to your GitHub repository works seamlessly with GitHub Pages!

- `index.html` — Web UI for GitHub Pages (Styled exactly like the desktop screenshot).
- `fb_bot.py` — Python Desktop GUI (Tkinter + Selenium automated Facebook messaging bot).
- `requirements.txt` — Python dependencies needed for local desktop execution.
- `README.md` — Project documentation and setup guide.

---

## 🌐 Deploying to GitHub Pages

1. Create a repository on GitHub (e.g., `facebook-bot-by-harshal`).
2. Upload all files (`index.html`, `fb_bot.py`, `requirements.txt`, `README.md`) **directly into the root** of the repository (do NOT put them in a subfolder).
3. Go to **Settings** > **Pages** in your GitHub repository.
4. Under **Branch**, select `main` (or `master`) and save.
5. Your web interface will be live at:
   `https://<your-username>.github.io/<repository-name>/`

---

## 💻 Running the Python Desktop App locally

To run the automated desktop application on your PC:

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch the Bot GUI**:
   ```bash
   python fb_bot.py
   ```

3. **Usage**:
   - Type your text message in the box.
   - Enter target Facebook usernames (space-separated).
   - Enter your Facebook Email/Username and Password.
   - Click **SUBMIT** to initiate automated messaging!

---
*Created by Harshal*
