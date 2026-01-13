# ⚡ Tự động tạo sản phẩm - Cách nhanh nhất

## 🚀 Cách 1: Qua Menu Action (Nhanh nhất)

### Bước 1: Cập nhật module

```bash
cd /Users/baonguyen/Desktop/app/Odoo
python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c odoo.conf -u product_attributes -d your_database_name
```

### Bước 2: Chạy action

1. **Truy cập:** http://localhost:8069
2. **Đăng nhập**
3. Vào **Inventory > Products**
4. Ở góc trên bên phải, tìm menu **"Action"** (hoặc biểu tượng ⚙️)
5. Click **"Action"** → Tìm **"Tự động tạo sản phẩm Bulong A193M B7/B8"**
6. **Click vào action đó**
7. ✅ **Xong!** Sản phẩm sẽ được tạo tự động

## 🎯 Cách 2: Qua Wizard (Có popup xác nhận)

1. Vào **Inventory > Products**
2. Tìm menu **"Tự động tạo sản phẩm"** (có thể ở menu Actions hoặc trên cùng)
3. Click vào menu
4. Popup hiện ra → Click **"Tạo sản phẩm"**
5. ✅ **Hoàn thành!**

## 📦 Kết quả

Sau khi chạy, bạn sẽ có:

- ✅ **2 sản phẩm:**
  - Bulong A193M B7
  - Bulong A193M B8

- ✅ **198 variants** (99 × 2)

- ✅ **Tab "Thuộc tính & biến thể"** với:
  - Đường kính: M12-M36 (dạng pills)
  - Chiều dài: 100-500 (dạng pills)

## 🔍 Xem kết quả

1. Vào **Inventory > Products**
2. Tìm "Bulong A193M B7"
3. **Mở sản phẩm**
4. Click tab **"Thuộc tính & biến thể"**
5. 🎉 **Giống hệt như trong ảnh!**

## ⚠️ Lưu ý

- Sẽ **xóa sản phẩm cũ** có tên chứa "Bulong A193"
- Nên **backup** trước khi chạy

---

**Cập nhật module và chạy action - Xong trong 30 giây! ⚡**
