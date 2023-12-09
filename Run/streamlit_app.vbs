Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd /K D: && cd 1.Programs and Codes\Ty-Project-1\Zology && streamlit run streamlit_app.py", 1, True
