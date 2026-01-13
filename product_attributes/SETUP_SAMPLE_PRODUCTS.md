# Hướng dẫn xóa sản phẩm cũ và tạo sản phẩm mẫu

## Tổng quan

Module đã được chuẩn bị với:
- **198 sản phẩm mẫu**: Bulong A193 B7 và B8
- **Kích thước**: M12, M14, M16, M18, M20, M22, M24, M27, M30, M32, M36
- **Chiều dài**: 100, 150, 200, 250, 300, 350, 400, 450, 500

## Cách 1: Qua Odoo Web Interface (Khuyến nghị)

### Bước 1: Xóa sản phẩm cũ

1. Truy cập: **http://localhost:8069**
2. Đăng nhập
3. Vào **Inventory > Products**
4. Chọn tất cả sản phẩm (checkbox ở header)
5. Click **Action > Delete**
6. Xác nhận xóa

### Bước 2: Cập nhật module để load dữ liệu mẫu

1. Vào **Apps** menu
2. Tìm "Product Attributes & SKU Generator"
3. Click **Upgrade** (hoặc Uninstall rồi Install lại)
4. Dữ liệu mẫu sẽ được tự động tạo

## Cách 2: Qua Command Line

### Bước 1: Xóa sản phẩm cũ

```bash
cd /Users/baonguyen/Desktop/app/Odoo
python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c odoo.conf shell -d your_database_name
```

Trong Odoo shell:
```python
products = env['product.template'].search([])
products.unlink()
print(f"Đã xóa {len(products)} sản phẩm")
exit()
```

### Bước 2: Cập nhật module

```bash
python3 /Users/baonguyen/Desktop/app/odoo-source/odoo-bin -c odoo.conf -u product_attributes -d your_database_name
```

## Cách 3: Sử dụng script tự động

```bash
cd /Users/baonguyen/Desktop/app/Odoo/product_attributes/scripts
./setup_sample_data.sh your_database_name
```

## Kiểm tra kết quả

Sau khi hoàn thành:

1. Vào **Inventory > Products**
2. Bạn sẽ thấy **198 sản phẩm** với tên:
   - Bulong A193M B7 M12 L100
   - Bulong A193M B7 M12 L150
   - ...
   - Bulong A193M B8 M36 L500

3. Mỗi sản phẩm có SKU tự động:
   - HB A193M B7 M12 L100
   - HB A193M B7 M12 L150
   - ...

## Danh sách sản phẩm được tạo

### Bulong A193M B7:
- 11 đường kính × 9 chiều dài = **99 sản phẩm**
- Đường kính: M12, M14, M16, M18, M20, M22, M24, M27, M30, M32, M36
- Chiều dài: 100, 150, 200, 250, 300, 350, 400, 450, 500

### Bulong A193M B8:
- 11 đường kính × 9 chiều dài = **99 sản phẩm**
- Tương tự như B7

**Tổng cộng: 198 sản phẩm**

## Lưu ý

- ⚠️ **Xóa sản phẩm sẽ xóa vĩnh viễn**, bao gồm cả lịch sử bán hàng liên quan
- 💾 **Nên backup database** trước khi xóa
- ✅ Dữ liệu mẫu chỉ được tạo khi cài đặt/cập nhật module lần đầu
- 🔄 Nếu muốn tạo lại, cần xóa sản phẩm và cập nhật module lại

## Troubleshooting

### Sản phẩm không được tạo
- Kiểm tra module đã được cài đặt chưa
- Kiểm tra file `product_sample_products.xml` có trong manifest không
- Xem logs: `tail -f /Users/baonguyen/Desktop/app/Odoo/odoo.log`

### Lỗi khi xóa sản phẩm
- Có thể sản phẩm đang được sử dụng trong đơn hàng
- Kiểm tra constraints trong Odoo
- Xem logs để biết lỗi cụ thể

### SKU không đúng
- Kiểm tra các giá trị thuộc tính đã được tạo chưa
- Kiểm tra `auto_generate_sku` đã bật chưa
- Xem tab "Thuộc tính sản phẩm" trong form sản phẩm

---

**Sau khi hoàn thành, bạn sẽ có 198 sản phẩm mẫu sẵn sàng sử dụng! 🎉**
