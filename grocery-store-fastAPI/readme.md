FAST-API-GROCERY/
├── main.py                         → Khởi tạo app, đăng ký router, tạo DB
├── requirements.txt
└── app/
    ├── core/config.py              → Cấu hình tên app, database URI
    ├── db/
    │   ├── base.py                 → Base + đăng ký models
    │   └── session.py              → Engine + SessionLocal
    ├── models/
    │   ├── product.py              → Product → PaintingProduct, WoodProduct (STI)
    │   ├── customer.py             → Customer → RegularCustomer, VIPCustomer (STI)
    │   └── invoice.py              → Invoice + InvoiceDetail
    ├── schemas/
    │   ├── product.py              → Validate input/output sản phẩm
    │   ├── customer.py             → Validate input/output khách hàng
    │   └── invoice.py              → Validate input/output hóa đơn
    └── api/
        ├── deps.py                 → get_db()
        └── endpoints/
            ├── products.py         → CRUD + filter sản phẩm
            ├── customers.py        → CRUD + tìm kiếm khách hàng
            ├── invoices.py         → Tạo hóa đơn, trừ kho, tích điểm
            └── stats.py            → Thống kê tồn kho, doanh thu, top KH


cd "C:\Users\hanki\Desktop\hoc python\learning-python\grocery-store-fastAPI"
uvicorn main:app --reload