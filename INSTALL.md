# Hướng dẫn cài đặt và chạy Odoo

## Cài đặt Odoo

### Cách 1: Cài đặt qua pip (Khuyến nghị cho development)

```bash
# Cài đặt Odoo
pip3 install odoo

# Hoặc cài đặt từ source
pip3 install -e git+https://github.com/odoo/odoo.git@master#egg=odoo
```

### Cách 2: Clone từ GitHub

```bash
# Clone Odoo repository
git clone https://github.com/odoo/odoo.git ~/odoo
cd ~/odoo

# Cài đặt dependencies
pip3 install -r requirements.txt
```

### Cách 3: Sử dụng Docker (Dễ nhất)

```bash
# Pull Odoo image
docker pull odoo:latest

# Chạy Odoo container
docker run -d \
  -p 8069:8069 \
  -v $(pwd)/order_progress_management:/mnt/extra-addons/order_progress_management \
  -e ODOO_DB_HOST=db \
  --name odoo \
  odoo:latest
```

## Cài đặt PostgreSQL

Odoo cần PostgreSQL để lưu trữ dữ liệu:

### macOS (sử dụng Homebrew)
```bash
brew install postgresql@14
brew services start postgresql@14
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo systemctl start postgresql
```

### Tạo database user
```bash
sudo -u postgres createuser -s odoo
# Hoặc nếu không có quyền sudo:
createuser -s $USER
```

## Chạy Odoo

### Cách 1: Sử dụng script tự động
```bash
cd /Users/baonguyen/Desktop/app/Odoo
./run_odoo.sh
```

### Cách 2: Chạy thủ công

Nếu Odoo được cài qua pip:
```bash
odoo-bin -c odoo.conf
```

Nếu Odoo được clone từ GitHub:
```bash
~/odoo/odoo-bin -c odoo.conf
```

### Cách 3: Chạy với Docker
```bash
docker-compose up
```

## Cấu hình

1. Chỉnh sửa file `odoo.conf` để phù hợp với môi trường của bạn
2. Đảm bảo PostgreSQL đang chạy
3. Đảm bảo module `order_progress_management` nằm trong `addons_path`

## Truy cập Odoo

1. Mở trình duyệt và truy cập: `http://localhost:8069`
2. Tạo database mới hoặc chọn database có sẵn
3. Cài đặt module `order_progress_management`:
   - Vào Apps menu
   - Bỏ filter "Apps"
   - Tìm "Order Progress Management"
   - Click Install

## Troubleshooting

### Lỗi: "odoo-bin: command not found"
- Đảm bảo Odoo đã được cài đặt
- Thêm đường dẫn Odoo vào PATH
- Hoặc sử dụng đường dẫn đầy đủ: `python3 /path/to/odoo/odoo-bin`

### Lỗi: "Could not connect to database"
- Kiểm tra PostgreSQL đang chạy: `pg_isready`
- Kiểm tra thông tin database trong `odoo.conf`
- Tạo database user nếu chưa có

### Lỗi: "Module not found"
- Kiểm tra `addons_path` trong `odoo.conf`
- Đảm bảo thư mục module có file `__manifest__.py`
- Cập nhật app list: `odoo-bin -u all -d your_database`

### Lỗi: "Port 8069 already in use"
- Thay đổi port trong `odoo.conf`: `http_port = 8070`
- Hoặc dừng process đang sử dụng port: `lsof -ti:8069 | xargs kill`

## Cập nhật module

Sau khi thay đổi code, cập nhật module:
```bash
odoo-bin -u order_progress_management -d your_database
```

## Logs

Xem logs tại: `odoo.log` hoặc trong terminal nơi chạy Odoo.
