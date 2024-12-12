# TaskTerminator

TaskTerminator is a lightweight Python-based graphical utility for managing and terminating processes on Windows systems. It provides an intuitive interface to view, refresh, and kill currently running processes by their PID (Process Identifier) or name.

## Features

- **Process List**: Displays a comprehensive list of currently running processes, including their PID and process name.
- **Terminate Processes**: Allows users to select and terminate unwanted processes safely.
- **Refresh Functionality**: Updates the process list to reflect the current state of the system.

## System Requirements

- Python 3.7 or higher
- Compatible with Windows operating systems
- Required Python libraries:
  - `psutil` for process management
  - `tkinter` for graphical user interface

## Application Overview

TaskTerminator offers a simple interface with two main sections:

1. **Process List**: A table displaying running processes with two columns:
   - **PID**: The unique identifier for each process.
   - **Name**: The name of the executable file.

2. **Control Buttons**:
   - **Refresh**: Updates the displayed list of processes.
   - **Kill Process**: Terminates the selected process after confirmation.

## Usage Notes

- Exercise caution when terminating processes. Killing critical system processes may cause instability or system crashes.
- Refresh the process list regularly to ensure you are working with up-to-date information.

## License

This project is released under the MIT License, allowing you to use, modify, and distribute the software freely.

---

Created with simplicity and functionality in mind. Enjoy managing your tasks efficiently with TaskTerminator!
