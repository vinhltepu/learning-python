from flask import Flask, render_template, request, redirect, url_for
from db import create_tables, connect

app = Flask(__name__)


create_tables()#tạo database


@app.route("/")
def home():
    return redirect(url_for("products"))


# hiển thị danh sách 
@app.route("/products")
def products():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, name, code,unit,impore_price,stell_price,imported_date stock FROM products ORDER BY id DESC")# sửa để khớp với db.main
    items = cur.fetchall()
    conn.close()
    return render_template("products.html", items=items)


# mục thêm sản phẩm 
@app.route("/products/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        code = request.form.get("code", "").strip()
        unit = request.form.get("unit", "").strip()
        import_price = float(request.form.get("import_price", "0") or "0")
        sell_price = float(request.form.get("sell_price", "0") or "0")
        stock = int(request.form.get("stock", "0") or "0")
        imported_date = request.form.get("imported_date", "").strip()

        conn = connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO products(name, code, unit, import_price,sell_price,stock,imported_date) VALUES (?, ?, ?, ?,?,?,?)",
            (name, code, price, stock)
        )
        conn.commit()

    # tạo thông báo lỗi thì tạo thất bại 
        if cur.rowcount > 0:
            print(" thêm sản phẩm thành công")
        else:
            print(" thêm sản phẩm thất bại") 

        conn.close()
        return redirect(url_for("products"))

    return render_template("product_form.html", mode="add", product=None)


# chức năng sửa sản phẩm 
@app.route("/products/<int:pid>/edit", methods=["GET", "POST"])
def edit_product(pid):
    conn = connect()
    cur = conn.cursor()

    
    cur.execute("""
       UPDATE products
       SET name=?, code=?, unit=?, import_price=?, sell_price=?, stock=?, imported_date=?
       WHERE id=?
    """, (name, code, unit, import_price, sell_price, stock, imported_date, pid))
    conn.commit()

    if product is None:
        conn.close()
        return "Product not found", 404

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        code = request.form.get("code", "").strip()
        import_price = float(request.form.get("import_price", "0") or "0")
        sell_price = float(request.form.get("sell_price", "0") or "0")
        stock = int(request.form.get("stock", "0") or "0")
        imported_date = request.form.get("imported_date", "").strip()

        cur.execute("""
            UPDATE products
            SET name=?, code=?, unit=?, import_price=?, sell_price=?, stock=?, imported_date=?
            WHERE id=?
        """, (name, code, price, stock, pid))

        conn.commit()
        conn.close()
        return redirect(url_for("products"))

    conn.close()
    return render_template("product_form.html", mode="edit", product=product)

# chức năng xóa sản phẩm 
@app.route("/products/<int:pid>/delete", methods=["POST"])
def delete_product(pid):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id=?", (pid,))
    conn.commit()
    conn.close()
    return redirect(url_for("products"))


if __name__ == "__main__":
    app.run(debug=True)
