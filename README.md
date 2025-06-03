# copilot_test.py

This repository contains a Python script, `copilot_test.py`, that prints the system uptime for Windows, Linux, and macOS systems. The script uses modern Python practices including `subprocess.run()` for executing shell commands and incorporates robust exception handling.

## Features

- Prints system uptime in hours, minutes, and seconds.
- Cross-platform support:
  - Linux (via `/proc/uptime`)
  - macOS (via `sysctl`)
  - Windows (via `net stats srv`)
- Uses `subprocess.run()` instead of deprecated `os.popen()`.
- Functions are modular and include exception handling for robustness.

## Usage

1. Make sure you have Python 3.5 or higher installed.
2. Clone this repository or download `copilot_test.py`.
3. Run the script:

```bash
python copilot_test.py
```

## Output Example

```
System uptime: 5 hours, 23 minutes, 12 seconds
```

## License

This project is licensed under the MIT License.

## Contributing

Pull requests and issues are welcome!
