# 📍 Vị trí field "Mã Template (Internal Reference)"

## ✅ Đã cập nhật!

Field **"Mã Template (Internal Reference)"** giờ đã được hiển thị **NGAY SAU TÊN SẢN PHẨM** trong form sản phẩm.

## 🎯 Cách tìm field

1. **Truy cập:** http://localhost:8069
2. **Đăng nhập**
3. Vào **Inventory > Products**
4. Mở sản phẩm **"Bulong A193M B7"** (hoặc bất kỳ sản phẩm nào)
5. **Tìm field ngay dưới tên sản phẩm:**

```
┌─────────────────────────────────────────┐
│ Product Name: Bulong A193M B7          │
├─────────────────────────────────────────┤
│ Mã Template (Internal Reference):       │
│ [                    ]  ← ĐÂY!          │
│ VD: HB A193M B7 (dùng làm phần đầu SKU)│
├─────────────────────────────────────────┤
│ 💡 Template Code: Mã này + Attributes...│
└─────────────────────────────────────────┘
```

## 📝 Cách sử dụng

1. **Click vào field** "Mã Template (Internal Reference)"
2. **Nhập:** `HB A193M B7`
3. **Click Save** (Lưu)
4. ✅ Tất cả variants sẽ tự động có SKU: `HB A193M B7 M12 100`, `HB A193M B7 M12 150`, ...

## 🔄 Nếu vẫn không thấy

1. **Refresh trang** (F5 hoặc Cmd+R)
2. **Clear cache** trình duyệt
3. **Restart Odoo server** (nếu cần)
4. **Kiểm tra module đã update chưa:**
   - Vào **Apps**
   - Tìm module **"product_attributes"**
   - Click **Upgrade**

## 💡 Lưu ý

- Field này **KHÔNG PHẢI** là nút bấm
- Field này là **Ô NHẬP TEXT** (text input)
- Nằm **NGAY DƯỚI TÊN SẢN PHẨM**
- Có label: **"Mã Template (Internal Reference)"**

---

**Sau khi cập nhật module, field sẽ hiển thị rõ ràng! 🎉**
