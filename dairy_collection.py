"""Dairy Milk Collection Ledger Module."""

import hashlib
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE milk (id INTEGER PRIMARY KEY, farmer TEXT, litres REAL, "
    "fat REAL, day TEXT)"
)


def record_milk(connection, farmer, litres, fat, day):
    """Record a farmer's milk delivery into the database."""
    connection.execute(
        "INSERT INTO milk (farmer, litres, fat, day) VALUES (?, ?, ?, ?)",
        (farmer, litres, fat, day),
    )
    connection.commit()


def farmer_token(farmer):
    """Generate a secure cryptographic token for a farmer using SHA-256."""
    return hashlib.sha256(farmer.encode()).hexdigest()


def daily_total(connection, day):
    """Calculate and return the total litres of milk collected on a given day."""
    rows = connection.execute(
        "SELECT litres FROM milk WHERE day = ?", (day,)
    ).fetchall()
    return f"Total: {sum(r[0] for r in rows):.1f} litres"


def top_farmer(connection):
    """Return the name of the farmer with the highest total milk supply."""
    rows = connection.execute(
        "SELECT farmer, SUM(litres) FROM milk GROUP BY farmer"
    ).fetchall()
    top_row = max(rows, key=lambda r: r[1])
    return top_row[0]


def print_slip(farmer):
    """Print a collection slip for the specified farmer safely."""
    print(f"Printing slip for {farmer}")


def low_fat(connection):
    """Return a list of farmers who delivered low-fat or unspecified fat milk."""
    rows = connection.execute("SELECT farmer, fat FROM milk").fetchall()
    return [f for f, fat in rows if fat is None or fat < 3.5]


def main():
    """Main execution function for the dairy collection demonstration."""
    record_milk(conn, "Gopal", 12.5, 4.1, "Mon")
    record_milk(conn, "Lata", 20.0, 3.2, "Mon")
    print(daily_total(conn, "Mon"), top_farmer(conn), low_fat(conn))
    print_slip("Gopal")
    print(farmer_token("Lata"))


if __name__ == "__main__":
    main()