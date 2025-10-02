import os
import psycopg2
from dotenv import load_dotenv

# Load .env if present
load_dotenv()

DB_NAME = os.getenv("DB_NAME", os.getenv("PGDATABASE", "duke_restaurants"))
DB_USER = os.getenv("DB_USER", os.getenv("PGUSER", "vscode"))
DB_PASSWORD = os.getenv("DB_PASSWORD", os.getenv("PGPASSWORD", "vscode"))
DB_HOST = os.getenv("DB_HOST", os.getenv("PGHOST", "localhost"))
DB_PORT = os.getenv("DB_PORT", os.getenv("PGPORT", "5432"))

def main():
    print(f"Connecting to {DB_NAME} at {DB_HOST}:{DB_PORT} as {DB_USER} ...\n")
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cur = conn.cursor()

    # Query 1: Restaurants within 2.0 miles, ordered by distance
    print("=" * 60)
    print("QUERY 1: Restaurants within 2.0 miles (ordered by distance)")
    print("=" * 60)
    cur.execute("""
        SELECT name, distance_miles
        FROM restaurants
        WHERE distance_miles <= 2.0
        ORDER BY distance_miles ASC;
    """)
    for row in cur.fetchall():
        print(f"  {row[0]:<25} - {row[1]} miles")

    # Query 2: Top 3 restaurants by rating
    print("\n" + "=" * 60)
    print("QUERY 2: Top 3 restaurants by rating")
    print("=" * 60)
    cur.execute("""
        SELECT name, rating
        FROM restaurants
        ORDER BY rating DESC
        LIMIT 3;
    """)
    for idx, row in enumerate(cur.fetchall(), 1):
        print(f"  {idx}. {row[0]:<25} - Rating: {row[1]}")

    # Query 3: Cost with 7.5% tax
    print("\n" + "=" * 60)
    print("QUERY 3: Average cost with 7.5% tax")
    print("=" * 60)
    cur.execute("""
        SELECT name, avg_cost, 
               ROUND(avg_cost * 1.075, 2) AS cost_with_tax
        FROM restaurants
        ORDER BY avg_cost ASC;
    """)
    for row in cur.fetchall():
        print(f"  {row[0]:<25} - ${row[1]:.2f} → ${row[2]:.2f} (with tax)")

    # Query 4: Count restaurants per cuisine
    print("\n" + "=" * 60)
    print("QUERY 4: Restaurant count per cuisine")
    print("=" * 60)
    cur.execute("""
        SELECT cuisine, COUNT(*) AS restaurant_count
        FROM restaurants
        GROUP BY cuisine
        ORDER BY restaurant_count DESC;
    """)
    for row in cur.fetchall():
        print(f"  {row[0]:<25} - {row[1]} restaurant(s)")

    # Close connection
    cur.close()
    conn.close()
    print("\n" + "=" * 60)
    print("All queries completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()