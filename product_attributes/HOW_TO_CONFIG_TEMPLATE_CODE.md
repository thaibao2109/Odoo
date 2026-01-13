# 📝 Hướng dẫn cấu hình Template Code (HB A193M B7)

## 🎯 Template Code là gì?

**Template Code** (Internal Reference) là mã cơ bản của sản phẩm, được dùng làm phần đầu của SKU cho tất cả variants.

Ví dụ:
- Template Code: `HB A193M B7`
- Variant có: Đường kính `M12`, Chiều dài `100`
- **SKU cuối cùng:** `HB A193M B7 M12 100`

## 🔧 Cách cấu hình Template Code

### Bước 1: Mở sản phẩm Template

1. **Truy cập:** http://localhost:8069
2. **Đăng nhập**
3. Vào **Inventory > Products**
4. Tìm và mở **"Bulong A193M B7"** (hoặc sản phẩm bạn muốn cấu hình)

### Bước 2: Cấu hình Internal Reference

1. Trong form sản phẩm, tìm field **"Internal Reference"** (Mã nội bộ)
2. Field này thường nằm ở:
   - **Tab "General Information"** (Thông tin chung)
   - Hoặc ngay dưới tên sản phẩm
3. **Nhập template code:** `HB A193M B7`
4. Click **Save** (Lưu)

### Bước 3: Xác nhận

Sau khi lưu, tất cả variants sẽ tự động có SKU mới:
- `HB A193M B7 M12 100`
- `HB A193M B7 M12 150`
- `HB A193M B7 M14 100`
- ...

## 📋 Ví dụ cấu hình

### Sản phẩm 1: Bulong A193M B7
- **Internal Reference:** `HB A193M B7`
- **SKU variants:** `HB A193M B7 M12 100`, `HB A193M B7 M12 150`, ...

### Sản phẩm 2: Bulong A193M B8
- **Internal Reference:** `HB A193M B8`
- **SKU variants:** `HB A193M B8 M12 100`, `HB A193M B8 M12 150`, ...

## 🎨 Vị trí field trong giao diện

```
┌─────────────────────────────────────────┐
│ Product Name: Bulong A193M B7          │
├─────────────────────────────────────────┤
│ Internal Reference: [HB A193M B7]  ← ĐÂY!│
│                                         │
│ [Thông tin chung] [Thuộc tính & biến thể]│
└─────────────────────────────────────────┘
```

## ⚡ Cập nhật tự động

Sau khi thay đổi **Internal Reference**:
- ✅ Tất cả variants sẽ tự động cập nhật SKU
- ✅ Không cần làm gì thêm
- ✅ SKU mới = Template Code mới + Attributes

## 🔄 Nếu muốn thay đổi Template Code

1. Mở sản phẩm template
2. Sửa **Internal Reference**
3. Click **Save**
4. Tất cả variants tự động cập nhật!

## 💡 Lưu ý

- **Template Code** khác với **Product Name**
- **Product Name:** "Bulong A193M B7" (tên hiển thị)
- **Internal Reference:** "HB A193M B7" (mã dùng trong SKU)

## 🎯 Công thức SKU

```
SKU = Internal Reference + Đường kính + Chiều dài
     = "HB A193M B7" + "M12" + "100"
     = "HB A193M B7 M12 100"
```

---

**Cấu hình Internal Reference và SKU sẽ tự động cập nhật! 🎉**
