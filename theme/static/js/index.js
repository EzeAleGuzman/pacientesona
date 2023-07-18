document.addEventListener('DOMContentLoaded', function () {
  console.log('DOMContentLoaded event fired');
  const servicioSelect = document.getElementById('servicio-select');
  const pacientesContainer = document.querySelector('.pacientes-container');
  const pacientes = pacientesContainer.children;

  const searchInput = document.getElementById('search-input');
  const searchButton = document.getElementById('search-button');
  const countPacientes = document.getElementById('count-pacientes');

  function updateCount() {
    const visiblePacientes = Array.from(pacientes).filter(paciente => paciente.style.display !== 'none').length;
    countPacientes.textContent = `Mostrando ${visiblePacientes} paciente(s)`;
  }

  searchButton.addEventListener('click', function () {
    const searchTerm = searchInput.value.toLowerCase().trim();

    Array.from(pacientes).forEach(paciente => {
      const nombreApellido = paciente.textContent.toLowerCase();
      if (nombreApellido.includes(searchTerm)) {
        paciente.style.display = 'block';
      } else {
        paciente.style.display = 'none';
      }
    });

    updateCount();
  });

  servicioSelect.addEventListener('change', function () {
    const servicioSeleccionado = servicioSelect.value;
    console.log('Servicio seleccionado:', servicioSeleccionado);
    Array.from(pacientes).forEach(paciente => {
      if (servicioSeleccionado === '' || paciente.textContent.includes(servicioSeleccionado)) {
        paciente.style.display = 'block';
      } else {
        paciente.style.display = 'none';
      }
    });

    updateCount();
  });
});
