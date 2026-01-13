# 🎯 Logic tạo SKU

## Công thức SKU

```
SKU Variant = SKU Template (default_code) + Attribute Values
```

## Ví dụ

### Sản phẩm tổng: Bulong A193M B7
- **Internal Reference (default_code):** `HB A193M B7` ← Nhập ở đây

### Variants:
- Variant 1: Đường kính = M12, Chiều dài = 100
  - **SKU:** `HB A193M B7 M12 100`
  
- Variant 2: Đường kính = M12, Chiều dài = 150
  - **SKU:** `HB A193M B7 M12 150`

- Variant 3: Đường kính = M14, Chiều dài = 100
  - **SKU:** `HB A193M B7 M14 100`

## Cách hoạt động

1. **Nhập SKU tổng trên Product Template:**
   - Mở sản phẩm "Bulong A193M B7"
   - Tìm field "Internal Reference" (default_code)
   - Nhập: `HB A193M B7`
   - Click Save

2. **SKU tự động cho Variants:**
   - Khi có attributes (Đường kính, Chiều dài)
   - Mỗi variant tự động có SKU = Template Code + Attribute Values
   - Ví dụ: `HB A193M B7` + `M12` + `100` = `HB A193M B7 M12 100`

3. **Tự động cập nhật:**
   - Khi thay đổi SKU tổng → Tất cả variants tự động cập nhật
   - Khi thay đổi attributes → SKU variant tự động cập nhật

## Code hiện tại

### Product Template
- Field `default_code` = SKU tổng (ví dụ: "HB A193M B7")
- Khi thay đổi `default_code` → Tất cả variants tự động cập nhật SKU

### Product Product (Variant)
- Field `auto_sku` = computed từ `template.default_code` + `attribute values`
- Field `default_code` = tự động set = `auto_sku`

## Đảm bảo

✅ SKU tổng nhập trên Product Template (default_code)
✅ SKU variant = SKU tổng + Attribute Values
✅ Tự động cập nhật khi thay đổi
