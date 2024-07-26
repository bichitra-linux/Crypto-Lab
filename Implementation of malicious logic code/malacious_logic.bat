@echo off
set "fileToDelete=path_to_file_to_delete"
if exist "%fileToDelete%" (
 del "%fileToDelete%"
 echo File deleted successfully.
) else (
 echo The file does not exist or the path is incorrect.
)
pause