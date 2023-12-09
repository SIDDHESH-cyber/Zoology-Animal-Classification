Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd /K cd.. && python app.py", 1, True


