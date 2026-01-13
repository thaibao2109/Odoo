# Hướng dẫn tạo sản phẩm với Attributes & Variants (như trong ảnh)

## Mục tiêu

Tạo sản phẩm với giao diện **"Thuộc tính & biến thể"** giống như trong ảnh, với:
- Tab "Thuộc tính & biến thể" 
- Attributes: Đường kính, Chiều dài
- Variants tự động được tạo từ các giá trị attributes
- Hiển thị dưới dạng pills/buttons màu sắc

## Cách 1: Sử dụng Script Python (Khuyến nghị)

### Bước 1: Chỉnh sửa cấu hình trong script

Mở file: `product_attributes/scripts/create_products_with_variants.py`

Sửa các thông tin:
```python
ODOO_DB = 'your_database_name'  # Tên database của bạn
ODOO_USERNAME = 'admin'           # Username
ODOO_PASSWORD = 'admin'          # Password
```

### Bước 2: Chạy script

```bash
cd /Users/baonguyen/Desktop/app/Odoo
python3 product_attributes/scripts/create_products_with_variants.py
```

Script sẽ:
1. ✅ Tạo attributes: "Đường kính" và "Chiều dài"
2. ✅ Tạo attribute values: M12-M36 và 100-500
3. ✅ Xóa sản phẩm cũ (nếu có)
4. ✅ Tạo 2 sản phẩm: Bulong A193M B7 và B8
5. ✅ Tự động tạo 198 variants cho mỗi sản phẩm (11 × 9 = 99 variants × 2 sản phẩm)

## Cách 2: Qua Odoo Web Interface

### Bước 1: Xóa sản phẩm cũ

1. Vào **Inventory > Products**
2. Tìm và xóa các sản phẩm cũ

### Bước 2: Tạo Attributes

1. Vào **Sales > Configuration > Product Attributes & Values**
2. Tạo attribute mới:
   - **Tên:** Đường kính
   - **Hiển thị:** Radio
   - **Tạo biến thể:** Luôn luôn
3. Thêm các giá trị: M12, M14, M16, M18, M20, M22, M24, M27, M30, M32, M36

4. Tạo attribute thứ 2:
   - **Tên:** Chiều dài
   - **Hiển thị:** Radio
   - **Tạo biến thể:** Luôn luôn
5. Thêm các giá trị: 100, 150, 200, 250, 300, 350, 400, 450, 500

### Bước 3: Tạo sản phẩm với Attributes

1. Vào **Inventory > Products > Create**
2. Điền thông tin:
   - **Tên:** Bulong A193M B7
   - **Mã nội bộ:** HB A193M B7
   - **Có thể bán:** ✓
   - **Có thể mua:** ✓

3. Vào tab **"Thuộc tính & biến thể"**
4. Click **"Thêm một dòng"**
5. Chọn **"Đường kính"** và chọn tất cả giá trị (M12-M36)
6. Click **"Thêm một dòng"** lần nữa
7. Chọn **"Chiều dài"** và chọn tất cả giá trị (100-500)
8. Click **"Lưu"**

9. Odoo sẽ tự động tạo **99 variants** (11 × 9)

### Bước 4: Tạo sản phẩm B8

Lặp lại Bước 3 với tên: **Bulong A193M B8**

## Kết quả

Sau khi hoàn thành, bạn sẽ có:

### 2 Product Templates:
- Bulong A193M B7
- Bulong A193M B8

### 198 Product Variants (99 × 2):
- Mỗi variant có SKU tự động: `HB A193M B7 M12 100`, `HB A193M B7 M12 150`, etc.

### Giao diện:
- Tab **"Thuộc tính & biến thể"** hiển thị:
  - **Đường kính:** M12, M14, M16, M18, M20, M22, M24, M27, M30, M32, M36 (dạng pills)
  - **Chiều dài:** 100, 150, 200, 250, 300, 350, 400, 450, 500 (dạng pills)
- Có thể xem và chỉnh sửa từng variant
- Có thể cấu hình attributes

## Lưu ý

⚠️ **Khi thêm/xóa attributes:**
- Odoo sẽ xóa và tạo lại tất cả variants
- Các tùy chỉnh trên variants cũ sẽ bị mất
- Nên backup trước khi thay đổi

✅ **Ưu điểm của cách này:**
- Sử dụng hệ thống native của Odoo
- Variants được quản lý tự động
- Dễ dàng thêm/bớt giá trị attributes
- Giao diện đẹp và chuẩn

## Troubleshooting

### Variants không được tạo
- Kiểm tra "Tạo biến thể" đã set là "Luôn luôn" chưa
- Kiểm tra đã chọn ít nhất 1 giá trị cho mỗi attribute chưa
- Xem logs: `tail -f odoo.log`

### Quá nhiều variants
- Nếu có nhiều attributes với nhiều giá trị, số lượng variants sẽ tăng theo cấp số nhân
- Ví dụ: 11 đường kính × 9 chiều dài = 99 variants
- Nếu thêm 1 attribute nữa với 5 giá trị = 99 × 5 = 495 variants

### Performance
- Với số lượng variants lớn (>1000), có thể ảnh hưởng performance
- Nên sử dụng "Tạo biến thể: Chỉ khi cần" cho attributes ít dùng

---

**Sau khi hoàn thành, bạn sẽ có giao diện giống hệt như trong ảnh! 🎉**
