# Robocorp-Linear-Framework

This framework is intended for linear (non-transactional) processes that do not require work items.

The demo process included in this framework is Robocorp's [Level 1 automation](https://robocorp.com/docs/courses/beginners-course/python-robot)

### Suggested Directory Structure

```
├── libraries
│   ├── framework
│   └── steps
├── output
├── conda.yaml
├── config.yaml
├── main.py
└── robot.yaml
```

- `libraries`: Python library code files
    - `framework`: Code files that can be used in any process
    - `steps`: Code files you create that are specific to your process
- `output`: Store process artifacts here, including error screenshots and logs
- `conda.yaml`: Configuration file used to set up runtime environment
- `config.yaml`: Configuration file used to store process settings
- `main.py`: High-level process definition for the automation
- `robot.yaml`: Configuration file for the robot

### Features

- Made in pure Python, which some people (including myself) prefer over Robot Framework
- Supports managing process settings using a local config file
- Supports managing attended automation credentials using Windows Credential Manager
