# ✅ Tính năng tự động tạo SKU đã sẵn sàng!

## 🎯 Tính năng

**Tự động tạo mã SKU (Internal Reference) cho từng variant** dựa trên:
- Mã template (default_code của product template)
- Mã của các thuộc tính (attribute values)

## 📋 Công thức

```
SKU = Template Code + Đường kính + Chiều dài + ...
```

### Ví dụ:
- **Template:** Bulong A193M B7 (default_code: `HB A193M B7`)
- **Variant có:** Đường kính `M12`, Chiều dài `100`
- **SKU tự động:** `HB A193M B7 M12 100`

## 🔄 Cập nhật module

Để kích hoạt tính năng:

```bash
cd /Users/baonguyen/Desktop/app/Odoo
python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c odoo.conf -u product_attributes -d odoo
```

Sau đó **restart Odoo server**.

## 🎨 Xem kết quả

### 1. Xem SKU trong Variant Form:
1. Vào **Inventory > Products**
2. Mở sản phẩm **Bulong A193M B7**
3. Scroll xuống phần **Variants**
4. Click vào một variant (ví dụ: M12, 100)
5. Bạn sẽ thấy field **"Mã SKU (Tự động)"** với giá trị: `HB A193M B7 M12 100`

### 2. Xem SKU trong Variant List:
1. Vào **Inventory > Products**
2. Mở sản phẩm có variants
3. Scroll xuống phần variants
4. Bật cột **"SKU (Tự động)"** (click vào biểu tượng cột)
5. Bạn sẽ thấy SKU của tất cả variants

## ✨ Tính năng tự động

- ✅ **Tự động tạo** khi tạo variant mới
- ✅ **Tự động cập nhật** khi thay đổi attributes
- ✅ **Tự động cập nhật** khi thay đổi template code
- ✅ **Tự động set** vào default_code của variant
- ✅ **Validation** đảm bảo SKU unique

## 📊 Ví dụ SKU đã được tạo

Sau khi cập nhật module, các variants sẽ có SKU như sau:

| Variant | SKU Tự động |
|---------|-------------|
| Bulong A193M B7 - M12 - 100 | `HB A193M B7 M12 100` |
| Bulong A193M B7 - M12 - 150 | `HB A193M B7 M12 150` |
| Bulong A193M B7 - M14 - 100 | `HB A193M B7 M14 100` |
| Bulong A193M B8 - M12 - 100 | `HB A193M B8 M12 100` |
| ... | ... |

## 🔍 Kiểm tra

1. **Mở variant** trong form sản phẩm
2. Kiểm tra field **"Mã SKU (Tự động)"**
3. Kiểm tra **Internal Reference** (default_code) đã được set = auto_sku

## ⚙️ Cấu hình

### Bật/tắt tự động tạo SKU:
1. Vào form **product template**
2. Bật/tắt **"Tự động tạo mã SKU"**
3. Nếu tắt, SKU sẽ không được tự động tạo

---

**Tính năng đã sẵn sàng! Cập nhật module và kiểm tra SKU tự động! 🚀**
