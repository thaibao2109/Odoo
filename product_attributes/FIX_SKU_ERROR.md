# 🔧 Sửa lỗi SKU trùng lặp

## ❌ Lỗi gặp phải

```
Mã SKU "M12 200" đã tồn tại cho variant: [M12 200] Bulong A193M B8 (M12, 200)
```

## 🔍 Nguyên nhân

SKU đang được tạo **không có template code**, dẫn đến:
- SKU chỉ có attributes: `M12 200`
- SKU đúng phải là: `HB A193M B8 M12 200` (có template code)

## ✅ Giải pháp đã áp dụng

### 1. Sửa constraint validation
- ✅ Chỉ kiểm tra SKU unique nếu SKU **đầy đủ** (có template code)
- ✅ Bỏ qua validation nếu SKU chưa có template code (đang trong quá trình cấu hình)

### 2. Đảm bảo SKU luôn có template code
- ✅ Chỉ cập nhật `default_code` nếu SKU bắt đầu bằng template code
- ✅ Không tạo SKU không đầy đủ khi chưa có template code

### 3. Script cập nhật SKU
- ✅ Script `fix_sku_with_template_code.py` để cập nhật lại tất cả variants

## 🚀 Cách sửa lỗi

### Bước 1: Đảm bảo Template Code đã được set

1. Mở sản phẩm **Bulong A193M B8**
2. Vào tab **"Thông tin chung"**
3. Tìm field **"Mã Template (Internal Reference)"**
4. **Nhập:** `HB A193M B8`
5. Click **Save**

### Bước 2: Chạy script cập nhật SKU

```bash
cd /Users/baonguyen/Desktop/app/Odoo/product_attributes/scripts
python3 fix_sku_with_template_code.py odoo
```

Script sẽ:
- Tìm tất cả product templates có template code
- Cập nhật lại SKU cho tất cả variants
- Đảm bảo SKU có đầy đủ template code

### Bước 3: Restart Odoo

```bash
cd /Users/baonguyen/Desktop/app/Odoo
./restart.sh
```

## 📋 Kiểm tra sau khi sửa

1. **Mở sản phẩm Bulong A193M B8**
2. **Vào tab "Thuộc tính & biến thể"**
3. **Click vào một variant** (VD: M12, 200)
4. **Kiểm tra Internal Reference:**
   - ✅ Phải là: `HB A193M B8 M12 200`
   - ❌ Không phải: `M12 200`

## 🎯 Công thức SKU đúng

```
SKU = Template Code + Đường kính + Chiều dài
     = "HB A193M B8" + "M12" + "200"
     = "HB A193M B8 M12 200"
```

## ⚠️ Lưu ý

1. **Luôn set Template Code trước** khi tạo variants
2. **Template Code phải unique** cho mỗi product template
3. **SKU sẽ tự động cập nhật** khi thay đổi Template Code hoặc Attributes

## 🔄 Nếu vẫn gặp lỗi

1. **Kiểm tra Template Code:**
   ```bash
   # Vào Odoo > Inventory > Products
   # Mở sản phẩm và kiểm tra field "Mã Template (Internal Reference)"
   ```

2. **Chạy script cập nhật:**
   ```bash
   python3 fix_sku_with_template_code.py odoo
   ```

3. **Restart Odoo:**
   ```bash
   ./restart.sh
   ```

4. **Kiểm tra logs:**
   ```bash
   tail -f /Users/baonguyen/Desktop/app/Odoo/odoo.log
   ```

---

**Sau khi sửa, SKU sẽ có đầy đủ template code và không còn trùng lặp! 🎉**
