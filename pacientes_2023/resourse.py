from import_export import resources
from .models import Paciente

class PacienteResource(resources.ModelResource):
    class Meta:
        model = Paciente
        exclude = ('id',)

        fields = ('nombre', 'apellido', 'servicio', 'habitacion', 'cama')

    def before_import_row(self, row, **kwargs):
        # Convierte las opciones de servicio a valores válidos
        servicio_mapping = {
            'Clinica Medica': 'Clinica Medica',
            'Guardia Adultos': 'Guardia Adultos',
            'Maternidad': 'Maternidad',
            'Neo': 'Neo',
            'Partos': 'Partos',
            'Pediatria Guardia': 'Pedriatria Guardia',
            'Pediatria Internacion': 'Pediatria Internacion',
            'Polivalente': 'Polivalente',
            'Quirofano': 'Quirofano',
            'UCI': 'UCI',
            'UTI': 'UTI',
            'Coordinacion': 'Coordinacion',
            'Casa de Madres': 'Casa de Madres',
        }
        servicio = row.get('servicio')
        row['servicio'] = servicio_mapping.get(servicio, 'Clinica Medica')  # Establece 'Clinica Medica' como valor predeterminado si no coincide

class PacienteResourceWithDefaults(PacienteResource):
    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        # Establece valores predeterminados para los campos que no se proporcionen durante la importación
        default_values = {
            'servicio': 'Clinica Medica',  # Valor predeterminado para el servicio
            'habitacion': '',  # Puedes ajustar el valor predeterminado según tu caso
            'cama': '',  # Puedes ajustar el valor predeterminado según tu caso
        }
        for row in dataset.dict:
            for field_name, default_value in default_values.items():
                if field_name not in row:
                    row[field_name] = default_value

        super().before_import(dataset, using_transactions, dry_run, **kwargs)
