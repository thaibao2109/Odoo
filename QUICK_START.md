# Hướng dẫn nhanh chạy Odoo

## Cách nhanh nhất: Sử dụng Docker (Khuyến nghị)

### Bước 1: Cài đặt Docker
- macOS: Tải Docker Desktop từ https://www.docker.com/products/docker-desktop
- Hoặc cài qua Homebrew: `brew install --cask docker`

### Bước 2: Chạy Odoo
```bash
cd /Users/baonguyen/Desktop/app/Odoo
docker-compose up
```

### Bước 3: Truy cập
- Mở trình duyệt: http://localhost:8069
- Tạo database mới với tên bất kỳ
- Master password: `admin` (hoặc để trống)
- Cài đặt module "Order Progress Management"

---

## Cách 2: Cài đặt thủ công

### Bước 1: Cài đặt PostgreSQL
```bash
# macOS
brew install postgresql@14
brew services start postgresql@14

# Tạo user
createuser -s $USER
```

### Bước 2: Cài đặt Odoo
```bash
# Cài đặt Odoo
pip3 install odoo

# Hoặc clone từ GitHub
git clone https://github.com/odoo/odoo.git ~/odoo
cd ~/odoo
pip3 install -r requirements.txt
```

### Bước 3: Chạy Odoo
```bash
cd /Users/baonguyen/Desktop/app/Odoo
./run_odoo.sh
```

Hoặc thủ công:
```bash
odoo-bin -c odoo.conf
```

---

## Kiểm tra

Sau khi chạy, truy cập: http://localhost:8069

Nếu thấy trang đăng nhập Odoo là thành công!

---

## Cài đặt module

1. Đăng nhập Odoo
2. Vào **Apps** menu
3. Bỏ filter "Apps" (click vào "Apps" ở góc trên)
4. Tìm "Order Progress Management"
5. Click **Install**

---

## Lưu ý

- Port mặc định: 8069
- Database user mặc định: odoo/odoo
- Logs: Xem trong terminal hoặc file `odoo.log`
