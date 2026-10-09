# Student Project

Student Information System: config (.env), JSON data, validation, grade calculation, report, logging, pytest.

## Setup
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    cp .env.example .env             # Windows: copy .env.example .env

## Run
    # Linux/macOS
    PYTHONPATH=src python -m student_app.main
    # Windows PowerShell
    $env:PYTHONPATH="src"; python -m student_app.main

## Test
    pytest
