#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tạo file XML với sản phẩm mẫu: Bulong A193 B7 và B8
"""

PRODUCT_TYPES = ['HB']
STANDARDS = ['A193M']
GRADES = ['B7', 'B8']
DIAMETERS = ['M12', 'M14', 'M16', 'M18', 'M20', 'M22', 'M24', 'M27', 'M30', 'M32', 'M36']
LENGTHS = ['L100', 'L150', 'L200', 'L250', 'L300', 'L350', 'L400', 'L450', 'L500']

xml_content = '''<?xml version="1.0" encoding="utf-8"?>
<odoo>
'''

product_id = 1

for product_type in PRODUCT_TYPES:
    for standard in STANDARDS:
        for grade in GRADES:
            for diameter in DIAMETERS:
                for length in LENGTHS:
                    sku_parts = [product_type, standard, grade, diameter, length]
                    sku = ' '.join(sku_parts)
                    name = f"Bulong {standard} {grade} {diameter} {length}"
                    
                    xml_content += f'''    <record id="product_sample_{product_id}" model="product.template">
        <field name="name">{name}</field>
        <field name="default_code">{sku}</field>
        <field name="product_type_attr" ref="attr_value_{product_type.lower()}"/>
        <field name="standard_attr" ref="attr_value_{standard.lower()}"/>
        <field name="grade_attr" ref="attr_value_{grade.lower()}"/>
        <field name="diameter_attr" ref="attr_value_{diameter.lower()}"/>
        <field name="length_attr" ref="attr_value_{length.lower()}"/>
        <field name="auto_generate_sku">True</field>
        <field name="sale_ok">True</field>
        <field name="purchase_ok">True</field>
        <field name="type">product</field>
    </record>
'''
                    product_id += 1

xml_content += '</odoo>'

with open('/Users/baonguyen/Desktop/app/Odoo/product_attributes/data/product_sample_products.xml', 'w', encoding='utf-8') as f:
    f.write(xml_content)

print(f"✅ Đã tạo {product_id - 1} sản phẩm mẫu")
print(f"   - Loại: {', '.join(PRODUCT_TYPES)}")
print(f"   - Tiêu chuẩn: {', '.join(STANDARDS)}")
print(f"   - Cấp bền: {', '.join(GRADES)}")
print(f"   - Đường kính: {len(DIAMETERS)} kích thước ({', '.join(DIAMETERS[:3])}...{DIAMETERS[-1]})")
print(f"   - Chiều dài: {len(LENGTHS)} kích thước ({', '.join(LENGTHS[:3])}...{LENGTHS[-1]})")
print(f"   File: product_attributes/data/product_sample_products.xml")
