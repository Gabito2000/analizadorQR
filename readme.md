HOW TO RUN THE SERVER
uvicorn main:app --host 0.0.0.0 --port 10000

HOW TO RUN THE SERVEER 
python main.py

CREATE THE EXECUTABLE
python -m PyInstaller --onefile program.py

HOW TO BUILD
pip install -r requirements.txt

HOW TO COMPILE
python -m pyinstaller --noconfirm --onedir --console --collect-all flasgger "./main.py"
