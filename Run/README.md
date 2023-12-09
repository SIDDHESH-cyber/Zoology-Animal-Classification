# Use This Script To Run The Application (Read Below For Details)

### NOTE : Keep Both The Files As - It - Is  
### Just Click the File to Run.
### It Uses VBScript (Visual Basic Scripting) 

## Break Down of Script :-
* WScript.Shell : It code snippet that uses the Windows Script Host (WScript.Shell) to execute a command in the Command Prompt (cmd)
* objShell :  This line creates an instance of the WScript.Shell object, which allows the script to run commands and manipulate the Windows environment.
* objShell.Run: This method is used to run a command or script. The command being run is enclosed in double quotes.
* cmd : This starts the Command Prompt (cmd) and keeps it open after executing the command.
* /K : It is used to run the specified command and then return to the Command Prompt(In Simple words it tells CMD To stay Open after Execution).
* D:: This changes the current drive to the D: drive(Cur).
* Change Folder Location : Replace (D:/) with (Your/folder/path) or replace the path according to your Need!
* &&: This is the logical AND operator in the Command Prompt. It allows you to chain multiple commands, and the subsequent command is executed only if the previous one succeeds
* python app.py : This runs the Python script named "app.py".
* streamlit run streamlit_app.py: This runs the Streamlit App(Python) named "streamlit_app.py.
* 1 : It specifies how the window should be displayed. In this case, it's set to 1, which means "Normal window."
* True : It specifies whether the script should wait for the command to complete before continuing. If set to True, the script will wait for the Command Prompt to close before proceeding.

* 1, True: These parameters are passed to the Run method.
