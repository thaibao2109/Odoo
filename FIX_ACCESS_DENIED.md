# ✅ Khắc phục lỗi "Access Denied" khi tạo Database

## Vấn đề
```
Database creation error: Access Denied
```

## Nguyên nhân
Lỗi này xảy ra vì Odoo yêu cầu **Master Password** (admin password) khi tạo database qua web interface. Master password được lưu trong file `odoo.conf` với tên `admin_passwd`.

## Giải pháp

### Cách 1: Tạo Database thủ công (Khuyến nghị)

Chạy script tự động:
```bash
cd /Users/baonguyen/Desktop/app/Odoo
./create_database.sh odoo_db admin@example.com admin vi_VN
```

Hoặc tạo thủ công:
```bash
# 1. Tạo database
/opt/homebrew/opt/postgresql@14/bin/psql -U odoo -d postgres -c "CREATE DATABASE odoo_db ENCODING 'utf8' TEMPLATE template0;"

# 2. Khởi tạo database với Odoo (không có demo data)
python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c odoo.conf -d odoo_db --stop-after-init --without-demo=all

# Hoặc với demo data
python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c odoo.conf -d odoo_db --stop-after-init
```

### Cách 2: Sử dụng Master Password trong Web Interface

Khi tạo database qua web interface (http://localhost:8069), bạn cần nhập **Master Password**.

Master password mặc định: **`admin`**

Hoặc bạn có thể đặt master password mới trong file `odoo.conf`:
```ini
admin_passwd = admin
```

Sau đó restart Odoo server.

## Các bước chi tiết

### Bước 1: Tạo database
```bash
cd /Users/baonguyen/Desktop/app/Odoo
./create_database.sh odoo_db
```

### Bước 2: Khởi tạo database với Odoo
```bash
# Không có demo data (nhanh hơn)
python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c odoo.conf -d odoo_db --stop-after-init --without-demo=all

# Hoặc với demo data (có dữ liệu mẫu)
python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c odoo.conf -d odoo_db --stop-after-init
```

### Bước 3: Truy cập Odoo
1. Mở trình duyệt: http://localhost:8069
2. Chọn database: `odoo_db`
3. Đăng nhập:
   - Email: `admin@example.com` (hoặc email bạn đã đặt)
   - Password: `admin` (hoặc password bạn đã đặt)

### Bước 4: Cài đặt module
1. Vào menu **Apps**
2. Bỏ filter "Apps"
3. Tìm "Order Progress Management"
4. Click **Install**

## Lưu ý

- Master password khác với password đăng nhập Odoo
- Master password dùng để tạo/xóa database
- Password đăng nhập dùng để đăng nhập vào Odoo sau khi database đã được tạo

## Kiểm tra

Sau khi tạo database, kiểm tra:
```bash
# Xem danh sách database
/opt/homebrew/opt/postgresql@14/bin/psql -U odoo -d postgres -c "\l" | grep odoo
```

---

**Sau khi hoàn thành các bước trên, bạn có thể sử dụng Odoo và module Order Progress Management! 🎉**
