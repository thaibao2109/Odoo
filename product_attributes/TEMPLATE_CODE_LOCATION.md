# 📍 Vị trí field "Mã Template (Internal Reference)"

## ✅ Đã cập nhật lại!

Field **"Mã Template (Internal Reference)"** giờ đã được thêm vào **TAB "THÔNG TIN CHUNG"** (General Information), ngay **TRƯỚC field "Loại sản phẩm"**.

## 🎯 Cách tìm field

1. **Truy cập:** http://localhost:8069
2. **Đăng nhập**
3. Vào **Inventory > Products**
4. Mở sản phẩm **"Bulong A193M B8"** (hoặc bất kỳ sản phẩm nào)
5. **Đảm bảo đang ở tab "Thông tin chung"** (tab đầu tiên)
6. **Tìm field ở đầu tab, trước "Loại sản phẩm":**

```
┌─────────────────────────────────────────┐
│ Tab: Thông tin chung                    │
├─────────────────────────────────────────┤
│ ┌─────────────────────────────────────┐ │
│ │ Mã Template (SKU Base)             │ │
│ │                                     │ │
│ │ Mã Template (Internal Reference):  │ │
│ │ [HB A193M B8]  ← ĐÂY!              │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ 💡 Template Code: Mã này + Attributes...│
│                                         │
│ Loại sản phẩm: [Sản phẩm lưu kho]      │
│ ...                                     │
└─────────────────────────────────────────┘
```

## 📝 Cách sử dụng

1. **Mở sản phẩm** (VD: Bulong A193M B8)
2. **Đảm bảo đang ở tab "Thông tin chung"**
3. **Scroll lên đầu tab** (nếu cần)
4. **Tìm group "Mã Template (SKU Base)"**
5. **Click vào field** "Mã Template (Internal Reference)"
6. **Nhập hoặc sửa:** `HB A193M B7` (hoặc mã khác)
7. **Click Save** (Lưu)
8. ✅ Tất cả variants sẽ tự động có SKU mới

## 🔄 Nếu vẫn không thấy

### Bước 1: Refresh và Clear Cache
1. **Hard refresh:** `Cmd + Shift + R` (Mac) hoặc `Ctrl + Shift + R` (Windows)
2. **Hoặc clear cache trình duyệt**

### Bước 2: Kiểm tra Module
1. Vào **Apps**
2. Tìm module **"product_attributes"**
3. Click **Upgrade** (Nâng cấp)
4. **Restart Odoo** (nếu cần)

### Bước 3: Kiểm tra Tab
- **Đảm bảo đang ở tab "Thông tin chung"** (tab đầu tiên)
- **KHÔNG phải** tab "Thuộc tính & biến thể"

### Bước 4: Scroll lên đầu tab
- Field nằm ở **đầu tab "Thông tin chung"**
- **Trước field "Loại sản phẩm"**

## 💡 Lưu ý quan trọng

- Field này nằm trong **group "Mã Template (SKU Base)"**
- Nằm ở **đầu tab "Thông tin chung"**
- **Trước field "Loại sản phẩm"**
- Có **label rõ ràng:** "Mã Template (Internal Reference)"
- Có **placeholder:** "VD: HB A193M B7 (dùng làm phần đầu của SKU)"
- Có **alert box màu xanh** giải thích cách dùng

## 🎨 Mô tả chi tiết

Field này sẽ hiển thị như sau:

```
┌─────────────────────────────────────────────┐
│ Mã Template (SKU Base)                      │
│                                             │
│ Mã Template (Internal Reference) *          │
│ ┌─────────────────────────────────────────┐ │
│ │ HB A193M B8                             │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ 💡 Template Code: Mã này + Attributes  │ │
│ │    = SKU của variants                   │ │
│ │                                         │ │
│ │ Ví dụ: "HB A193M B7" + "M12" + "100"   │ │
│ │      = "HB A193M B7 M12 100"           │ │
│ │                                         │ │
│ │ 📝 Cách dùng: Nhập mã template (VD:     │ │
│ │    HB A193M B7) vào field trên, sau đó │ │
│ │    Save. Tất cả variants sẽ tự động có │ │
│ │    SKU mới.                             │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

---

**Sau khi upgrade module và refresh, field sẽ hiển thị rõ ràng ở đầu tab "Thông tin chung"! 🎉**
