document.addEventListener('DOMContentLoaded', function() {
  const dropdownLinks = document.querySelectorAll('.dropdown-content a');
  dropdownLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      if (link.textContent.includes('Admin')) {
        window.location.href = '/accounts/login/?type=admin';
      } else if (link.textContent.includes('Doctor')) {
        window.location.href = '/accounts/login/?type=doctor';
      } else if (link.textContent.includes('Patient')) {
        window.location.href = '/accounts/login/?type=patient';
      }
    });
  });
});
