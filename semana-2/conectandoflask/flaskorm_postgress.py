from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, types
from sqlalchemy.sql.schema import ForeignKey
app = Flask(__name__)

#dialect : //nombres:password@host/db
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:root@localhost/empresa'

conexion = SQLAlchemy(app)

class Trabajador(conexion.Model):     
        id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
        nombre = Column(type_=types.String(length=100), nullable=False)
        habilitado = Column(type_=types.Boolean, default=True)
        # sirva para indicar lo que seria la tbala en la base de datos
        __tablename__='trabajadores'

class Direccion(conexion.Model):        
        id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
        nombre = Column(type_=types.String(length=250), nullable=True)
        numero = Column(type_=types.Integer)        
        #identifica = Column(type_=types.Integer)
        #Llave foranea
        # trabajadorId = Column(ForeignKey(column='trabajadores.id'),
        #   type_ = types.Integer, nullable = False, name = 'trabajador_id')

        __tablename__ = 'Direccion'
        # trabajador_Id = Column(ForeignKey('Trabajador.id'), type_ = types.Integer, nullable = False)
        #  request_id = db.Column(db.Integer, db.ForeignKey('request.id'))
        #  request = db.relationship("Request", backref=backref("request", uselist=False))
        

@app.route('/')
def home():
     print("Yo me ejecuto")
     conexion.create_all()
     

@app.route('/trabajadores', methods=['GET','POST'])
def trabajadores():
    if request.method == 'GET':
        # resultado = conexion.session.query(Trabajador).all()
        resultado : list[Trabajador] = conexion.session.query(Trabajador).all()
        print(resultado)
        trabajadores=[]

        for trabajor in resultado:
            trabajadores.append({
                'id': trabajor.id,
                'nombre': trabajor.nombre,
                'habilitado': trabajor.habilitado,
            })

        return {
            'content ': trabajadores
        }
    elif request.method == 'POST':
        data = request.get_json()

        new_trabajador = Trabajador(
            nombre = data.get('nombre'),
            habilitado = data.get('habilitado')
        )

        print(new_trabajador)
        #Registramos los cambios en la bd
        conexion.session.add(new_trabajador)

        #Guardamos los cambios de manera permanente
        conexion.session.commit()
        return {
            'message ': 'Trabajador creado exitosamente'
        }


@app.route('/direcciones', methods=['POST'])
def gestion_direcciones():    
        data = request.get_json()   
        new_direccion=Direccion(**data)
        conexion.session.add(new_direccion)

        # new_direccion = Direccion(
        #     id=data.get('id'),
        #     nombre = data.get('nombre'),
        #     numero = data.get('numero')
        # )        

        #Registramos los cambios en la bd
        #conexion.session.add(new_direccion)

        #Guardamos los cambios de manera permanente
        conexion.session.commit()
        return {
            'message ': 'Direccion creado exitosamente'
        }        


@app.route('/direcciones/<int:TrabajadorId>', methods=['GET'])
def devolver_direcciones():    
    resultado : list[Direccion] = conexion.session.query(Direccion).filter_by(TrabajadorId=TrabajadorId)
    print(resultado)
    
    if resultado is None:
        return jsonify({
        "message": "No hay datos"
        })
    
    for direccion in resultado:
        direcciones.append({
            'id':direccion_id,
            'nombre': direccion.nombre,
            'numero': direccion.numero
        })
    return{
        'content': direcciones
    }

    # ------------------
    # if request.method =='POST':
        # try:
            # data = request.get_json()

            # new_direccion = Direccion(
            #     nombre = data.get('nombre'),
            #     numero = data.get('numero'),
            #     trabajador_Id = data.get('trabajador_Id')
            # )

         
            # new_direccion = Direccion(**data)
            # print(new_direccion)
            
            #print(direcciones)
            # print(nuevaDireccion)
            # conexion.session.add(nuevaDireccion)
            # conexion.session.commit()
            # return {
            #     'message': 'Direccion agregada exitosamente'
            # }
        # except:
        #     return {
        #         'message': 'Error al agregar Direccion'
        #     },400


app.run(debug=True)










