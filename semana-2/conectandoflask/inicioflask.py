from flask import Flask, request

# Indica nuestro arhivo principal 
app = Flask(__name__)

productos = [
    {
        "id":1,
        "producto":"Manzana",
        "precio": 3.50
    },
    {
        "id":2,
        "producto":"Platano",
        "precio": 2.50
    },
    {
        "id":3,
        "producto":"Fresas",
        "precio": 4.20
    },
    ]

@app.route('/')
def inicio():
    return "<h1>Bienvenido a mi aplicacion</h1>"

@app.route('/productos', methods=['GET','POST'])
def gestion_productos():         
    if request.method=='GET':
      return {
         'content': productos
         }
    elif request.method=='POST':
        print(request.get_json())
        data = request.get_json()        
        item = data.get('producto') + ' creado exitosamente'   #nombre del producto
        print(item)
        productos.append(data)
        return {
            'message': item
         }


@app.route('/producto/<int:indice>',  methods=['GET','PUT','DELETE'])
def gestion_items(indice):
    if request.method=='GET':
        registro = len(productos)
        if registro < indice:
            return {
                    'message': 'El producto no existe.'
                    }    
        else:
            return {
                'content': productos[indice]
                }    
    elif request.method=='PUT':
        registro = len(productos)
        if registro < indice:
            return {
                    'message': 'El producto no existe.'
                    }    
        else:
            data = request.get_json()
            productos[indice] = data
            return {
                'messsage' : 'Producto actualizado exitosamente'
            }
    elif request.method=='DELETE':
        registro = len(productos)
        if registro < indice:
            return {
                    'message': 'El producto no existe.'
                    }    
        else:
            del productos[indice]
            return {
                'messsage' : 'Producto eliminado exitosamente'
            }
        
if __name__ == '__main__':
    app.run(debug=True)
