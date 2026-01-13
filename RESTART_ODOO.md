# 🔄 Restart Odoo Server

## ⚡ Cách nhanh nhất

### Restart Odoo Server

```bash
cd /Users/baonguyen/Desktop/app/Odoo
./restart.sh
```

Hoặc với database cụ thể:
```bash
./restart.sh odoo
```

### Stop Odoo Server

```bash
./stop.sh
```

### Start Odoo Server

```bash
./start.sh
```

Hoặc với database cụ thể:
```bash
./start.sh odoo
```

---

## 📋 Các lệnh có sẵn

### 1. `restart.sh` - Restart Odoo server
- Dừng server đang chạy
- Khởi động lại server
- Tự động kiểm tra port và process

**Cách dùng:**
```bash
./restart.sh [database_name]
```

**Ví dụ:**
```bash
./restart.sh          # Restart với database mặc định (odoo)
./restart.sh odoo     # Restart với database "odoo"
```

### 2. `stop.sh` - Dừng Odoo server
- Tìm và dừng tất cả process Odoo
- Tự động force kill nếu cần

**Cách dùng:**
```bash
./stop.sh
```

### 3. `start.sh` - Khởi động Odoo server
- Khởi động Odoo server
- Kiểm tra port trước khi start
- Hỏi xác nhận nếu port đã được sử dụng

**Cách dùng:**
```bash
./start.sh [database_name]
```

**Ví dụ:**
```bash
./start.sh            # Start với database mặc định (odoo)
./start.sh odoo       # Start với database "odoo"
```

---

## 🎯 Khi nào cần restart?

1. **Sau khi cài đặt/upgrade module**
   ```bash
   ./restart.sh
   ```

2. **Sau khi thay đổi code Python**
   ```bash
   ./restart.sh
   ```

3. **Sau khi thay đổi cấu hình (`odoo.conf`)**
   ```bash
   ./restart.sh
   ```

4. **Khi gặp lỗi "Module not found"**
   ```bash
   ./restart.sh
   ```

5. **Khi server bị treo hoặc không phản hồi**
   ```bash
   ./restart.sh
   ```

---

## 🔍 Kiểm tra trạng thái server

### Kiểm tra port 8069

```bash
lsof -i :8069
```

### Kiểm tra process Odoo

```bash
ps aux | grep odoo-bin
```

### Xem logs

```bash
tail -f /Users/baonguyen/Desktop/app/Odoo/odoo.log
```

---

## ⚠️ Lưu ý

1. **Backup database trước khi restart** (nếu cần)
2. **Đảm bảo PostgreSQL đang chạy** trước khi start Odoo
3. **Kiểm tra port 8069** không bị chiếm bởi ứng dụng khác
4. **Đợi vài giây** sau khi restart để server khởi động hoàn toàn

---

## 🚀 Quick Commands

```bash
# Restart nhanh
./restart.sh

# Stop server
./stop.sh

# Start server
./start.sh

# Xem logs
tail -f odoo.log

# Kiểm tra port
lsof -i :8069
```

---

**Sử dụng `./restart.sh` để restart Odoo server một cách dễ dàng! 🎉**
