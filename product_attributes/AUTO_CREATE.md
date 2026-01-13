# 🚀 Tự động tạo sản phẩm - Hướng dẫn nhanh

## ⚡ Cách sử dụng

### Bước 1: Cập nhật module

```bash
cd /Users/baonguyen/Desktop/app/Odoo
python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c odoo.conf -u product_attributes -d your_database_name
```

### Bước 2: Mở wizard tự động tạo

1. **Truy cập:** http://localhost:8069
2. **Đăng nhập**
3. Vào **Inventory > Products**
4. Tìm menu **"Tự động tạo sản phẩm"** (ở trên cùng hoặc trong menu Actions)
5. **Click vào menu đó**

### Bước 3: Chạy wizard

1. Một popup sẽ hiện ra với thông tin về những gì sẽ được tạo
2. **Click nút "Tạo sản phẩm"**
3. Đợi vài giây...
4. ✅ **Hoàn thành!** Bạn sẽ thấy danh sách 2 sản phẩm đã tạo

## 📦 Kết quả

Sau khi chạy wizard, bạn sẽ có:

- ✅ **2 Product Templates:**
  - Bulong A193M B7
  - Bulong A193M B8

- ✅ **198 Product Variants:**
  - 99 variants cho B7 (11 đường kính × 9 chiều dài)
  - 99 variants cho B8 (11 đường kính × 9 chiều dài)

- ✅ **Attributes:**
  - Đường kính: M12, M14, M16, M18, M20, M22, M24, M27, M30, M32, M36
  - Chiều dài: 100, 150, 200, 250, 300, 350, 400, 450, 500

## 🎯 Xem kết quả

1. Vào **Inventory > Products**
2. Tìm "Bulong A193M B7" hoặc "Bulong A193M B8"
3. **Mở sản phẩm**
4. Click tab **"Thuộc tính & biến thể"**
5. Bạn sẽ thấy giao diện giống như trong ảnh! 🎉

## ⚠️ Lưu ý

- Wizard sẽ **xóa tất cả sản phẩm** có tên chứa "Bulong A193"
- Nên **backup database** trước khi chạy
- Nếu chạy lại, sẽ tạo lại từ đầu

## 🔄 Nếu không thấy menu

1. **Cập nhật module:**
   ```bash
   python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c odoo.conf -u product_attributes -d your_database_name
   ```

2. **Refresh trình duyệt:** Ctrl+F5 hoặc Cmd+Shift+R

3. **Kiểm tra quyền:** Đảm bảo user có quyền tạo sản phẩm

---

**Chạy wizard và bạn sẽ có sản phẩm với variants tự động! 🎉**
