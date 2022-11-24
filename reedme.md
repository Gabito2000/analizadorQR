HOW TO RUN
uvicorn main:app --reload

CREATE THE EXECUTABLE
python -m PyInstaller --onefile program.py

HOW TO build 
pip install -r requirements.txt

HOW TO COMPILE
python -m pyinstaller --noconfirm --onedir --console --collect-all flasgger "./main.py"
