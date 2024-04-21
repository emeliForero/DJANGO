from django.http import JsonResponse
from .models import Animal, Contact
from django.views.decorators.csrf import csrf_exempt
import json



@csrf_exempt
def obtener_lista_animales(request):
    animales = Animal.objects.all()
    data = [{'animal_id': animal.animal_id, 'nombre': animal.name, 'especie': animal.species, 'edad': animal.age, 'url_image': animal.url_image} for animal in animales]
    return JsonResponse(data, safe=False)

@csrf_exempt
def agregar_animal(request):
    if request.method == 'POST':
        # Obtener los datos del cuerpo de la solicitud
        data = json.loads(request.body)
        animal_id = data.get('animal_id')
        name = data.get('name')
        age = data.get('age')
        species = data.get('species')
        url_image = data.get('url_image')
        state = data.get('state')
        shelter = data.get('shelter')

        animal = Animal.objects.create(animal_id=animal_id, name=name, age=age, species=species, url_image=url_image, state=state, shelter=shelter)
        
        # Devolver una respuesta
        return JsonResponse({'mensaje': 'Anminal agregado correctamente'}, status=201)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)    

@csrf_exempt
def agregar_contacto(request):
    if request.method == 'POST':
        # Obtener los datos del cuerpo de la solicitud
        data = json.loads(request.body)
        animal_id = data.get('animal_id')
        nombre_contacto = data.get('name')
        telefono = data.get('cell_phone')
        email = data.get('email')
        message = data.get('message')

        # Verificar si el animal existe
        try:
            animal = Animal.objects.get(animal_id=animal_id)
        except Animal.DoesNotExist:
            return JsonResponse({'error': 'El animal no existe'}, status=404)

        # Crear el nuevo contacto
        contacto = Contact.objects.create(animal_id=animal_id, name=nombre_contacto, cell_phone=telefono, email=email, message=message)
        
        # Devolver una respuesta
        return JsonResponse({'mensaje': 'Contacto agregado correctamente'}, status=201)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)