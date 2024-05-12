from django.contrib import admin
from Vets.models import AnimalMascota
from Vets.models import Raza
from Vets.models import Mascota
from Vets.models import Cita
from Vets.models import HistorialCita
from Vets.models import Vacuna
from Vets.models import Vacunacion

# Register your models here.
admin.site.register(AnimalMascota)
admin.site.register(Raza)
admin.site.register(Mascota)
admin.site.register(Cita)
admin.site.register(HistorialCita)
admin.site.register(Vacuna)
admin.site.register(Vacunacion)