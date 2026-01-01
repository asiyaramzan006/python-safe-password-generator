# Password Generator (Tkinter)

A simple GUI password generator built with Python's `tkinter`. It creates random passwords using letters, digits, and punctuation.

## Features

- Generate passwords of user-specified length
- Input validation for non-numeric and non-positive values
- Uses only Python standard library (`random`, `string`, `tkinter`)

## Requirements

- Python 3.6+ (Windows)
- `tkinter` (usually included with standard Python on Windows)

## Usage

1. Open a terminal in the folder containing `password.py`.

```powershell
python password.py
```

or

```powershell
py password.py
```

2. Enter the desired password length and click **Generate Password**.
3. The generated password will appear in the result field.

## Notes

- If you see "Enter a valid number" or "Enter a positive number", adjust the input accordingly.
- You can modify the character set in `password.py` by changing the `characters` variable.

## License

Feel free to use or adapt this script for personal projects. If you need a specific license, add one to the repository.
