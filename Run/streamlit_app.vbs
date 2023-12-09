Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd /K cd.. && streamlit run streamlit_app.py", 1, True
