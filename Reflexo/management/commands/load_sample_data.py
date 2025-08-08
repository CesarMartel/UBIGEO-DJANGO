from django.core.management.base import BaseCommand
from Reflexo.models import Country, Region, Province, District

class Command(BaseCommand):
    help = 'Carga datos de ejemplo para demostrar la funcionalidad'

    def handle(self, *args, **options):
        self.stdout.write('Cargando datos de ejemplo...')
        
        # Crear países
        peru = Country.objects.create(name="Perú", phone_code="+51", ISO2="PE")
        mexico = Country.objects.create(name="México", phone_code="+52", ISO2="MX")
        colombia = Country.objects.create(name="Colombia", phone_code="+57", ISO2="CO")
        
        # Crear regiones
        costa = Region.objects.create(name="Costa")
        sierra = Region.objects.create(name="Sierra")
        selva = Region.objects.create(name="Selva")
        
        # Crear provincias
        lima = Province.objects.create(name="Lima", region=costa)
        arequipa = Province.objects.create(name="Arequipa", region=sierra)
        cusco = Province.objects.create(name="Cusco", region=sierra)
        loreto = Province.objects.create(name="Loreto", region=selva)
        
        # Crear distritos
        District.objects.create(name="Miraflores", province=lima)
        District.objects.create(name="San Isidro", province=lima)
        District.objects.create(name="Barranco", province=lima)
        District.objects.create(name="Arequipa", province=arequipa)
        District.objects.create(name="Yanahuara", province=arequipa)
        District.objects.create(name="Cusco", province=cusco)
        District.objects.create(name="San Sebastián", province=cusco)
        District.objects.create(name="Iquitos", province=loreto)
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Datos cargados exitosamente:\n'
                f'- {Country.objects.count()} países\n'
                f'- {Region.objects.count()} regiones\n'
                f'- {Province.objects.count()} provincias\n'
                f'- {District.objects.count()} distritos'
            )
        )




