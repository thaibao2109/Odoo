# ⚡ Cập nhật module để kích hoạt tính năng tự động tạo SKU

## 🚀 Cách nhanh nhất

### Bước 1: Cập nhật module

```bash
cd /Users/baonguyen/Desktop/app/Odoo
python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c odoo.conf -u product_attributes -d odoo
```

### Bước 2: Restart Odoo (nếu cần)

```bash
# Dừng Odoo
pkill -f "odoo-bin"

# Khởi động lại
cd /Users/baonguyen/Desktop/app/Odoo
python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c odoo.conf
```

### Bước 3: Kiểm tra

1. Truy cập: **http://localhost:8069**
2. Vào **Inventory > Products**
3. Mở **Bulong A193M B7**
4. Scroll xuống phần **Variants**
5. Click vào một variant
6. Bạn sẽ thấy field **"Mã SKU (Tự động)"** với SKU đã được tạo!

## 📋 Ví dụ SKU

Sau khi cập nhật, các variants sẽ có SKU:

- `HB A193M B7 M12 100`
- `HB A193M B7 M12 150`
- `HB A193M B7 M14 100`
- `HB A193M B8 M12 100`
- ...

## ✨ Tính năng

- ✅ SKU tự động được tạo cho mỗi variant
- ✅ SKU = Template Code + Attribute Values
- ✅ Tự động cập nhật khi thay đổi attributes
- ✅ Tự động set vào Internal Reference

---

**Cập nhật module và kiểm tra ngay! 🎉**
