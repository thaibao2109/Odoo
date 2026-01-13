# 🎯 Tính năng tự động tạo mã SKU cho Variants

## 📋 Tổng quan

Module đã được cập nhật để **tự động tạo mã SKU (Internal Reference)** cho từng variant dựa trên:
- **Mã template** (default_code của product template)
- **Mã của các thuộc tính** (attribute values)

## 🔧 Cách hoạt động

### Công thức tạo SKU:
```
SKU = Template Code + Attribute Value 1 + Attribute Value 2 + ...
```

### Ví dụ:
- **Template:** Bulong A193M B7 (default_code: `HB A193M B7`)
- **Attributes:** Đường kính: `M12`, Chiều dài: `100`
- **SKU tự động:** `HB A193M B7 M12 100`

### Thứ tự attributes:
SKU sẽ được tạo theo thứ tự **sequence** của attributes để đảm bảo nhất quán:
1. Đường kính (sequence thấp hơn)
2. Chiều dài (sequence cao hơn)

## ✨ Tính năng

### 1. Tự động tạo SKU
- ✅ SKU được tự động tạo khi:
  - Tạo variant mới
  - Thay đổi attributes
  - Thay đổi template code
  - Thay đổi attribute values

### 2. Tự động cập nhật default_code
- ✅ `default_code` của variant tự động được set = `auto_sku`
- ✅ Đảm bảo đồng bộ giữa SKU và Internal Reference

### 3. Validation
- ✅ Kiểm tra SKU unique
- ✅ Cảnh báo nếu SKU trùng lặp

### 4. Hiển thị trong giao diện
- ✅ Field `auto_sku` hiển thị trong form variant
- ✅ Field `auto_sku` hiển thị trong tree view (optional)
- ✅ Có thể search theo `auto_sku`

## 🎨 Giao diện

### Trong Product Variant Form:
- Field **"Mã SKU (Tự động)"** hiển thị SKU đã được tạo
- Field này **readonly** và chỉ hiển thị khi `auto_generate_sku = True`
- Có thông báo giải thích công thức tạo SKU

### Trong Product Variant Tree:
- Cột **"SKU (Tự động)"** có thể được hiển thị (optional)
- Dễ dàng xem SKU của nhiều variants cùng lúc

## 📝 Ví dụ cụ thể

### Sản phẩm: Bulong A193M B7
- **Template Code:** `HB A193M B7`

### Variants và SKU tự động:

| Đường kính | Chiều dài | SKU Tự động |
|------------|-----------|-------------|
| M12 | 100 | `HB A193M B7 M12 100` |
| M12 | 150 | `HB A193M B7 M12 150` |
| M12 | 200 | `HB A193M B7 M12 200` |
| M14 | 100 | `HB A193M B7 M14 100` |
| M14 | 150 | `HB A193M B7 M14 150` |
| ... | ... | ... |
| M36 | 500 | `HB A193M B7 M36 500` |

## 🔄 Cập nhật module

Để sử dụng tính năng này:

```bash
cd /Users/baonguyen/Desktop/app/Odoo
python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c odoo.conf -u product_attributes -d your_database_name
```

## 🎯 Sử dụng

### 1. Thiết lập Template Code
- Vào **Inventory > Products**
- Mở sản phẩm template (ví dụ: Bulong A193M B7)
- Đặt **Internal Reference** (default_code): `HB A193M B7`
- Bật **"Tự động tạo mã SKU"**

### 2. Xem SKU tự động
- Vào tab **"Thuộc tính & biến thể"**
- Click vào một variant để xem chi tiết
- Bạn sẽ thấy field **"Mã SKU (Tự động)"** với SKU đã được tạo

### 3. Kiểm tra tất cả variants
- Trong form sản phẩm, scroll xuống phần variants
- Hoặc vào **Inventory > Products > Variants**
- Bạn sẽ thấy cột **"SKU (Tự động)"** với SKU của từng variant

## ⚙️ Cấu hình

### Tắt tự động tạo SKU:
1. Vào form product template
2. Tắt **"Tự động tạo mã SKU"**
3. SKU sẽ không được tự động tạo nữa

### Tùy chỉnh SKU:
- Nếu muốn SKU khác với tự động, có thể chỉnh sửa **Internal Reference** của variant trực tiếp
- Tuy nhiên, nếu `auto_generate_sku = True`, SKU sẽ bị ghi đè lại khi attributes thay đổi

## 🔍 Kiểm tra

### Xem SKU của variant:
1. Vào **Inventory > Products**
2. Mở sản phẩm có variants
3. Scroll xuống phần **Variants**
4. Click vào một variant
5. Xem field **"Mã SKU (Tự động)"**

### Tìm kiếm theo SKU:
1. Vào **Inventory > Products**
2. Trong search bar, gõ SKU (ví dụ: `HB A193M B7 M12 100`)
3. Variant tương ứng sẽ được tìm thấy

## 🎉 Lợi ích

1. **Tự động hóa:** Không cần nhập SKU thủ công cho từng variant
2. **Nhất quán:** SKU được tạo theo quy tắc nhất quán
3. **Dễ quản lý:** Dễ dàng tìm kiếm và quản lý variants
4. **Giảm lỗi:** Tránh lỗi nhập liệu thủ công
5. **Mở rộng:** Dễ dàng thêm attributes mới, SKU tự động cập nhật

---

**Tính năng đã sẵn sàng! Cập nhật module và kiểm tra SKU tự động! 🚀**
