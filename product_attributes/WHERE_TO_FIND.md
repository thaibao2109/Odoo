# 🔍 Tìm mục sản phẩm và thiết lập Attributes

## 📍 Vị trí menu sản phẩm

### Cách 1: Qua Inventory (Tồn kho) - **Khuyến nghị**

1. **Truy cập:** http://localhost:8069
2. **Đăng nhập** vào Odoo
3. **Click menu "Inventory"** (Tồn kho) ở thanh menu trên cùng
4. **Click "Products"** (Sản phẩm)
5. Bạn sẽ thấy danh sách sản phẩm

### Cách 2: Qua Sales (Bán hàng)

1. **Click menu "Sales"** (Bán hàng)
2. **Click "Products"** hoặc tìm trong menu con
3. Hoặc vào **Configuration > Products**

### Cách 3: Qua menu module (nếu có)

1. **Click menu "Sales"**
2. Tìm menu **"Thuộc tính sản phẩm"** (nếu module đã cài)
3. **Click "Sản phẩm"**

## 🎯 Cách thiết lập Attributes (như trong ảnh)

### Bước 1: Mở sản phẩm

1. Vào **Inventory > Products**
2. **Tạo sản phẩm mới** (Click nút "Create") hoặc **mở sản phẩm có sẵn**

### Bước 2: Tìm button thiết lập

Trong form sản phẩm, bạn sẽ thấy:

#### Option A: Button ở header (góc trên bên phải)
- Tìm button **"THIẾT LẬP ATTRIBUTES"** với icon bánh răng (⚙️)
- Button này chỉ hiển thị khi sản phẩm **chưa có attributes**

#### Option B: Tab "Thuộc tính & biến thể"
- Scroll xuống, tìm tab **"Thuộc tính & biến thể"**
- Click vào tab này
- Click nút **"Thêm một dòng"** để thêm attributes thủ công

### Bước 3: Click button thiết lập

1. **Click button "THIẾT LẬP ATTRIBUTES"**
2. Hệ thống sẽ tự động:
   - ✅ Tạo attribute "Đường kính" với: M12, M14, M16, M18, M20, M22, M24, M27, M30, M32, M36
   - ✅ Tạo attribute "Chiều dài" với: 100, 150, 200, 250, 300, 350, 400, 450, 500
   - ✅ Tự động tạo 99 variants

### Bước 4: Xem kết quả

1. Sau khi click, trang sẽ reload
2. **Click tab "Thuộc tính & biến thể"**
3. Bạn sẽ thấy:
   - **Đường kính:** M12, M14, M16... (dạng pills màu) ✅
   - **Chiều dài:** 100, 150, 200... (dạng pills màu) ✅
   - Có nút **"CẤU HÌNH"** để chỉnh sửa ✅
   - Giống hệt như trong ảnh! 🎉

## 🖼️ Hình ảnh minh họa vị trí

```
┌─────────────────────────────────────────────────┐
│ Inventory > Products                            │
├─────────────────────────────────────────────────┤
│                                                  │
│  [Create] [Import] [Export] ...                 │
│                                                  │
│  ┌──────────────────────────────────────────┐   │
│  │ Product Name: Bulong A193M B7           │   │
│  │ [THIẾT LẬP ATTRIBUTES] ← Button ở đây!  │   │
│  ├──────────────────────────────────────────┤   │
│  │ Thông tin chung | Thuộc tính & biến thể │   │
│  │                  ↑ Tab này sẽ xuất hiện │   │
│  │                  sau khi click button   │   │
│  └──────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
```

## ⚠️ Nếu không thấy button

### Kiểm tra 1: Module đã cài chưa?

1. Vào **Apps** menu
2. Tìm **"Product Attributes & SKU Generator"**
3. Đảm bảo đã **Install** hoặc **Upgrade**

### Kiểm tra 2: Đã cập nhật module chưa?

```bash
cd /Users/baonguyen/Desktop/app/Odoo
python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c odoo.conf -u product_attributes -d your_database_name
```

### Kiểm tra 3: Sản phẩm đã có attributes chưa?

- Button sẽ **ẩn** nếu sản phẩm đã có attributes
- Nếu đã có, vào tab **"Thuộc tính & biến thể"** để xem

### Kiểm tra 4: Refresh trình duyệt

- Nhấn **Ctrl+F5** (Windows/Linux) hoặc **Cmd+Shift+R** (Mac)
- Hoặc xóa cache trình duyệt

## 🚀 Cách nhanh: Dùng Script

Nếu muốn tạo nhanh 2 sản phẩm với đầy đủ variants:

```bash
cd /Users/baonguyen/Desktop/app/Odoo
python3 product_attributes/scripts/create_products_with_variants.py
```

Sau đó vào **Inventory > Products** để xem!

## 📞 Vẫn không thấy?

1. **Kiểm tra logs:**
   ```bash
   tail -f /Users/baonguyen/Desktop/app/Odoo/odoo.log
   ```

2. **Kiểm tra quyền truy cập:**
   - Đảm bảo user có quyền tạo/sửa sản phẩm

3. **Thử tạo sản phẩm mới:**
   - Tạo sản phẩm hoàn toàn mới
   - Button sẽ hiển thị rõ ràng hơn

---

**Làm theo các bước trên, bạn sẽ tìm thấy và thiết lập được attributes như trong ảnh! 🎉**
