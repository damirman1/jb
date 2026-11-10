from db import connect_db

# 03 Переименование товара 
# Запросите ID и новое имя. Отсекайте пустой ввод до запроса. Покажите, найден ли товар. Проверьте, что цена и остаток не изменились

def rename_product():
    product_id = input("Введите ID товара: ").strip()
    if not product_id:
        print("ID товара не может быть пустым!")
        return
    
    new_name = input("Введите новое имя товара: ").strip()
    if not new_name:
        print("Новое имя товара не может быть пустым!")
        return
    
    sql = """
        UPDATE terminal_products
        SET name = %s
        WHERE id = %s
    """
    
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (product_id,))
            product = cur.fetchone()
            
            if product is None:
                print(product_id)
                return
            
            cur.execute(sql, (new_name, product_id))
            conn.commit()
            
