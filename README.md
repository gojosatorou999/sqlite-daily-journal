# Chronos: SQLite Daily Journal System

A simple, lightweight CLI tool to store and manage daily journal entries using an SQLite database.

## Features 

- **Daily Logging**: Automatically timestamps entries with today's date.
- **CLI Interface**: Easy to use commands for adding, listing, and searching entries.
- **SQLite Backend**: Efficient storage in a single portable database file.

## Schema Overview :

The database uses a single table called `entries`.

| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | INTEGER | Primary key, automatically increments. |
| `date` | TEXT | The date of the entry in `YYYY-MM-DD` format. |
| `content` | TEXT | The actual journal entry text. |
| `created_at` | TIMESTAMP | The exact time the entry was recorded (defaults to `CURRENT_TIMESTAMP`). |

## Usage 

### 1. Add an entry
```bash
python journal.py add "Today was a productive day. I finally finished the SQLite project."
```

### 2. List all entries
```bash
python journal.py list
```

### 3. Search entries
```bash
python journal.py search "SQLite"
```

## Setup

No external dependencies are required as it uses the built-in `sqlite3` and `argparse` libraries.

1. Clone the repository.
2. Run `python journal.py` to get started.
