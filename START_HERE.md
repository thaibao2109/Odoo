# 🚀 BẮT ĐẦU TẠI ĐÂY - Chạy Odoo

## ⚡ Cách nhanh nhất

### Bước 1: Cài đặt PostgreSQL (nếu chưa có)

```bash
# Kiểm tra PostgreSQL
psql --version

# Nếu chưa có, cài đặt:
brew install postgresql@14
brew services start postgresql@14

# Tạo database user
createuser -s $USER
```

### Bước 2: Chạy Odoo

```bash
cd /Users/baonguyen/Desktop/app/Odoo
./start.sh
```

Hoặc chạy trực tiếp:
```bash
python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c /Users/baonguyen/Desktop/app/Odoo/odoo.conf
```

### Bước 3: Truy cập Odoo

1. Mở trình duyệt: **http://localhost:8069**
2. Tạo database mới:
   - Database name: `odoo_db` (hoặc tên bất kỳ)
   - Email: `admin@example.com`
   - Password: `admin`
   - Language: `Vietnamese` hoặc `English`
   - Country: `Vietnam`
   - Demo data: ✅ (để có dữ liệu mẫu)

### Bước 4: Cài đặt module

1. Đăng nhập với email và password vừa tạo
2. Vào menu **Apps**
3. Bỏ filter "Apps" (click vào "Apps" ở góc trên bên phải)
4. Tìm kiếm: **"Order Progress Management"**
5. Click **Install**

---

## 📋 Kiểm tra trước khi chạy

- ✅ Odoo source đã được clone: `/Users/baonguyen/Desktop/app/odoo-source`
- ✅ Dependencies đã được cài đặt
- ⚠️ PostgreSQL cần được cài đặt và chạy

---

## 🔧 Troubleshooting

### Lỗi: "Could not connect to database"

**Giải pháp:**
```bash
# Khởi động PostgreSQL
brew services start postgresql@14

# Hoặc nếu dùng PostgreSQL khác:
pg_ctl -D /usr/local/var/postgres start
```

### Lỗi: "Port 8069 already in use"

**Giải pháp:**
- Thay đổi port trong `odoo.conf`: `http_port = 8070`
- Hoặc dừng process: `lsof -ti:8069 | xargs kill`

### Lỗi: "Module not found"

**Giải pháp:**
- Kiểm tra `addons_path` trong `odoo.conf`
- Đảm bảo thư mục `order_progress_management` nằm trong addons_path
- Cập nhật module: `./start.sh -u order_progress_management -d odoo_db`

---

## 📝 Lệnh hữu ích

```bash
# Chạy Odoo với database cụ thể
./start.sh -d odoo_db

# Cập nhật module
./start.sh -u order_progress_management -d odoo_db

# Chạy với log level debug
./start.sh --log-level=debug

# Xem logs
tail -f odoo.log
```

---

## 🎯 Sau khi chạy thành công

1. Truy cập: http://localhost:8069
2. Tạo database
3. Cài đặt module "Order Progress Management"
4. Vào menu **Quản lý tiến độ đơn hàng > Đơn hàng**
5. Tạo đơn hàng mới và test các tính năng!

---

**Chúc bạn thành công! 🎉**
