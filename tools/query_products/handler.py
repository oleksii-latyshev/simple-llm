import os
import psycopg2


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://agent:agent@localhost:5432/agent_db")


def _get_connection():
    return psycopg2.connect(DATABASE_URL)


def execute(product_name: str = None, include_feedback: bool = True) -> dict:
    try:
        conn = _get_connection()
        cur = conn.cursor()

        if product_name:
            cur.execute(
                "SELECT id, name, category, price, description FROM products WHERE name ILIKE %s",
                (f"%{product_name}%",),
            )
        else:
            cur.execute("SELECT id, name, category, price, description FROM products")

        products = cur.fetchall()
        if not products:
            cur.close()
            conn.close()
            return {"status": "success", "products": [], "message": "No products found."}

        result = []
        for pid, name, category, price, description in products:
            product = {
                "id": pid,
                "name": name,
                "category": category,
                "price": float(price),
                "description": description,
            }

            if include_feedback:
                cur.execute(
                    "SELECT author, rating, comment FROM feedback WHERE product_id = %s ORDER BY created_at",
                    (pid,),
                )
                reviews = cur.fetchall()
                product["feedback"] = [
                    {"author": author, "rating": rating, "comment": comment}
                    for author, rating, comment in reviews
                ]
                if reviews:
                    ratings = [r[1] for r in reviews]
                    product["average_rating"] = round(sum(ratings) / len(ratings), 1)

            result.append(product)

        cur.close()
        conn.close()

        return {"status": "success", "products": result}

    except Exception as e:
        return {"status": "error", "message": str(e)}
