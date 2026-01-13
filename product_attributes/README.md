# Product Attributes & SKU Generator Module

Module quản lý thuộc tính sản phẩm và tự động tạo mã SKU cho Odoo.

## Tính năng

### 1. Quản lý thuộc tính sản phẩm
- **Loại sản phẩm** (Product Type): HHB, SB, CHB, FN, GP, LN, etc.
- **Tiêu chuẩn** (Standard): A194, D933, F3125, A193M, etc.
- **Cấp bền** (Grade): B7, A325, 2H, L7, etc.
- **Kích thước** (Size): M16, L300, 11/2", etc.
- **Bề mặt** (Surface): PTFE, HDG, ZP, BO, etc.
- **Đặc biệt** (Special): FT, HD, TEST, NL200, etc.

### 2. Tự động tạo mã SKU
Công thức: **Loại sản phẩm + Tiêu chuẩn + Cấp bền + Kích thước + Bề mặt + Đặc biệt**

Ví dụ:
- `HHB A193M B7 M16 L300 PTFE`
- `HB F3125 A325 11-1 2L250 HDG`

### 3. Quản lý từ điển thuộc tính
- Mỗi giá trị có: Tên đầy đủ, Từ viết tắt, Giải thích (Tiếng Việt), Tiếng Anh
- Dễ dàng thêm/sửa/xóa giá trị
- Phân loại theo loại thuộc tính

### 4. Validation
- Đảm bảo SKU unique
- Kiểm tra trùng lặp khi tạo sản phẩm mới
- Cảnh báo nếu SKU đã tồn tại

## Cấu trúc Module

```
product_attributes/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── product_attribute_type.py    # Loại thuộc tính
│   ├── product_attribute_value.py   # Giá trị thuộc tính
│   └── product_template.py          # Mở rộng product.template
├── views/
│   ├── product_attribute_views.xml   # Views cho thuộc tính
│   ├── product_template_views.xml   # Views cho sản phẩm
│   └── product_attribute_menus.xml  # Menu items
├── data/
│   └── product_attribute_data.xml    # Dữ liệu mẫu
└── security/
    └── ir.model.access.csv          # Phân quyền
```

## Cách sử dụng

### Bước 1: Cài đặt module
1. Vào **Apps** menu
2. Tìm "Product Attributes & SKU Generator"
3. Click **Install**

### Bước 2: Thiết lập thuộc tính

#### Quản lý Loại thuộc tính:
1. Vào **Sales > Thuộc tính sản phẩm > Loại thuộc tính**
2. Các loại đã có sẵn: Loại sản phẩm, Tiêu chuẩn, Cấp bền, Kích thước, Bề mặt, Đặc biệt

#### Quản lý Giá trị thuộc tính:
1. Vào **Sales > Thuộc tính sản phẩm > Giá trị thuộc tính**
2. Thêm các giá trị mới:
   - **Loại sản phẩm:** HHB, SB, CHB, FN, GP, LN, etc.
   - **Tiêu chuẩn:** A194, D933, F3125, A193M, etc.
   - **Cấp bền:** B7, A325, 2H, L7, etc.
   - **Kích thước:** M16, L300, 11/2", M20.8, etc.
   - **Bề mặt:** PTFE, HDG, ZP, BO, ZNI, etc.
   - **Đặc biệt:** FT, HD, TEST, NL200, 3T, etc.

### Bước 3: Tạo sản phẩm với thuộc tính

1. Vào **Sales > Thuộc tính sản phẩm > Sản phẩm** hoặc **Inventory > Products**
2. Tạo sản phẩm mới
3. Vào tab **"Thuộc tính sản phẩm"**
4. Chọn các thuộc tính:
   - Loại sản phẩm: HHB
   - Tiêu chuẩn: A193M
   - Cấp bền: B7
   - Kích thước: M16, L300
   - Bề mặt: PTFE
   - Đặc biệt: (nếu có)
5. Mã SKU sẽ được tự động tạo: `HHB A193M B7 M16 L300 PTFE`
6. Mã SKU tự động được gán vào **Internal Reference** (default_code)

### Bước 4: Tùy chỉnh SKU (nếu cần)

- Nếu muốn nhập SKU thủ công:
  1. Tắt **"Tự động tạo mã SKU"**
  2. Nhập mã SKU tùy chỉnh vào trường **"Mã SKU tùy chỉnh"**

## Ví dụ sử dụng

### Ví dụ 1: Heavy Hex Bolt
- Loại sản phẩm: **HHB** (Heavy hex bolt)
- Tiêu chuẩn: **A193M** (ASTM A193M)
- Cấp bền: **B7** (Grade B7)
- Kích thước: **M16** (đường kính 16), **L300** (chiều dài 300)
- Bề mặt: **PTFE** (PTFE Coating)
- **SKU tự động:** `HHB A193M B7 M16 L300 PTFE`

### Ví dụ 2: Hex Bolt với Hot Dip Galvanized
- Loại sản phẩm: **HB** (Hex Bolt)
- Tiêu chuẩn: **F3125** (ASTM F3125)
- Cấp bền: **A325** (Grade A325)
- Kích thước: **11-1** (1 1/2"), **2L250** (250mm length)
- Bề mặt: **HDG** (Hot Dip Galvanized)
- **SKU tự động:** `HB F3125 A325 11-1 2L250 HDG`

## Lợi ích

1. **Tự động hóa:** Không cần nhập SKU thủ công, giảm lỗi
2. **Chuẩn hóa:** Đảm bảo SKU nhất quán theo quy tắc công ty
3. **Dễ quản lý:** Từ điển thuộc tính tập trung, dễ cập nhật
4. **Tìm kiếm:** Dễ dàng tìm sản phẩm theo thuộc tính
5. **Mở rộng:** Dễ dàng thêm thuộc tính mới khi cần

## Best Practices

1. **Thiết lập từ điển trước:** Tạo đầy đủ các giá trị thuộc tính trước khi tạo sản phẩm
2. **Đặt tên rõ ràng:** Sử dụng từ viết tắt nhất quán và dễ nhớ
3. **Kiểm tra trùng lặp:** Module tự động kiểm tra SKU trùng, nhưng nên kiểm tra thủ công
4. **Backup dữ liệu:** Thường xuyên backup dữ liệu thuộc tính
5. **Đào tạo người dùng:** Đảm bảo người dùng hiểu cách sử dụng module

## Troubleshooting

### SKU không được tạo tự động
- Kiểm tra: Đã chọn đủ thuộc tính chưa?
- Kiểm tra: "Tự động tạo mã SKU" đã bật chưa?

### SKU bị trùng
- Module sẽ cảnh báo nếu SKU trùng
- Kiểm tra sản phẩm đã tồn tại
- Có thể thêm thuộc tính "Đặc biệt" để phân biệt

### Không thấy menu
- Đảm bảo module đã được cài đặt
- Kiểm tra quyền truy cập
- Refresh trình duyệt (Ctrl+F5)

## Tác giả

Odoo

## License

LGPL-3
