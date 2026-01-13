#!/bin/bash

# Script để xóa sản phẩm cũ và tạo sản phẩm mẫu

echo "=========================================="
echo "Setup Sample Products"
echo "=========================================="
echo ""

# Cấu hình
DB_NAME="${1:-odoo_db}"
ODOO_BIN="/Users/baonguyen/Desktop/app/odoo-source/odoo-bin"
CONFIG_FILE="/Users/baonguyen/Desktop/app/Odoo/odoo.conf"

echo "Database: $DB_NAME"
echo ""

# Bước 1: Xóa tất cả sản phẩm cũ
echo "Bước 1: Xóa tất cả sản phẩm cũ..."
echo "⚠️  Bạn có chắc muốn xóa TẤT CẢ sản phẩm? (yes/no): "
read confirm

if [ "$confirm" != "yes" ]; then
    echo "❌ Đã hủy."
    exit 1
fi

# Tạo script Python để xóa sản phẩm
cat > /tmp/delete_products.py << 'EOF'
import xmlrpc.client

ODOO_URL = 'http://localhost:8069'
ODOO_DB = 'odoo_db'  # Sẽ được thay thế
ODOO_USERNAME = 'admin'
ODOO_PASSWORD = 'admin'

common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})

if uid:
    models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
    product_ids = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'product.template', 'search', [[]])
    if product_ids:
        models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'product.template', 'unlink', [product_ids])
        print(f"Đã xóa {len(product_ids)} sản phẩm")
    else:
        print("Không có sản phẩm nào")
else:
    print("Lỗi xác thực")
EOF

# Thay thế database name
sed -i '' "s/ODOO_DB = '.*'/ODOO_DB = '$DB_NAME'/" /tmp/delete_products.py

python3 /tmp/delete_products.py

echo ""
echo "Bước 2: Cập nhật module để load dữ liệu mẫu..."
python3 "$ODOO_BIN" -c "$CONFIG_FILE" -u product_attributes -d "$DB_NAME" --stop-after-init

echo ""
echo "✅ Hoàn thành!"
echo "Truy cập Odoo để xem các sản phẩm mẫu đã được tạo."
