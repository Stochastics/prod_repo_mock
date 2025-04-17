# 🐍 Python Virtual Environment Setup Guide

This guide walks you through creating a virtual environment for a Python project using `venv`, installing dependencies from `requirements.txt`, and using a `setup.sh` script for automation.

---

## 📘 What Is a Virtual Environment?

A virtual environment is an isolated Python environment where you can install packages separately from the system-wide Python installation. This helps prevent version conflicts and keeps dependencies organized per project.

---

## 📁 Project Structure Example

```
my_project/
├── setup.sh
├── requirements.txt
└── main.py
```

---

## ⚙️ Step-by-Step Setup

### 1. Create a Virtual Environment

```bash
python3 -m venv venv
```

This creates a `venv/` directory containing the isolated Python environment.

### 2. Activate the Environment

- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

- **Windows:**
  ```cmd
  venv\Scripts\activate
  ```

You’ll see the environment name in your terminal prompt.

### 3. Create `requirements.txt`

```txt
pandas
numpy
requests
```

(Add any dependencies your project needs.)

### 4. Install Requirements

```bash
pip install -r requirements.txt
```

### 5. (Optional) Create `setup.sh` Script

This makes setup easier in one command:

```bash
#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then make it executable:

```bash
chmod +x setup.sh
```

Run it:

```bash
./setup.sh
```

---

## ✅ Running Your Code

Once the environment is active:

```bash
python main.py
```

---

## 🧼 Deactivate the Environment

```bash
deactivate
```

---

## 📦 Freezing Dependencies (for sharing)

```bash
pip freeze > requirements.txt
```

---

## 💡 Tips

- Use `.gitignore` to exclude `venv/` from Git:

```gitignore
venv/
```

- Re-run `source venv/bin/activate` each time you work in the project.

---

Happy coding! 🧪