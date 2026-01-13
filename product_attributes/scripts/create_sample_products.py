#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để tạo sản phẩm mẫu: Bulong A193 B7 và B8
Kích thước: M12-M36
Chiều dài: 100-500
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom

# Cấu hình
PRODUCT_TYPES = ['HB']  # Hex Bolt
STANDARDS = ['A193M']
GRADES = ['B7', 'B8']
DIAMETERS = ['M12', 'M14', 'M16', 'M18', 'M20', 'M22', 'M24', 'M27', 'M30', 'M32', 'M36']
LENGTHS = ['L100', 'L150', 'L200', 'L250', 'L300', 'L350', 'L400', 'L450', 'L500']

def create_product_xml():
    """Tạo file XML với các sản phẩm mẫu"""
    
    root = ET.Element('odoo')
    
    product_id = 1
    
    for product_type in PRODUCT_TYPES:
        for standard in STANDARDS:
            for grade in GRADES:
                for diameter in DIAMETERS:
                    for length in LENGTHS:
                        # Tạo SKU: HB A193M B7 M12 L100
                        sku_parts = [product_type, standard, grade, diameter, length]
                        sku = ' '.join(sku_parts)
                        
                        # Tên sản phẩm
                        name = f"Bulong {standard} {grade} {diameter} {length}"
                        
                        # Tạo record
                        record = ET.SubElement(root, 'record')
                        record.set('id', f'product_sample_{product_id}')
                        record.set('model', 'product.template')
                        
                        # Name
                        field_name = ET.SubElement(record, 'field')
                        field_name.set('name', 'name')
                        field_name.text = name
                        
                        # Default code (SKU)
                        field_code = ET.SubElement(record, 'field')
                        field_code.set('name', 'default_code')
                        field_code.text = sku
                        
                        # Product type attribute
                        field_type = ET.SubElement(record, 'field')
                        field_type.set('name', 'product_type_attr')
                        field_type.set('ref', f'attr_value_{product_type.lower()}')
                        
                        # Standard attribute
                        field_std = ET.SubElement(record, 'field')
                        field_std.set('name', 'standard_attr')
                        field_std.set('ref', f'attr_value_{standard.lower()}')
                        
                        # Grade attribute
                        field_grade = ET.SubElement(record, 'field')
                        field_grade.set('name', 'grade_attr')
                        field_grade.set('ref', f'attr_value_{grade.lower()}')
                        
                        # Size attribute - cần tạo composite hoặc dùng diameter
                        # Tạm thời chỉ dùng diameter, length sẽ được thêm sau
                        field_size = ET.SubElement(record, 'field')
                        field_size.set('name', 'size_attr')
                        field_size.set('ref', f'attr_value_{diameter.lower()}')
                        
                        # Auto generate SKU
                        field_auto = ET.SubElement(record, 'field')
                        field_auto.set('name', 'auto_generate_sku')
                        field_auto.text = 'True'
                        
                        # Sale ok
                        field_sale = ET.SubElement(record, 'field')
                        field_sale.set('name', 'sale_ok')
                        field_sale.text = 'True'
                        
                        # Purchase ok
                        field_purchase = ET.SubElement(record, 'field')
                        field_purchase.set('name', 'purchase_ok')
                        field_purchase.text = 'True'
                        
                        # Type
                        field_type_prod = ET.SubElement(record, 'field')
                        field_type_prod.set('name', 'type')
                        field_type_prod.text = 'product'
                        
                        product_id += 1
    
    # Format XML
    xml_str = ET.tostring(root, encoding='unicode')
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent='    ', encoding='utf-8')
    
    return pretty_xml

if __name__ == '__main__':
    xml_content = create_product_xml()
    with open('/Users/baonguyen/Desktop/app/Odoo/product_attributes/data/product_sample_products.xml', 'wb') as f:
        f.write(xml_content)
    print(f"Đã tạo {len(PRODUCT_TYPES) * len(STANDARDS) * len(GRADES) * len(DIAMETERS) * len(LENGTHS)} sản phẩm mẫu")
    print("File: product_attributes/data/product_sample_products.xml")
