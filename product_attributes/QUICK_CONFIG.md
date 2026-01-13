# ⚡ Cấu hình Template Code nhanh

## 📍 Vị trí cấu hình

### Cách 1: Trong Product Template Form

1. **Truy cập:** http://localhost:8069
2. Vào **Inventory > Products**
3. Mở **"Bulong A193M B7"**
4. Tìm field **"Mã Template (Internal Reference)"** hoặc **"Internal Reference"**
5. **Nhập:** `HB A193M B7`
6. Click **Save**

### Cách 2: Trong Product List View

1. Vào **Inventory > Products**
2. Tìm **"Bulong A193M B7"** trong danh sách
3. Click vào cột **"Internal Reference"** (nếu có)
4. **Nhập:** `HB A193M B7`
5. Click **Save**

## 🎯 Sau khi cấu hình

Sau khi set **Internal Reference = "HB A193M B7"**:
- ✅ Tất cả 99 variants sẽ tự động có SKU: `HB A193M B7 M12 100`, `HB A193M B7 M12 150`, ...
- ✅ Không cần làm gì thêm
- ✅ SKU tự động cập nhật

## 📋 Tương tự cho B8

1. Mở **"Bulong A193M B8"**
2. Set **Internal Reference = "HB A193M B8"**
3. Tất cả variants sẽ có SKU: `HB A193M B8 M12 100`, ...

## 🔍 Kiểm tra

1. Mở sản phẩm **Bulong A193M B7**
2. Scroll xuống phần **Variants**
3. Click vào một variant
4. Xem **Internal Reference** của variant: `HB A193M B7 M12 100` ✅

---

**Cấu hình Internal Reference và SKU sẽ tự động cập nhật! 🎉**
