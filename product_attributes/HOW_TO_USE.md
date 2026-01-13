# 📖 Hướng dẫn sử dụng: Tìm mục sản phẩm và thiết lập Attributes

## 🔍 Tìm mục sản phẩm

### Cách 1: Qua menu Inventory (Khuyến nghị)

1. Truy cập: **http://localhost:8069**
2. Đăng nhập
3. Vào menu **Inventory** (Tồn kho)
4. Click **Products** (Sản phẩm)
5. Tạo sản phẩm mới hoặc mở sản phẩm có sẵn

### Cách 2: Qua menu Sales

1. Vào menu **Sales** (Bán hàng)
2. Click **Configuration > Product Attributes & Values** (nếu có)
3. Hoặc vào **Products** trực tiếp

### Cách 3: Qua menu Thuộc tính sản phẩm (Module custom)

1. Vào menu **Sales**
2. Tìm menu **"Thuộc tính sản phẩm"**
3. Click **"Sản phẩm"**

## 🎯 Thiết lập Attributes & Variants (như trong ảnh)

### Bước 1: Tạo hoặc mở sản phẩm

1. Vào **Inventory > Products**
2. Click **Create** (Tạo) để tạo sản phẩm mới
   - Hoặc mở sản phẩm có sẵn (ví dụ: "Bulong A193M B7")

### Bước 2: Thiết lập Attributes tự động

1. Trong form sản phẩm, bạn sẽ thấy:
   - Button **"THIẾT LẬP ATTRIBUTES & VARIANTS"** ở góc trên bên phải
   - Hoặc thông báo hướng dẫn

2. Click button **"THIẾT LẬP ATTRIBUTES & VARIANTS"**

3. Hệ thống sẽ tự động:
   - ✅ Tạo attribute "Đường kính" với giá trị: M12, M14, M16, M18, M20, M22, M24, M27, M30, M32, M36
   - ✅ Tạo attribute "Chiều dài" với giá trị: 100, 150, 200, 250, 300, 350, 400, 450, 500
   - ✅ Gán attributes vào sản phẩm
   - ✅ Tự động tạo 99 variants (11 × 9)

### Bước 3: Xem kết quả

1. Sau khi click button, trang sẽ reload
2. Bạn sẽ thấy tab **"Thuộc tính & biến thể"** xuất hiện
3. Click vào tab này để xem:
   - **Đường kính:** M12, M14, M16... (dạng pills màu)
   - **Chiều dài:** 100, 150, 200... (dạng pills màu)
   - Có nút **"CẤU HÌNH"** để chỉnh sửa
   - Có thể xem từng variant

## 📋 Nếu không thấy button

### Kiểm tra:

1. **Module đã được cài đặt chưa?**
   - Vào **Apps** menu
   - Tìm "Product Attributes & SKU Generator"
   - Đảm bảo đã **Install** hoặc **Upgrade**

2. **Đã cập nhật module chưa?**
   ```bash
   python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c /Users/baonguyen/Desktop/app/Odoo/odoo.conf -u product_attributes -d your_database
   ```

3. **Refresh trình duyệt:**
   - Nhấn **Ctrl+F5** (Windows/Linux) hoặc **Cmd+Shift+R** (Mac)
   - Hoặc xóa cache trình duyệt

4. **Kiểm tra logs:**
   ```bash
   tail -f /Users/baonguyen/Desktop/app/Odoo/odoo.log
   ```

## 🎨 Giao diện mong đợi

Sau khi thiết lập thành công, bạn sẽ thấy:

### Trong form sản phẩm:
- Tab **"Thuộc tính & biến thể"** (giống như trong ảnh)
- Attributes hiển thị dưới dạng pills/buttons màu sắc
- Có thể click vào từng giá trị để xem variant tương ứng

### Trong danh sách sản phẩm:
- Có thể thấy số lượng variants
- Có thể filter theo attributes

## 🚀 Cách nhanh nhất: Sử dụng Script

Nếu muốn tạo nhanh 2 sản phẩm với đầy đủ variants:

```bash
cd /Users/baonguyen/Desktop/app/Odoo
python3 product_attributes/scripts/create_products_with_variants.py
```

Script sẽ tự động tạo:
- Bulong A193M B7 (99 variants)
- Bulong A193M B8 (99 variants)

Sau đó vào **Inventory > Products** để xem!

## ❓ Câu hỏi thường gặp

### Q: Tôi không thấy button "THIẾT LẬP ATTRIBUTES & VARIANTS"
**A:** 
- Đảm bảo module đã được cài đặt và cập nhật
- Refresh trình duyệt
- Kiểm tra sản phẩm đã có attributes chưa (button sẽ ẩn nếu đã có)

### Q: Tab "Thuộc tính & biến thể" không hiển thị
**A:**
- Đảm bảo đã click button thiết lập
- Kiểm tra sản phẩm đã có ít nhất 1 attribute chưa
- Thử tạo sản phẩm mới và thiết lập lại

### Q: Variants không được tạo
**A:**
- Kiểm tra "Tạo biến thể" = "Luôn luôn" trong attribute settings
- Đảm bảo đã chọn ít nhất 1 giá trị cho mỗi attribute
- Xem logs để biết lỗi cụ thể

---

**Sau khi làm theo hướng dẫn, bạn sẽ thấy giao diện giống hệt như trong ảnh! 🎉**
