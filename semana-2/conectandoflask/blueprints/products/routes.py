from flask import Blueprint, jsonify, request
from extensions import db
from entities.product_model import Product

products_bp = Blueprint('product',__name__)

@products_bp.route('/api/v1/product')
def get_all_products():
    try:
        products = Product.query.all()

        dic_products = []

        for product in products:
            dic_products.append(product.to_dic())

        return jsonify({
            'products': dic_products
        })
    except Exception as e:
        return jsonify({
            "error": e,
            "linea": e.__traceback__.tb_lineno
        }), 500

#CREAR (POST)
@products_bp.route('/api/v1/product', methods=['POST'])
def create_product():
    try:
        product_data = request.get_json()
        new_product = Product(
            name =  product_data['name'],
            description = product_data['description'],
            price = product_data['price'],
            stock = product_data['stock'],
            )

        db.session.add(new_product)
        db.session.commit()
       
        return jsonify({
            "new_product": new_product.to_dic()
        }),201
    except Exception as e:
        return jsonify({
            "error": e,
            "linea": e.__traceback__.tb_lineno
        }),500

if __name__ == '__main__':
    with app.app_context():        
        db.create_all()
    app.run(port=7000, debug=True)


# DELETE
@products_bp.route('/api/v1/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        # buscar por id
        product = Product.query.get(product_id)

        if product is None:
            return jsonify({
                "message": "producto not found"
            })

        # eliminar al usuario
        db.session.delete(product)
        db.session.commit()

        return jsonify({
            "message": "Producto deleted"
        })
    except Exception as e:
        return jsonify({
            "error": e,
            "linea": e.__traceback__.tb_lineno
        }), 500


#BUSCAR ID 
@products_bp.route('/api/v1/product/<int:product_id>')
def get_product_by_id(product_id):
     try:
         product = Product.query.get(product_id)

         if product is None:
             return jsonify({
                 "message" : "producto not found"
             })

         return jsonify({
             "producto ": product.to_dic()
         })
     except Exception as e:
         return jsonify({
             "error ": e,
             "linea": e__traceback__.tb_lineno
         }),500