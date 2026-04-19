import sqlite3
import argparse
from datetime import datetime
import sys

DB_NAME = "journal.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_entry(content, date=None):
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO entries (date, content) VALUES (?, ?)", (date, content))
    conn.commit()
    conn.close()
    print(f"Added entry for {date}")

def list_entries():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, content FROM entries ORDER BY date DESC, created_at DESC")
    entries = cursor.fetchall()
    conn.close()
    
    if not entries:
        print("No entries found.")
        return

    print(f"{'ID':<5} | {'Date':<12} | {'Content'}")
    print("-" * 50)
    for row in entries:
        content_preview = row[2] if len(row[2]) < 50 else row[2][:47] + "..."
        print(f"{row[0]:<5} | {row[1]:<12} | {content_preview}")

def search_entries(query):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, content FROM entries WHERE content LIKE ? ORDER BY date DESC", (f"%{query}%",))
    entries = cursor.fetchall()
    conn.close()
    
    if not entries:
        print(f"No entries found matching '{query}'.")
        return

    for row in entries:
        print(f"[{row[1]}] {row[2]}")
        print("-" * 20)

def main():
    init_db()
    parser = argparse.ArgumentParser(description="SQLite Daily Journal System")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new journal entry")
    add_parser.add_argument("content", help="The content of the journal entry")
    add_parser.add_argument("--date", help="Optional: date in YYYY-MM-DD format (defaults to today)")

    # List command
    subparsers.add_parser("list", help="List all journal entries")

    # Search command
    search_parser = subparsers.add_parser("search", help="Search journal entries")
    search_parser.add_argument("query", help="Text to search for")

    args = parser.parse_args()

    if args.command == "add":
        add_entry(args.content, args.date)
    elif args.command == "list":
        list_entries()
    elif args.command == "search":
        search_entries(args.query)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
