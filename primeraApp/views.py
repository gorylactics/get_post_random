from django.shortcuts import render , HttpResponse , redirect

def index(request):
    return render(request,'index.html')

# def get_o_post(request):
#     if request.method == 'GET':
#         texto = 'esto es una respuesta GET'
#         print(texto)
#         contexto = {
#             'nombre' : texto
#         }
#         return render(request , 'formulario.html' , contexto)
    
#     if request.method == 'POST':
#         print(request.POST)
#         print('esto es una respuesta POST')
#         return redirect('/')

def formulario(request):
    if request.method == 'GET':
        texto = 'esto es una respuesta GET'
        print(texto)
        contexto = {
            'nombre' : texto
        }
        return render(request , 'formulario.html' , contexto)
    
    if request.method == 'POST':
        print(request.POST)
        valor1 = request.POST['datoUno']
        valor2 = request.POST['datoDos']
        valorTotal = [valor1,valor2]
        print(valorTotal)
        print('esto es una respuesta POST')
        return redirect('/')

def registrarUsuario(request):
    return render(request, 'registrarUsuario.html')

def usuarioRegistrado(request):
    # este funciona como servlet, solo toma la inforacion y la redirecciona
    print("Got Post Info....................")
    print(request.POST)
    valor1 = request.POST['nombre']
    valor2 = request.POST['correo']
    # print(f'los datos son: {valor1} y {valor2}')
    # contexto = {
    #     'valor1' : valor1,
    #     'valor2' : valor2,
    # }

    request.session['nombreUsuario'] = valor1
    request.session['emailUsuario'] = valor2

    # return render(request, 'usuarioRegistrado.html' , contexto)
    # nunca se debe renderizar un post ya que se podria guardar muchas veces en la base de datos
    return redirect('/mostrarUsuario')

def mostrarUsuario(request):
    return render(request , 'mostrarUsuario.html')

def terminarSesion(request):
    if 'nombreUsuario' in request.session:
        del request.session['nombreUsuario']
    if 'emailUsuario' in request.session:
        del request.session['emailUsuario']
    return redirect('/')