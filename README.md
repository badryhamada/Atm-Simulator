# 🏧 ATM Simulator Project

A modular **ATM Simulator system built in Python**, designed to simulate real-world ATM operations using clean architecture, object-oriented programming (OOP), and professional Git/GitHub workflows.

---

## 📌 Project Overview

This project demonstrates how a real ATM system works, including authentication, balance management, and transaction tracking.

It is designed as a **CLI (Command Line Interface) application** and follows **software engineering best practices** such as modular design, separation of concerns, and version control using Git.

---

## 👥 Team Collaboration (6 Members)

The project was developed collaboratively using a **feature-branch workflow**.

Each team member was responsible for a specific module:

| Module | Responsibility |
|--------|--------------|
| `auth.py` | Authentication system (PIN validation + login attempts) |
| `account.py` | Account management using OOP |
| `deposit.py` | Deposit operations |
| `withdraw.py` | Withdrawal operations with validation |
| `transactions.py` | Transaction history tracking with timestamps |
| `utils.py` | Helper and utility functions |
| `main.py` | System integration and user interface |

---

## ⚙️ Features

### 🔐 Authentication System
- Secure PIN validation
- Limited login attempts (anti-brute-force)

### 💰 Account Management
- Check balance
- Object-Oriented account handling

### ➕ Deposit System
- Input validation
- Real-time balance update

### ➖ Withdraw System
- Prevent overdraft
- Validation of invalid inputs

### 📜 Transaction History
- Tracks all operations
- Includes timestamps for each transaction

### 🧩 Modular Design
- Each feature separated into its own module
- Easy to maintain and extend

---

## 🧠 Project Structure
