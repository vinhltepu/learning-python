# exam/models/customer.py
from abc import ABC, abstractmethod


class Customer(ABC):
    def __init__(self, id, name, phone, address, total_spent=0, customer_type="regular"):
        self._id = id
        self.name = name
        self.phone = phone
        self.address = address
        self.total_spent = total_spent
        self.customer_type = customer_type

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        value = (value or "").strip()
        if not value:
            raise ValueError("Tên khách hàng không được để trống")
        self._name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        value = (value or "").strip()
        if not value:
            raise ValueError("Số điện thoại không được để trống")
        if (not value.isdigit()) or (len(value) < 9 or len(value) > 12):
            raise ValueError("Số điện thoại không hợp lệ (chỉ số, dài 9-12)")
        self._phone = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        value = (value or "").strip()
        if not value:
            raise ValueError("Địa chỉ không được để trống")
        self._address = value

    @property
    def total_spent(self):
        return self._total_spent

    @total_spent.setter
    def total_spent(self, value):
        try:
            value = float(value)
        except:
            value = 0
        if value < 0:
            raise ValueError("Tổng tiền đã mua không được âm")
        self._total_spent = value

    @abstractmethod
    def discount_rate(self) -> float:
        """trả về % giảm giá (0.05 = 5%)."""
        raise NotImplementedError

    def calc_discount(self, total_amount: float) -> float:
        """Tính số tiền giảm trên tổng hóa đơn."""
        try:
            total_amount = float(total_amount)
        except:
            total_amount = 0
        if total_amount < 0:
            total_amount = 0
        return total_amount * self.discount_rate()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "address": self.address,
            "total_spent": self.total_spent,
            "customer_type": self.customer_type,
            "discount_rate": self.discount_rate(),
        }


class RegularCustomer(Customer):
    """Khách thường: không giảm giá."""
    def __init__(self, id, name, phone, address, total_spent=0):
        super().__init__(id, name, phone, address, total_spent, customer_type="regular")

    def discount_rate(self) -> float:
        return 0.0


class VIPCustomer(Customer):
    def __init__(self, id, name, phone, address, total_spent=0):
        super().__init__(id, name, phone, address, total_spent, customer_type="vip")

    def discount_rate(self) -> float:
        if self.total_spent > 200_000_000:
            return 0.10
        if self.total_spent > 100_000_000:
            return 0.05
        return 0.0


def customer_from_row(row: dict):
    ctype = (row.get("customer_type") or "regular").strip().lower()

    base_kwargs = dict(
        id=row.get("id"),
        name=row.get("name"),
        phone=row.get("phone"),
        address=row.get("address"),
        total_spent=row.get("total_spent", 0),
    )

    if ctype == "vip":
        return VIPCustomer(**base_kwargs)
    return RegularCustomer(**base_kwargs)
