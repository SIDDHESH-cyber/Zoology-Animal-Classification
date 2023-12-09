Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd /K D: && cd Programs and Codes\Project && python app.py && streamlit run streamlit_app.py", 1, True


