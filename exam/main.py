from flask import Flask, render_template, request, redirect, url_for
from db import create_tables, connect

app = Flask(__name__)

create_tables()

@app.route("/")
def home():
    return redirect(url_for("products"))

@app.route("/products")
def products():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, name, code, price, stock FROM products ORDER BY id DESC")
    items = cur.fetchall()
    conn.close()
    return render_template("products.html", items=items)

@app.route("/products/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form.get("name", "")
        code = request.form.get("code", "")
        price = float(request.form.get("price", "0") or "0")
        stock = int(request.form.get("stock", "0") or "0")

        conn = connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO products(name, code, price, stock) VALUES (?, ?, ?, ?)",
            (name, code, price, stock)
        )
        conn.commit()
        if cur.rowcount > 0 :
            print ("thêm sản phẩm thành công ")
        else :
            print ("thêm sản phẩm thất bại ")
    
        conn.close()

        return redirect(url_for("products"))

    return render_template("add_product.html")

if __name__ == "__main__":
    app.run(debug=True)
