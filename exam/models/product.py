class Product:
    """
    Định nghia class sản phẩm cơ bản với các thuộc tính chung.
    __init__ nhận các tham số cần thiết để khởi tạo một sản phẩm.
    self: tham chiếu đến đối tượng hiện tại của class.
    """
    def __init__(
            self, 
            id, 
            name, 
            code, 
            unit,
            import_price, 
            sell_price, 
            stock, 
            imported_date,
            product_type="base"
        ):
        self.id = id
        self.name = name
        self.code = code
        self.unit = unit
        self.import_price = import_price
        self.sell_price = sell_price
        self.stock = stock
        self.imported_date = imported_date
        self.product_type = product_type

        # Kiểm tra tính hợp lệ của dữ liệu
        if sell_price < import_price:
            raise ValueError("Giá bán phải lớn hơn hoặc bằng giá nhập")
        if stock < 0:
            raise ValueError("Tồn kho không được âm")
        if len(name) < 1 or len(code) < 1:
            raise ValueError("Tên và mã sản phẩm không được để trống")

    # Thêm phương thức extra_info để trả về thông tin bổ sung
    def extra_info(self):
        return ""
    
    # Phương thức để chuyển đổi đối tượng thành dict
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'unit': self.unit,
            'import_price': self.import_price,
            'sell_price': self.sell_price,
            'stock': self.stock,
            'imported_date': self.imported_date,
            'product_type': self.product_type,
            'extra_info': self.extra_info()
        }

class PaintingProduct(Product):
    # Định nghĩa class sản phẩm sơn kế thừa từ Product
    def __init__(
            self, 
            *args, 
            paint_brand=None, 
            **kwargs
        ):
        super().__init__(
            *args, 
            product_type="painting",
            **kwargs
        )

        # Thuộc tính riêng của sản phẩm sơn
        self.paint_brand = paint_brand

    # Phương thức trả về thông tin bổ sung, override từ lớp cha
    def extra_info(self):
        return f"Hãng sơn: {self.paint_brand or ''}"

    # Phương thức để chuyển đổi đối tượng thành dict, override từ lớp cha
    def to_dict(self):
        data = super().to_dict()
        data['paint_brand'] = self.paint_brand
        return data

class WoodProduct(Product):
    # Định nghĩa class sản phẩm gỗ kế thừa từ Product
    def __init__(
            self, 
            *args, 
            wood_source=None, 
            **kwargs):
        super().__init__(
            *args, 
            product_type="wood",
            **kwargs
        )
        # Thuộc tính riêng của sản phẩm gỗ
        self.wood_source = wood_source
    # Phương thức trả về thông tin bổ sung, override từ lớp cha
    def extra_info(self):
        return f"Nguồn gỗ: {self.wood_source or ''}"

    # Phương thức để chuyển đổi đối tượng thành dict, override từ lớp cha
    def to_dict(self):
        data = super().to_dict()
        data['wood_source'] = self.wood_source
        return data

"""
Cháu thêm một vài class con để minh họa cách mở rộng từ class Product nhé

"""

def product_from_row(row):
    # Hàm tạo đối tượng sản phẩm từ dict
    # dùng row.get(...) để tránh lỗi khi key không tồn tại
    base_args = (
        row.get("id"),
        row.get("name"),
        row.get("code"),
        row.get("unit"),
        row.get("import_price"),
        row.get("sell_price"),
        row.get("stock"),
        row.get("imported_date")
    )

    ptype = row.get("product_type")

    if ptype == "painting":
        return PaintingProduct( *base_args, paint_brand=row.get("paint_brand") )
    if ptype == "wood":
        return WoodProduct( *base_args, wood_source=row.get("wood_source") )

    return Product(
        *base_args, 
        product_type=ptype,
        paint_brand=row.get("paint_brand"),
        wood_source=row.get("wood_source")
    )
class PaintingProduct(Product):
    """Sản phẩm sơn: có thêm tên hãng sơn (paint_brand)."""
    def __init__(self, *args, paint_brand=None, **kwargs):
        # ép product_type về "painting"
        kwargs.pop("product_type", None)
        super().__init__(*args, product_type="painting", **kwargs)
        self.paint_brand = paint_brand

    def extra_info(self):
        return f"Hãng sơn: {self.paint_brand or ''}"

    def to_dict(self):
        data = super().to_dict()
        data["paint_brand"] = self.paint_brand
        return data


class WoodProduct(Product):
    """Sản phẩm gỗ: có thêm nguồn nhập hàng (wood_source)."""
    def __init__(self, *args, wood_source=None, **kwargs):
        kwargs.pop("product_type", None)
        super().__init__(*args, product_type="wood", **kwargs)
        self.wood_source = wood_source

    def extra_info(self):
        return f"Nguồn gỗ: {self.wood_source or ''}"

    def to_dict(self):
        data = super().to_dict()
        data["wood_source"] = self.wood_source
        return data


class BulkProduct(Product):
    """Minh hoạ: sản phẩm bán sỉ (không cần cột DB riêng)."""
    def __init__(self, *args, **kwargs):
        kwargs.pop("product_type", None)
        super().__init__(*args, product_type="bulk", **kwargs)

    def extra_info(self):
        return "Loại: Bán sỉ"


class ClearanceProduct(Product):
    """Minh hoạ: sản phẩm xả kho (không cần cột DB riêng)."""
    def __init__(self, *args, **kwargs):
        kwargs.pop("product_type", None)
        super().__init__(*args, product_type="clearance", **kwargs)

    def extra_info(self):
        return "Loại: Xả kho"
