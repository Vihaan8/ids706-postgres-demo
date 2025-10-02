# IDS706 PostgreSQL Demo

A PostgreSQL database project featuring Durham, NC restaurants.

## 🗂️ Project Structure

```
ids706-postgres-demo/
├── .devcontainer/
│   ├── devcontainer.json
│   ├── docker-compose.yml
│   └── .env
├── scripts/
│   ├── query.py              
│   └── vihaan_queries.py     # Practice SQL queries
├── init.sql                 
├── requirements.txt
└── README.md
```

## 🛠️ Technologies Used

- **PostgreSQL 16** - Database
- **Python 3.11** - Programming language
- **psycopg2** - PostgreSQL adapter
- **Docker** - Containerization
- **VS Code Dev Containers** - Development environment

## 🚀 Setup Instructions

### 1. Prerequisites
- Docker Desktop installed and running
- VS Code with Dev Containers extension

### 2. Open in Dev Container
1. Clone this repository
2. Open in VS Code
3. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows)
4. Select **"Dev Containers: Reopen in Container"**
5. Wait for container to build and dependencies to install

### 3. Connect PostgreSQL Explorer (Optional)
- Install PostgreSQL extension in container
- Add connection with these settings:
  - Host: `db`
  - User: `vscode`
  - Password: `vscode`
  - Port: `5432`
  - Database: `duke_restaurants`

## 📊 Database Schema

**Table: `restaurants`**

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| name | TEXT | Restaurant name |
| address | TEXT | Street address |
| distance_miles | NUMERIC | Distance from Duke |
| rating | NUMERIC | Rating (out of 5) |
| cuisine | TEXT | Cuisine type |
| avg_cost | NUMERIC | Average cost per meal |
| personal_rank | INT | Personal ranking |

**Initial Data:** 6 restaurants in Durham, NC area

## 💻 Running the Scripts

### CRUD Operations Demo
```bash
python scripts/query.py
```

**Operations performed:**
- SELECT: Display top-rated restaurants
- INSERT: Add new restaurant (Queeny's)
- UPDATE: Increase NuvoTaco's rating by 0.1
- DELETE: Remove lowest-rated restaurant

### Practice Queries
```bash
python scripts/vihaan_queries.py
```

## 📈 Query Results

### Query 1: Restaurants within 2.0 miles (ordered by distance)
```
  NuvoTaco                  - 1.2 miles
  Queeny's                  - 1.5 miles
  Pizzeria Toro             - 1.8 miles
  Guglhupf Bakery           - 1.9 miles
```

### Query 2: Top 3 restaurants by rating
```
  1. NuvoTaco                  - Rating: 4.9
  2. M Sushi                   - Rating: 4.7
  3. Guglhupf Bakery           - Rating: 4.6
```

### Query 3: Average cost with 7.5% tax
```
  NuvoTaco                  - $12.50 → $13.44 (with tax)
  Bullock's BBQ             - $15.00 → $16.13 (with tax)
  Pizzeria Toro             - $18.00 → $19.35 (with tax)
  Guglhupf Bakery           - $20.00 → $21.50 (with tax)
  Queeny's                  - $22.00 → $23.65 (with tax)
  M Sushi                   - $35.00 → $37.63 (with tax)
```

### Query 4: Restaurant count per cuisine
```
  German Café               - 1 restaurant(s)
  American                  - 1 restaurant(s)
  Japanese                  - 1 restaurant(s)
  Mexican                   - 1 restaurant(s)
  Southern/BBQ              - 1 restaurant(s)
  Italian                   - 1 restaurant(s)
```

## 🔍 SQL Queries Explained

### Query 1: Proximity Search
```sql
SELECT name, distance_miles
FROM restaurants
WHERE distance_miles <= 2.0
ORDER BY distance_miles ASC;
```
Finds restaurants within walking distance (2 miles) from Duke campus.

### Query 2: Top Rated
```sql
SELECT name, rating
FROM restaurants
ORDER BY rating DESC
LIMIT 3;
```
Identifies the highest-rated restaurants for quality dining.

### Query 3: Tax Calculation
```sql
SELECT name, avg_cost, 
       ROUND(avg_cost * 1.075, 2) AS cost_with_tax
FROM restaurants
ORDER BY avg_cost ASC;
```
Calculates total meal cost including 7.5% sales tax.

### Query 4: Cuisine Distribution
```sql
SELECT cuisine, COUNT(*) AS restaurant_count
FROM restaurants
GROUP BY cuisine
ORDER BY restaurant_count DESC;
```
Shows variety of cuisine options available.

---

**Course:** IDS706 - Data Engineering  
**Institution:** Duke University  
**Date:** October 