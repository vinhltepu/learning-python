class Product:
    def __init__(self, id, name, code, unit, import_price, sell_price, stock, imported_date,
                 product_type="base", paint_brand=None, wood_source=None):
        self.id = id
        self.name = name
        self.code = code
        self.unit = unit
        self.import_price = import_price
        self.sell_price = sell_price
        self.stock = stock
        self.imported_date = imported_date
        self.product_type = product_type
        self.paint_brand = paint_brand
        self.wood_source = wood_source

   
    def extra_info(self):
        return ""

class PaintingProduct(Product):
    def __init__(self, *args, paint_brand=None, **kwargs):
        super().__init__(*args, product_type="painting", paint_brand=paint_brand, **kwargs)

    def extra_info(self):
        return f"Hãng sơn: {self.paint_brand or ''}"

class WoodProduct(Product):
    def __init__(self, *args, wood_source=None, **kwargs):
        super().__init__(*args, product_type="wood", wood_source=wood_source, **kwargs)

    def extra_info(self):
        return f"Nguồn gỗ: {self.wood_source or ''}"

def product_from_row(row):

    base_args = (
        row["id"], row["name"], row["code"],
        row["unit"], row["import_price"], row["sell_price"],
        row["stock"], row["imported_date"]
    )

    ptype = row["product_type"]

    if ptype == "painting":
        return PaintingProduct(*base_args, paint_brand=row["paint_brand"])
    if ptype == "wood":
        return WoodProduct(*base_args, wood_source=row["wood_source"])

    return Product(*base_args, product_type=ptype,
                   paint_brand=row["paint_brand"], wood_source=row["wood_source"])
