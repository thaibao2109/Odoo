# Order Progress Management Module

Module quản lý tiến độ chi tiết đơn hàng cho Odoo, hỗ trợ theo dõi đơn hàng theo 3 hạng mục:
- **Sản xuất** (Manufacturing)
- **Mua hàng** (Purchasing/Commercial)
- **Tồn kho** (Inventory)

## Tính năng

### 1. Status Bar (Thanh trạng thái tiến độ)
- MỚI (New)
- ĐANG SX (In Production)
- MUA NGOÀI (External Purchase)
- CHƯA GIAO (Not Delivered)
- ĐÃ GIAO (Delivered)
- HOÀN THÀNH (Completed)
- HỦY (Cancelled)

### 2. Quản lý theo hạng mục
Mỗi dòng sản phẩm có 3 checkbox:
- **Mua**: Đánh dấu sản phẩm cần mua hàng
- **SX**: Đánh dấu sản phẩm cần sản xuất
- **KHO**: Đánh dấu sản phẩm từ tồn kho

### 3. Các section quản lý

#### Người phụ trách
- Ngày thực hiện
- Nhân viên báo giá
- Nhân viên kinh doanh
- Ngày giao hàng dự kiến (SX)
- Ghi chú nội bộ SX

#### BÁO GIÁ
- Ghi chú báo giá
- Tài liệu đính kèm

#### MUA HÀNG
- Ghi chú mua hàng
- Yêu cầu mua hàng
- Ngày deadline
- Ngày hoàn thành
- Ghi chú

#### KHO (Inventory)
- Ghi chú kho

#### SẢN XUẤT (Manufacturing)
- Yêu cầu sản xuất
- Ngày nhập kho
- Ghi chú

### 4. Product Lines với Tabs
- Chi tiết bom hàng
- Chi tiết đơn hàng
- Tài liệu
- Mua nguyên vật liệu
- Yêu cầu gia công

### 5. Activity Feed
Tích hợp với Odoo chatter để theo dõi lịch sử thay đổi và ghi chú

## Cài đặt

1. Copy module vào thư mục addons của Odoo
2. Cập nhật app list: `odoo-bin -u all -d your_database`
3. Hoặc cài đặt qua Apps menu trong Odoo

## Yêu cầu

- Odoo 14.0 trở lên
- Module `sale`
- Module `stock` (cho inventory)
- Module `mrp` (cho manufacturing)
- Module `purchase` (cho purchasing)

## Sử dụng

1. Vào menu **Quản lý tiến độ đơn hàng > Đơn hàng**
2. Tạo hoặc mở một đơn hàng
3. Sử dụng status bar để cập nhật trạng thái tiến độ
4. Đánh dấu checkbox Mua/SX/KHO cho từng sản phẩm
5. Cập nhật các ghi chú và thông tin trong các section tương ứng
6. Theo dõi activity feed để xem lịch sử thay đổi

## Cấu trúc Module

```
order_progress_management/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── sale_order.py
│   └── sale_order_line.py
├── views/
│   ├── __init__.py
│   ├── sale_order_views.xml
│   └── order_progress_menus.xml
├── security/
│   └── ir.model.access.csv
├── static/
│   └── src/
│       ├── css/
│       │   └── order_progress.css
│       └── js/
│           └── order_progress.js
└── README.md
```

## Tác giả

Odoo

## License

LGPL-3
