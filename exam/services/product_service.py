from db import connect
from models.product import Product, PaintingProduct, WoodProduct

class ProductService:
    def get_all(self):
        """
        Lấy tất cả sản phẩm từ DB và chuyển thành list các object Product (hoặc subclass).
        Sử dụng sqlite3.Row để truy cập theo tên cột cho an toàn.
        """
        conn = connect()
        # Để dễ truy cập theo tên cột, dùng row_factory = sqlite3.Row
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("""
            SELECT id, name, code, unit, import_price, sell_price, 
                   stock, imported_date, product_type, paint_brand, wood_source 
            FROM products 
            ORDER BY id DESC
        """)
        rows = cur.fetchall()
        conn.close()

        products = []
        for row in rows:
            # row là sqlite3.Row, truy cập bằng tên cột
            base_kwargs = {
                'id': row['id'],
                'name': row['name'],
                'code': row['code'],
                'unit': row['unit'],
                'import_price': row['import_price'],
                'sell_price': row['sell_price'],
                'stock': row['stock'],
                'imported_date': row['imported_date'],
                'product_type': row['product_type']
            }

            ptype = row['product_type']

            if ptype == 'painting':
                p = PaintingProduct(
                    id=base_kwargs['id'],
                    name=base_kwargs['name'],
                    code=base_kwargs['code'],
                    unit=base_kwargs['unit'],
                    import_price=base_kwargs['import_price'],
                    sell_price=base_kwargs['sell_price'],
                    stock=base_kwargs['stock'],
                    imported_date=base_kwargs['imported_date'],
                    paint_brand=row['paint_brand']
                )
            elif ptype == 'wood':
                p = WoodProduct(
                    id=base_kwargs['id'],
                    name=base_kwargs['name'],
                    code=base_kwargs['code'],
                    unit=base_kwargs['unit'],
                    import_price=base_kwargs['import_price'],
                    sell_price=base_kwargs['sell_price'],
                    stock=base_kwargs['stock'],
                    imported_date=base_kwargs['imported_date'],
                    wood_source=row['wood_source']
                )
            else:
                # Loại base hoặc loại khác (nếu có thêm sau này)
                p = Product(**base_kwargs)

            products.append(p)

        return products

    def add(self, product: Product):
        """
        Thêm một sản phẩm vào DB.
        Trả về product với id được cập nhật.
        """
        conn = connect()
        cur = conn.cursor()

        if isInstance(product, PaintingProduct):
            cur.execute("""
                INSERT INTO products 
                (name, code, unit, import_price, sell_price, stock, imported_date, product_type, paint_brand)
                VALUES (?, ?, ?, ?, ?, ?, ?, 'painting', ?)
            """, (
                product.name,
                product.code,
                product.unit,
                product.import_price,
                product.sell_price,
                product.stock,
                product.imported_date,
                product.paint_brand
            ))
        elif isInstance(product, WoodProduct):
            cur.execute("""
                INSERT INTO products 
                (name, code, unit, import_price, sell_price, stock, imported_date, product_type, wood_source)
                VALUES (?, ?, ?, ?, ?, ?, ?, 'wood', ?)
            """, (
                product.name,
                product.code,
                product.unit,
                product.import_price,
                product.sell_price,
                product.stock,
                product.imported_date,
                product.wood_source
            ))
        else:
            # Loại base hoặc loại chung
            cur.execute("""
                INSERT INTO products 
                (name, code, unit, import_price, sell_price, stock, imported_date, product_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                product.name,
                product.code,
                product.unit,
                product.import_price,
                product.sell_price,
                product.stock,
                product.imported_date,
                product.product_type
            ))

        conn.commit()
        product.id = cur.lastrowid  # Cập nhật id mới cho object
        conn.close()
        return product
"""
Cháu viết thêm các class con của Product đã thêm vào ở Product để minh họa cách mở rộng

Viết thêm các phương thức khác như update, delete để cập nhật/xóa sản phẩm

Làm tương tự với các dịch vụ khác như CustomerService, InvoiceService
"""