@echo off
cd /d "C:\Dimensao_Cosmica_Quantica"
call ciborna_env\Scripts\activate.bat
start http://localhost:8501
ciborna_env\Scripts\python.exe -m streamlit run cosmos.py
pause
