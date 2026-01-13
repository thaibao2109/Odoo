# 🚀 Hướng dẫn nhanh: Tạo sản phẩm với Variants (như trong ảnh)

## ⚡ Cách nhanh nhất

### Chạy script tự động:

```bash
cd /Users/baonguyen/Desktop/app/Odoo

# 1. Sửa database name trong script (nếu cần)
nano product_attributes/scripts/create_products_with_variants.py
# Sửa: ODOO_DB = 'your_database_name'

# 2. Chạy script
python3 product_attributes/scripts/create_products_with_variants.py
```

Script sẽ tự động:
- ✅ Tạo attributes: "Đường kính" và "Chiều dài"
- ✅ Tạo attribute values: M12-M36 và 100-500
- ✅ Xóa sản phẩm cũ
- ✅ Tạo 2 sản phẩm: Bulong A193M B7 và B8
- ✅ Tự động tạo 198 variants (99 × 2)

## 📋 Kết quả

Sau khi chạy script, bạn sẽ có:

### 2 Product Templates:
- **Bulong A193M B7** - với tab "Thuộc tính & biến thể"
- **Bulong A193M B8** - với tab "Thuộc tính & biến thể"

### 198 Product Variants:
- Mỗi variant có SKU: `HB A193M B7 M12 100`, `HB A193M B7 M12 150`, etc.

### Giao diện giống ảnh:
- Tab **"Thuộc tính & biến thể"** hiển thị:
  - **Đường kính:** M12, M14, M16, M18, M20, M22, M24, M27, M30, M32, M36 (dạng pills màu)
  - **Chiều dài:** 100, 150, 200, 250, 300, 350, 400, 450, 500 (dạng pills màu)
- Có nút **"CẤU HÌNH"** để chỉnh sửa attributes
- Có thể xem và chỉnh sửa từng variant

## 🔍 Kiểm tra

1. Truy cập: **http://localhost:8069**
2. Vào **Inventory > Products**
3. Tìm "Bulong A193M B7"
4. Mở sản phẩm
5. Click tab **"Thuộc tính & biến thể"**
6. Bạn sẽ thấy giao diện giống như trong ảnh! 🎉

## ⚠️ Lưu ý

- Script sẽ **xóa tất cả sản phẩm** có tên chứa "Bulong A193"
- Nên **backup database** trước khi chạy
- Đảm bảo **Odoo đang chạy** trước khi chạy script

## 🆘 Nếu gặp lỗi

### Lỗi kết nối:
- Kiểm tra Odoo đang chạy: `curl http://localhost:8069`
- Kiểm tra database name đúng chưa

### Lỗi xác thực:
- Kiểm tra username và password trong script
- Đảm bảo user có quyền tạo sản phẩm

### Variants không được tạo:
- Kiểm tra "Tạo biến thể" = "Luôn luôn" trong attribute settings
- Xem logs: `tail -f /Users/baonguyen/Desktop/app/Odoo/odoo.log`

---

**Chạy script và bạn sẽ có giao diện giống hệt như trong ảnh! 🎉**
