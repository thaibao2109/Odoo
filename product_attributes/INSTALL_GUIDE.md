# Hướng dẫn cài đặt Module Product Attributes & SKU Generator

## Bước 1: Đảm bảo Odoo đang chạy

```bash
cd /Users/baonguyen/Desktop/app/Odoo
./start.sh
```

Hoặc kiểm tra:
```bash
curl http://localhost:8069
```

## Bước 2: Cài đặt module

### Cách 1: Qua Web Interface (Khuyến nghị)

1. Truy cập: **http://localhost:8069**
2. Đăng nhập vào Odoo
3. Vào menu **Apps**
4. Bỏ filter "Apps" (click vào "Apps" ở góc trên bên phải)
5. Tìm kiếm: **"Product Attributes & SKU Generator"**
6. Click **Install**

### Cách 2: Qua Command Line

```bash
cd /Users/baonguyen/Desktop/app/Odoo
python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c odoo.conf -i product_attributes -d your_database_name
```

## Bước 3: Cập nhật module (nếu đã cài)

Sau khi thay đổi code, cập nhật module:
```bash
python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c odoo.conf -u product_attributes -d your_database_name
```

## Bước 4: Kiểm tra cài đặt

1. Vào menu **Sales > Thuộc tính sản phẩm**
2. Kiểm tra các menu:
   - Loại thuộc tính
   - Giá trị thuộc tính
   - Sản phẩm

## Bước 5: Thiết lập dữ liệu mẫu

Module đã có sẵn dữ liệu mẫu:
- 6 loại thuộc tính
- Một số giá trị mẫu cho mỗi loại

Bạn có thể:
1. Vào **Sales > Thuộc tính sản phẩm > Giá trị thuộc tính**
2. Thêm các giá trị mới theo nhu cầu công ty

## Bước 6: Sử dụng

1. Tạo sản phẩm mới
2. Vào tab **"Thuộc tính sản phẩm"**
3. Chọn các thuộc tính
4. Mã SKU sẽ được tự động tạo

## Troubleshooting

### Module không xuất hiện trong Apps
- Kiểm tra file `__manifest__.py` có đúng không
- Kiểm tra `addons_path` trong `odoo.conf`
- Restart Odoo server

### Lỗi khi cài đặt
- Xem logs: `tail -f /Users/baonguyen/Desktop/app/Odoo/odoo.log`
- Kiểm tra dependencies: `product`, `sale`
- Đảm bảo database đã được tạo

### Lỗi khi tạo sản phẩm
- Kiểm tra đã có giá trị thuộc tính chưa
- Kiểm tra quyền truy cập
- Xem logs để biết lỗi cụ thể

## Cấu trúc thư mục

Module nằm tại:
```
/Users/baonguyen/Desktop/app/Odoo/product_attributes/
```

Đảm bảo đường dẫn này nằm trong `addons_path` của `odoo.conf`:
```
addons_path = /Users/baonguyen/Desktop/app/Odoo,/Users/baonguyen/Desktop/app/odoo-source/addons
```

---

**Sau khi cài đặt thành công, bạn có thể bắt đầu sử dụng module! 🎉**
